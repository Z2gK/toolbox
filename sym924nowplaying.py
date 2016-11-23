import xml.etree.ElementTree as ET
tree = ET.parse('nowplay.xml')
tree.getroot()

rt = tree.getroot()
print (rt.tag)

for child in rt:
    for child2 in child:
        print(child2.tag)

    
