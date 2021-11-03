from filter_tweet import *

filtered_data = 'output.txt'


def tuple_maker(input):
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
