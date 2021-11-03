from filter_tweet import *
import re

filtered_data = 'output.txt'
sample_time_date_start = "Sat Nov 16 13:52:20 +0000 2019"
sample_time_date_end = "Sun Nov 17 04:38:18 +0000 2019"


def list_maker(input):
    with open(input, encoding='utf8') as in_file:
        all_lines = in_file.readlines()
    split_by_chars = ' - b'
    results = []
    for line in all_lines:
        parts = line.split(split_by_chars)
        parts.append(filter_by_sport(parts[1]))
        results.append(parts)
    input = []
    for item in results:
        input.append(item)
    return input


def convert_time_date_to_unix_millis(input):
    # Assuming date time comes in form -> Sun Nov 17 04:38:18 +0000 2019
    split_input = re.split(" ", input)
    date_time_filtered = [split_input[1], split_input[2], split_input[3], split_input[5]]

# datetime.datetime.fromtimestamp(ms/1000.0)
# to convert back into date time