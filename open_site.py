import urllib

def open_site():
    connection_site = urllib.urlopen("https://www.betfair.com/sport")
    output_site = connection_site.read()
    print(output_site)
    connection_site.close()

open_site()