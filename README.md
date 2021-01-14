# Resource Pack Builder

Github Workflow using python to read a configuration file and generate .zips based off its content

Configuration Options:
```py
{
  "pack_name": {
     # What the pack .zip will be named
    "sha1": "bool"
       # Boolean saying if a .json file with the pack's sha1 hash
       # Used for server resource packs
       # [default=false]
    "path": "string"
       # Folder to put the packs inside
       # [default="build"]
    "directory": "str"
       # Folder to look for files inside of
       # Set as "." for the main directory
       # [default="."]
    "files": [
       # List of files to put inside of the pack
       # [default=directory"
      "str"
    ]
  }
}
```

When adding a new pack, specifying a directory and no files will use all the files inside of the directory
You have to use either the "files" key or the "directory" key, else the build won't work
To add multiple packs, add a new "pack_name" in the file

If issues arise, [jsonlint](https://jsonlint.com/) is here to help
