<<<<<<< HEAD
import json
import urllib.request

url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"
file = urllib.request.urlopen(url)

for line in file:
    tweetAux = json.loads(line)
    print(tweetAux['created_at'], "-", tweetAux['text'].encode('utf-8'), file=open('output.txt', 'a'))

=======
import json
import urllib.request

url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"
file = urllib.request.urlopen(url)

for line in file:
    tweetAux = json.loads(line)
    print(tweetAux['created_at'], "-", tweetAux['text'].encode('utf-8'), file=open('output.txt', 'a'))

>>>>>>> 185413b7629c1af7f1202599a13a24ed46ce1414
print('done')