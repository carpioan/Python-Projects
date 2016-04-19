import requests
from bs4 import BeautifulSoup

#url = "http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=Los+Angeles%2C+CA"
url = "https://www.betfair.com/sport/inplay"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

g_data = soup.find_all("div")

print(g_data)
#for line in g_data.get("id"):
    #print(line)