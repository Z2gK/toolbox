import xml.etree.ElementTree as ET
import requests
import time

def durationstr2mmss(t):
    sec = int(t[:-3])
    m = sec // 60
    s = sec % 60
    return "{}m {}s".format(m,s)
    
def epoch2time(t):
    e = int(t[:-3])
    return time.strftime("%d-%m-%Y %H:%M", time.localtime(e)) # might fail
    
url = 'https://np.tritondigital.com/public/nowplaying?mountName=SYMPHONY924AAC&numberToFetch=2&eventType=track'

response = requests.get(url)
xmlstring = response.text
# print(xmlstring)

root = ET.fromstring(xmlstring)

durationstr = root[0][0].text # final 3 digits could also be decimal places
unixtimestr = root[0][1].text # final 3 digits are decimal places
title = root[0][2].text
performer = root[0][3].text

print("\nNOW PLAYING ON SYMPHONY 92.4")
print("============================")
print("TITLE      : " + title)
print("PERFORMER  : " + performer)
print("DURATION   : " + durationstr2mmss(durationstr))
print("STARTED ON : " + epoch2time(unixtimestr))
print("\n")
