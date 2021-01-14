import hashlib, json, sys
BLOCKSIZE = 65536

def generate_sha1(file_name, zip_file, path):
    json_name = path + '/' + zip_file + "_sha1.json"
    hasher = hashlib.sha1()
    with open(file_name, 'rb') as zip_file:
        buf = zip_file.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = zip_file.read(BLOCKSIZE)
    with open(json_name, 'w+') as zip_file:
        json.dump({'sha1': hasher.hexdigest()}, zip_file)

for arg in sys.argv[1:]:
    args = arg.split(':')
    generate_sha1(args[0], args[1])