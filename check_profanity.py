import urllib

def read_txt():
    menaia = open("C:\Scripts\udacity\Sep11.txt")
    content_menaia = menaia.read()
    menaia.close()
    check_profanity(content_menaia)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=")
    output = connection.read()
    print(output)
    connection.close()

check_profanity("irmos")