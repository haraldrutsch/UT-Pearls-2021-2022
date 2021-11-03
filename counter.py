from filter_tweet import *
import re
import datetime

filtered_data = 'output.txt'
sample_time_date_start = "Sat Nov 16 13:52:20 +0000 2019"
sample_time_date_end = "Sun Nov 17 04:38:18 +0000 2019"


# Think how this could be put into a stream and not read from file
def list_maker(input):
    with open(input, encoding='utf8') as in_file:
        all_lines = in_file.readlines()
    split_by_chars = ' - b'
    results = []
    for line in all_lines:
        parts = line.split(split_by_chars)
        parts[0] = convert_time_date_to_unix(parts[0])
        parts.append(filter_by_sport(parts[1]))
        results.append(parts)
    input = []
    for item in results:
        input.append(item)
    return input


def counter_for_graph(input_list, time_frame_unix):
    start_unix_time = input_list[0][0]
    end_unix_time = start_unix_time + time_frame_unix

    unix_time_frames = []
    baseball_totals = [0]
    basketball_totals = [0]
    volleyball_totals = [0]
    tennis_totals = [0]
    cricket_totals = [0]
    soccer_totals = [0]
    football_totals = [0]
    rugby_totals = [0]

    unix_time_frames.append(end_unix_time)
    time_frame_index = 0

    for tweet in input_list:
        if tweet[2] == []:
            continue
        elif tweet[0] <= unix_time_frames[time_frame_index]:
            print()
        else:
            unix_time_frames.append(unix_time_frames[time_frame_index] + time_frame_unix)
            time_frame_index += 1

    all_totals = [unix_time_frames, baseball_totals, basketball_totals, volleyball_totals, tennis_totals, cricket_totals, soccer_totals, football_totals, rugby_totals]
    return all_totals


def convert_time_date_to_unix(input):
    # Assuming date time comes in form -> Sun Nov 17 04:38:18 +0000 2019
    split_input = re.split(" ", input)
    date_time_filtered = "{1}/{0}/{2}, {3}".format(covert_string_month_to_num(split_input[1]), split_input[2], split_input[5], split_input[3])
    date_format = datetime.datetime.strptime(date_time_filtered, "%d/%m/%Y, %H:%M:%S")
    unix_time = datetime.datetime.timestamp(date_format)
    return unix_time


def convert_unix_to_time_date(input):
    print()
    # TODO: make this func
    # datetime.datetime.fromtimestamp(ms/1000.0)
    # to convert back into date time


def covert_string_month_to_num(input_mon):
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

