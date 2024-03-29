from filter_tweet import *
import re
import datetime


# Counts the number of tweets for all kind of sports
def counter_for_graph(input_list, time_frame_unix):
    # Gets the unix time of the first tweet in the input list
    start_unix_time = input_list[0][0]
    # End of the timeframe
    end_unix_time = start_unix_time + time_frame_unix

    # Declaring all the lists that are going to be used
    unix_time_frames = []
    baseball_totals = []
    basketball_totals = []
    volleyball_totals = []
    tennis_totals = []
    cricket_totals = []
    soccer_totals = []
    football_totals = []
    rugby_totals = []

    # Declaring all counting variables that are going to be used
    baseball_num = 0
    basketball_num = 0
    volleyball_num = 0
    tennis_num = 0
    cricket_num = 0
    soccer_num = 0
    football_num = 0
    rugby_num = 0

    # Adds end of timeframe to list
    unix_time_frames.append(end_unix_time)
    time_frame_index = 0

    # Looks at if a sport is mentioned in a tweet
    # If it is empty it is skipped
    for tweet in input_list:
        if tweet[1] == []:
            continue
        # Looks whether the tweet is in the timeframe
        elif tweet[0] <= unix_time_frames[time_frame_index]:
            # Checks all the items in the list, for each item the corresponding counter is incremented
            for sport in tweet[1]:
                if sport == "baseball":
                    baseball_num += 1
                elif sport == "basketball":
                    basketball_num += 1
                elif sport == "volleyball":
                    volleyball_num += 1
                elif sport == "tennis":
                    tennis_num += 1
                elif sport == "cricket":
                    cricket_num += 1
                elif sport == "soccer":
                    soccer_num += 1
                elif sport == "football":
                    football_num += 1
                elif sport == "rugby":
                    rugby_num += 1
        else:
            # Adds everything to their respective lists and resets the variables
            unix_time_frames.append(unix_time_frames[time_frame_index] + time_frame_unix)
            time_frame_index += 1
            baseball_totals.append(baseball_num)
            baseball_num = 0
            basketball_totals.append(basketball_num)
            basketball_num = 0
            volleyball_totals.append(volleyball_num)
            volleyball_num = 0
            tennis_totals.append(tennis_num)
            tennis_num = 0
            cricket_totals.append(cricket_num)
            cricket_num = 0
            soccer_totals.append(soccer_num)
            soccer_num = 0
            football_totals.append(football_num)
            football_num = 0
            rugby_totals.append(rugby_num)
            rugby_num = 0

    # Combines all the lists into one list
    all_totals = [unix_time_frames, baseball_totals, basketball_totals, volleyball_totals, tennis_totals,
                  cricket_totals, soccer_totals, football_totals, rugby_totals]
    return all_totals


def convert_time_date_to_unix(input_time_date):
    # Assuming date time comes in form -> Sun Nov 17 04:38:18 +0000 2019
    # Splits the input coming in and harvests only relevant data and puts in a specific format
    split_input = re.split(" ", input_time_date)
    date_time_filtered = "{1}/{0}/{2}, {3}".format(convert_string_month_to_num(split_input[1]), split_input[2],
                                                   split_input[5], split_input[3])

    # coverts from this specific format into unix time
    date_format = datetime.datetime.strptime(date_time_filtered, "%d/%m/%Y, %H:%M:%S")
    unix_time = datetime.datetime.timestamp(date_format)
    return unix_time


# Converts unix time to date time
def convert_unix_to_time_date(input_unix):
    # Uses pythons built in functions to convert back to time stamp
    date_time = datetime.datetime.fromtimestamp(input_unix)
    return date_time.strftime('%d-%m-%Y %H:%M:%S')


# Converts the month abbreviation into a number
def convert_string_month_to_num(input_mon):
    if input_mon.lower() == "jan":
        return 1
    elif input_mon.lower() == "feb":
        return 2
    elif input_mon.lower() == "mar":
        return 3
    elif input_mon.lower() == "apr":
        return 4
    elif input_mon.lower() == "may":
        return 5
    elif input_mon.lower() == "jun":
        return 6
    elif input_mon.lower() == "jul":
        return 7
    elif input_mon.lower() == "aug":
        return 8
    elif input_mon.lower() == "sep":
        return 9
    elif input_mon.lower() == "oct":
        return 10
    elif input_mon.lower() == "nov":
        return 11
    elif input_mon.lower() == "dec":
        return 12
    else:
        return "Error: Month {0} not recognised".format(input_mon)
