import requests
from lxml import html

link = "https://www.betfair.com/sport/inplay"

start_page = requests.get(link)
tree = html.fromstring(start_page.text)

events_list = []
home_score = tree.xpath("//span[@class='ui-score-home']/text()")[6]
away_score = tree.xpath("//div[@class='sport-1']//*/a[@data-sport='SOCCER']//*/span[@class='home-team-name']/text()")
#name = tree.xpath("//span[@class='home-team-name']/text()")[1]
events_id = tree.xpath("//div[@class='sport-1']//*/a[@data-sport='SOCCER']/@href")

#for event in events_id[::2]:
    #print "https://www.betfair.com" + event

for awsc in away_score:
    print awsc