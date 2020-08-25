import sys
import xml.etree.ElementTree as ET
# from urllib.request import urlopen as URLopen
if (sys.version_info[0] == 2):
    from urllib import urlopen as URLopen
if (sys.version_info[0] == 3):
    from urllib.request import urlopen as URLopen

URL="http://radio.toggle.sg/static/symphony/billboard.xml"
f = URLopen(URL)
xmlstring = f.read()
f.close()


if (sys.version_info[0] == 2):
    ofp = open("out.xml", "w")
    ofp.write(xmlstring)
if (sys.version_info[0] == 3):
    ofp = open("out.xml", "w")
    ofp.write(xmlstring.decode('utf-8'))

ofp.close()

# print xmlstring

# tree = ET.parse('nowplay.xml')
# tree.getroot()
# rt = tree.getroot()

rt = ET.fromstring(xmlstring)
# print (rt.tag)

playlist = []

for child in rt:
    # print child.tag, child.attrib
    x = child.attrib.get('eventType')
    # print x
    if (x == 'Song'):
        # print "Song detected"
        for child2 in child:
            title = child2.attrib.get('title')
            # print title
            for child3 in child2:
                if (child3.tag == '{urn:schemas-rcsworks-com:SongSchema}Artist'):
                    player = child3.attrib.get('name')
                if (child3.tag == '{urn:schemas-rcsworks-com:SongSchema}Album'):
                    album = child3.attrib.get('title')
            # print player, album
            # Fill in list of triplet title, player, album    
            playlist.append((title, player, album))



# print list and format in gui
# print playlist
displaystring = ""
for tp in playlist:
    displaystring += tp[0]
    displaystring += "\n"
    displaystring += tp[1]
    displaystring += "\n"
    displaystring += tp[2]
    displaystring += "\n\n"
    
print (displaystring)
