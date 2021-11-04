import json
import urllib.request
from counter import *
from filter_tweet import *


end_time = 0
itteration = 0


def parser(url, time_frame):
    json_file = urllib.request.urlopen(url)
    json_aux = json_file[0]
    first_tweet_time = convert_time_date_to_unix(json_aux['created_at'])

    return parserI(url, time_frame, first_tweet_time)

def parserI(url, time_frame, first_tweet_time):
    file = urllib.request.urlopen(url)

    global itteration
    global end_time

    cleaned_data = []

    if itteration == 0:
        tweet_time = first_tweet_time
    else:
        tweet_time = end_time

    for line in file:
        tweetAux = json.loads(line)
        if  convert_time_date_to_unix(tweetAux['created_at']) <= tweet_time + time_frame:
            input_data = convert_time_date_to_unix(tweetAux['created_at']), filter_by_sport(tweetAux['text']), tweetAux['text']
            cleaned_data.append(input_data)
            end_time = convert_time_date_to_unix(tweetAux['created_at'])
        else:
            break
    
    itteration += 1

    return cleaned_data


#print(parser("http://library.ewi.utwente.nl/ecadata/sports-20191117.txt",3))