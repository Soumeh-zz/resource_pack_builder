from os.path import basename
from json import load
from zipfile import ZipFile
from pack_sha1 import generate_sha1
import os, sys

class ConfigError(Exception):
    pass

def read_config():
    try:
        with open('.github/workflows/config.json', 'r') as json:
            return load(json)
    except:
        raise ConfigError("Generating a blank config file, check config file documentation.")

def filter_config(config_dict):
    #try:
    for key, data in config_dict.items():

        # filter directory
        try:
            data['directory']
        except KeyError:
            data['directory'] = '.'

        if data['directory'] == '.':
            data['directory'] = ''
        else:
            data['directory'] = data['directory'].replace('/', '\\')

        # if no path specified, use 'build'
        try:
            data['path']
        except:
            data['path'] = 'build'
        if data['path'].endswith('/'):
            data['path'].rsplit('/')[0]
        
        # if no sha1, false
        try:
            data['sha1']
        except:
            data['sha1'] = ''
        
        # if no files specified, use all files from directory
        try:
            data['files']
        except KeyError:
            data['files'] = os.listdir(data['directory'])

        config_dict[key] = data

    return config_dict
    #except:
    #    raise ConfigError("Config file is incorrect, check config file documentation.")

def generate_zips(config_dict):
    main = os.getcwd()
    for zip_name, data in config_dict.items():
        file_name = data['path'] + '/' + zip_name + ".zip"
        if data['path'] not in os.listdir():
            os.mkdir(data['path'])
        with ZipFile(file_name, 'w') as zip_file:
            if data['directory']:
                os.chdir(main + '/' + data['directory'])
            else:
                os.chdir(main)
            for file in data['files']:
                if '.' in file:
                    zip_file.write(file)
                else:
                    for folder_name, sub_folder, file_names in os.walk(file):
                        for file in file_names:
                            file_path = os.path.join(folder_name, file)
                            zip_file.write(file_path)
        if data['sha1']:
            generate_sha1(file_name, zip_name, data['path'])

        os.chdir(main)

if __name__ == '__main__':
    config_dict = read_config()
    config_dict = filter_config(config_dict)
    generate_zips(config_dict)