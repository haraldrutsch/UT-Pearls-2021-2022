import json
import urllib.request
from counter import *
from filter_tweet import *


# Parser used for call outside of the module
def parser(url, time_frame, time_frame_index):
    # Following code gets the "created_at" of the first tweet
    json_file = urllib.request.urlopen(url)

    json_aux = ""
    for line in json_file:
        json_aux = json.loads(line)
        break

    # Gets the time of the first tweet in the json file.
    # It then calculates at what time should we start counting tweets from
    first_tweet_time = convert_time_date_to_unix(json_aux['created_at'])
    tweet_parse_time = first_tweet_time + (time_frame * time_frame_index)

    # Calls parser_stage_two for further processing
    return parser_stage_two(url, time_frame, tweet_parse_time)


def parser_stage_two(url, time_frame, first_tweet_time):
    # Gets the .json file from a url
    file = urllib.request.urlopen(url)

    cleaned_data = []

    # Goes through the json data and harvests all relevant data
    for line in file:
        tweet_aux = json.loads(line)
        # Checks whether the current tweet was created inside the timeframe
        if convert_time_date_to_unix(tweet_aux['created_at']) < first_tweet_time:
            continue
        elif convert_time_date_to_unix(tweet_aux['created_at']) <= first_tweet_time + time_frame:
            # Tries to fetch the quoted tweet
            # If the quoted tweet doesn't exist then only the main tweet is fetched
            try:
                input_data = convert_time_date_to_unix(tweet_aux['created_at']), filter_by_sport(
                    tweet_aux['text'] + tweet_aux['extended_tweet']['full_text']), tweet_aux['text']
            except:
                input_data = convert_time_date_to_unix(tweet_aux['created_at']), filter_by_sport(tweet_aux['text']), \
                             tweet_aux['text']
            cleaned_data.append(input_data)
        else:
            break

    return cleaned_data
