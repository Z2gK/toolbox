import os
import hashlib

def file_hash(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
            return h.hexdigest()

# find files in two directory trees that are potentially not duplicates
# idea is to combine these two directories into one
# these two directories have lots of duplicates - can we collapse them into one?
# /mnt/veracrypt1/vids/pr
# /mnt/veracrypt1/vids/pr-3

DIR1="/mnt/veracrypt1/vids/pr"
DIR2="/mnt/veracrypt1/vids/pr-3"

dir1allfiles = {}
duplicates = {}

# build file index in DIR1
for root, dirs, files in os.walk(DIR1):
    for names in files:
        longfilename = os.path.join(root,names)
        h = file_hash(longfilename)
        if h not in dir1allfiles:
            dir1allfiles[h] = [longfilename]
        else:
            dir1allfiles[h].append(longfilename)

# Go through DIR2
dir2uniquefiles = {}
for root, dirs, files in os.walk(DIR2):
    for names in files:
        longfilename = os.path.join(root,names)
        h = file_hash(longfilename)
        if h in dir1allfiles or h in duplicates:
            # this is a duplicate in both dirs - record in duplicates
            if h in dir1allfiles:
                dir1allfiles.pop(h)
            if h not in duplicates:
                duplicates[h] = ""
        else:
            if h not in dir2uniquefiles:
                dir2uniquefiles[h] = [longfilename]
            else:
                dir2uniquefiles[h].append(longfilename)

# Files in dir1 that are not in dir2
print("\nFiles in dir1 that are not in dir2")
for k,v in dir1allfiles.items():
    print ("\n" + k + ":")
    for f in v:
        print(f)

# Files in dir2 that are not in dir2
print("\nFiles in dir2 that are not in dir1")
for k,v in dir2uniquefiles.items():
    print ("\n" + k + ":")
    for f in v:
        print(f)
