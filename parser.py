import json
import urllib.request

url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"
file = urllib.request.urlopen(url)

for line in file:
    tweetAux = json.loads(line)
    print(tweetAux['created_at'], "-", tweetAux['text'])