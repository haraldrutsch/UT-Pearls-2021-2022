import json
import urllib.request

url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"
file = urllib.request.urlopen(url)

# Takes useful data from the .json file and saves result in output.txt
for line in file:
    tweetAux = json.loads(line)
    print(tweetAux['created_at'], "-", tweetAux['text'].encode('utf-8'), file=open('output.txt', 'a'))

print('done')