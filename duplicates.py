import os
import hashlib

def file_hash(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
            return h.hexdigest()

#PATH = "/mnt/veracrypt1/zuijinshanleg"
#PATH = "/mnt/veracrypt1/zztest"
#PATH = "/mnt/veracrypt1/trx2fon"
#PATH = "/mnt/veracrypt1/tumblrs"
#PATH = "/mnt/veracrypt1/Vids2016"
#PATH = "/mnt/veracrypt1/VidsApr2013"
#PATH = "/mnt/veracrypt1/stuffof2015"
#PATH = "/mnt/veracrypt1/vids/pr"
PATH = "/mnt/veracrypt1/vids/pr-3"
allfiles = {}
duplicates = {}
for root, dirs, files in os.walk(PATH):
    for names in files:
        longfilename =  os.path.join(root, names)
#        print(longfilename)
        h = file_hash(longfilename)
        if h in allfiles:
            # add entry in duplicates
            if h in duplicates:
#                print(h)
#                print (duplicates[h])
                duplicates[h].append(longfilename)
            else:
                # add new entry to duplicates
                duplicates[h] = [allfiles[h], longfilename]
        else:
            allfiles[h] = longfilename
        
# print out files in master list
#for k,v in allfiles.items():
#   print (k + ": " + v)
# print out all duplicates
print("\nDUPLICATES")
for k,v in duplicates.items():
    print ("\n" + k + ":")
    for f in v:
        print(f)
