import requests
from bs4 import BeautifulSoup
import urllib
import os 
from time import sleep


f = open("output.txt",'a')
filesize = os.path.getsize("output.txt")
if filesize != 0:
    print("If you continue you will overwrite the contents of output.txt. Please save that file now.")
    sleep(2)

keyword2 = input("What keyword would you like to search for?\n")
f.truncate(0)
def findLinks(keyword):
    global goodlinks_str
    goodlinks = []
    url = urllib.parse.quote(keyword + " site:pastebin.com", safe='')
    r = requests.get("http://www.google.com/search?q=" + url)
    soup = BeautifulSoup(r.text, 'lxml')

    for a in soup.find_all('a'):
        href = a['href']
        s1 = href.replace("/search?q=site:", "")
        s2 = s1.replace("/url?q=","")
        links = s2[0:29]
        
        for line in links.splitlines():
            if line.startswith('https://pastebin.com'):
                goodlinks.append(line)
            else:
                continue
    goodlinks_str = '\n'.join(goodlinks)
    return goodlinks_str

goodlinks = findLinks(keyword2)
for line in goodlinks.splitlines():
    r = requests.get(line)
    soup = BeautifulSoup(r.text, 'lxml')
    textarea = soup.find("textarea", {"class": "textarea"})
    def getAccounts():
        f = open("output.txt",'a')
        try:
            for line in textarea:
                if 'HQ' not in line and 'keywords' not in line and 'leaked' not in line and 'hulu subscription' not in line and 'tags' not in line:
                    if 'username' in line:
                        print(line.strip())
                        f.write(line.strip())
                    if 'accounts' in line:
                        print(line.strip())
                        f.write(line.strip())
                    elif '.net:' in line:
                        print(line.strip())
                        f.write(line.strip())


        except:
            print("Could not scrape")
    getAccounts()

