import urllib
from xml.etree.ElementTree import parse

daves_latitude = 41.98062
candidates = ("1895","1394")

def distance(lat1, lat2):
    "Return distance in miles"
    return 69 * abs(lat1 - lat2)

def monitor():
    u = urllib.urlopen("freegeoip.net/xml/4.2.2.2")
    doc = parse(u)
    for bus in doc.findall("bus"):
        busid = bus.findtext("id")
        if busid in candidates:
            lat = float(bus.findtext("lat"))
            dis = distance(lat, daves_latitude)
            print busid, dis, "miles"
    print "-" * 10

import time
while True:
    monitor()
    #time.sleep(5)