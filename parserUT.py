import json
import urllib.request
from counter import *
from filter_tweet import *

# Global variables
end_time = 0
iteration = 0

# Parser used for call outside of the module
def parser(url, time_frame):
    # Following code gets the "created_at" of the first tweet
    json_file = urllib.request.urlopen(url)

    json_aux = ""
    for line in json_file:
        json_aux = json.loads(line)
        break

    first_tweet_time = convert_time_date_to_unix(json_aux['created_at'])

    # Calls parserI for further processing
    return parserI(url, time_frame, first_tweet_time)

def parserI(url, time_frame, first_tweet_time):
    # Gets the .json file from a url
    file = urllib.request.urlopen(url)

    # Declaring global variables so they can be use in the function
    global iteration
    global end_time

    cleaned_data = []

    # Checks whether this is the first iteration of the parser
    # If so, uses the first_tweet_time, otherwise end_time of previous iteration
    if iteration == 0:
        tweet_time = first_tweet_time
    else:
        tweet_time = end_time

    # Goes through the json data and harvests all relevant data
    for line in file:
        tweetAux = json.loads(line)
        # Checks whether the current tweet was created inside the timeframe
        if  convert_time_date_to_unix(tweetAux['created_at']) <= tweet_time + time_frame:
            # Tries to fetch the quoted tweet
            # If it doesn't exist, it doesn't
            try:
                input_data = convert_time_date_to_unix(tweetAux['created_at']), filter_by_sport(tweetAux['text'] + tweetAux['extended_tweet']['full_text']), tweetAux['text']
            except:
                input_data = convert_time_date_to_unix(tweetAux['created_at']), filter_by_sport(tweetAux['text']), tweetAux['text']
            cleaned_data.append(input_data)
            end_time = convert_time_date_to_unix(tweetAux['created_at'])
        else:
            break
    
    iteration += 1

    return cleaned_data