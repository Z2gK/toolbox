# Takes an input text file containing a list of search paths
# These paths can be absolute or relative
# and looks for files that are duplicates, or looks for files that are not duplicates

# This script will go through every file in these search paths, descending into subfolders if necessary, and identify the duplicates
# Internally, this script hashes every file encountered and stores the <hash, file-path> pair in a dictionary. If duplicates are found, they will be put into another data structure - maybe another dictionary, with the <hash, filepaths> as key-value pairs

# by default, if no other arguments are provided, the duplicate files are printed on standard output
# -p <pickle-file> - if specified, this script will save the duplicate file dictionary in a pickle file
# -u - if specified, the script will output the unique files instead

import os, hashlib, sys, pickle

# This function may have a problem with zero byte files - Seems to be fixed
# Reference: https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
def filehash(filename):
    ''' Returns the SHA256 hash of a file.
    The return value is a string'''
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
    return h.hexdigest()


def readpathlist(fp):
    ''' Takes a file pointer as the input and goes through the paths on each line
    Returns a list of paths provided in this file
    WARNING: No error checking is implemented! '''
    return [x.strip() for x in fp if x.strip() != ""]
        


def duplicates(pathlist):
    ''' This function takes a list of filepaths as input and returns 
    a dictionary of information about the duplicates. 
    <key, value> = <hash of file, (list of filepaths where this occurs)>'''
    allfiles = {} # Stores a dict of all files scanned so far
    dups = {} # Stores a dict of duplicates found so far
    for path in pathlist:
        for root, dirs, files in os.walk(path):
            for name in files:
                filepath = os.path.join(root,name)
                h = filehash(filepath) # may have a problem with zero byte files - Fixed
                # Deal with the edge case where one path is inside another
                if h in allfiles:      # this file has been seen before
                    if h in dups:  # this file has been seen at least twice
                        dups[h].append(filepath)
                    else:  # this file has been seen only once
                        dups[h] = [allfiles[h], filepath]
                else: # this file has not been seen before
                    allfiles[h] = filepath
    return allfiles, dups

def unique(pathlist):
    ''' To find unique files '''
    u,d = duplicates(pathlist)
    for key in d:
        u.pop(key)
    return u
    

def pickledict(d, filename):
    ''' This function takes in a dictionary and a filename and saves the dictionary to
    a pickle file'''
    fp = open(filename, "wb")
    pickle.dump(d, fp)
    fp.close()

def printresult(d):
    ''' This function takes a dictionary as the input and prints it to standard output '''
    for k, v in d.items():
        print(k)
        for s in v:
            print(s)
        print()

filename = sys.argv[1]
#thehash = filehash(filename)
#print(thehash)
#print(type(thehash))

with open(filename, "r") as fp:
    filelist = readpathlist(fp)

print(filelist)
# all,d = duplicates(filelist)
# printresult(d)
#pickledict(d, "dupfiles.p")
#print(d)

u = unique(filelist)
print(u)

# print(filehash(filename))

#for arg in sys.argv:
#    print(arg)
