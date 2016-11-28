import xml.etree.ElementTree as ET
URL="http://radio.toggle.sg/static/symphony/billboard.xml"

tree = ET.parse('nowplay.xml')
tree.getroot()

rt = tree.getroot()
print (rt.tag)

for child in rt:
    # print child.tag, child.attrib
    x = child.attrib.get('eventType')
    print x
    if (x == 'Song'):
        print "Song detected"
        for child2 in child:
            title = child2.attrib.get('title')
            print title
            for child3 in child2:
                if (child3.tag == '{urn:schemas-rcsworks-com:SongSchema}Artist'):
                    player = child3.attrib.get('name')
                if (child3.tag == '{urn:schemas-rcsworks-com:SongSchema}Album'):
                    album = child3.attrib.get('title')
            print player, album
            # Fill in list of triplet title, player, album    


# print list and format in gui


#for child in rt.findall('Event'):
#    x = child.attrib.get('eventID')
#    y = child.attrib.get('eventType')
#    print x,y


        
    
