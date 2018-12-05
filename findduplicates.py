# Takes an input text file containing a list of search paths
# These paths can be absolute or relative
# and looks for files that are duplicates, or looks for files that are not duplicates

# This script will go through every file in these search paths, descending into subfolders if necessary, and identify the duplicates
# Internally, this script hashes every file encountered and stores the <hash, file-path> pair in a dictionary. If duplicates are found, they will be put into another data structure - maybe another dictionary, with the <hash, filepaths> as key-value pairs

# by default, if no other arguments are provided, the duplicate files are printed on standard output
# -p <pickle-file> - if specified, this script will save the duplicate file dictionary in a pickle file
# -u - if specified, the script will output the unique files instead

import os, hashlib
import sys

def file_hash(filename):
    ''' Returns the SHA256 hash of a file.
    The return value is a string'''
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
            return h.hexdigest()



filename = sys.argv[1]
thehash = file_hash(filename)
print(thehash)
print(type(thehash))




# print(file_hash(filename))

#for arg in sys.argv:
#    print(arg)
