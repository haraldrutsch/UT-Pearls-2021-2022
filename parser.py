import json
import urllib.request
from counter import *

first_tweet_time = 	1573905101
end_time = 0
itteration = 0



def parser(url, time_frame):
    file = urllib.request.urlopen(url)

    global first_tweet_time
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
            input_data = convert_time_date_to_unix(tweetAux['created_at']), tweetAux['text'].encode('utf-8')
            cleaned_data.append(input_data)
            end_time = convert_time_date_to_unix(tweetAux['created_at'])
        else:
            break
    
    itteration += 1

    return cleaned_data

    