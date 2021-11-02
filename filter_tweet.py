import re

sports = ["baseball", "basketball", "volleyball", "tennis", "cricket", "soccer", "football", "rugby"]


def filter_by_sport(input):
    global sports
    rem_input = remove_special_chars(input)
    input_split_spaces = re.split(" ", rem_input.lower())

    twt_sport = []

    for word in input_split_spaces:
        x = 0
        while x < len(sports):
            if word == sports[x]:
                twt_sport.append(sports[x])
            x += 1
    return remove_dups(twt_sport)


def remove_special_chars(input):
    return re.sub("[^A-Za-z0-9 ]+", " ", input)


def remove_dups(data):
    res = []
    if len(data) != 0:
        fresh = data[0]
        i = 1
        while len(data) > i >= 0:
            if data[i] != fresh:
                res.append(fresh)
                fresh = data[i]
            i += 1
        res.append(fresh)
    return res


def main():
    print("incorrect call")



