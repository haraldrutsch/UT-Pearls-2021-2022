import re

# creates a list with all the sport keywords
sports = ["baseball", "basketball", "volleyball", "tennis", "cricket", "soccer", "football", "rugby"]


# takes in a whole tweet and returns a list of all sports mentioned in it
def filter_by_sport(input):
    # declares sports a global var so that we can access it from within the function
    global sports

    # removes all special characters from the tweet
    # and then splits it into entries in a list that were separated from spaces
    rem_input = remove_special_chars(input)
    input_split_spaces = re.split(" ", rem_input.lower())

    twt_sport = []

    # checks if the words is in the sports list
    # if it is then it is added to a list, if not it is skipped
    for word in input_split_spaces:
        x = 0
        while x < len(sports):
            if word == sports[x]:
                twt_sport.append(sports[x])
            x += 1

    # if their were multiple repetitions of a sport in the tweet, they are removed
    # bubble sort needs to be before the removal of dupes
    # since dupes after a unique entry would not be removed
    return remove_dups(bubble_sort(twt_sport))


# uses RegEx to remove all special characters from an input
def remove_special_chars(input):
    return re.sub("[^A-Za-z0-9 ]+", " ", input)


# removes duplicates in a list
def remove_dups(data):
    # declares result list
    res = []

    # if data is not null it continues
    if len(data) != 0:
        fresh = data[0]
        i = 1
        # if the data keeps repeating itself in a row, it is ignored
        # if it is new it is added to the result list and it becomes the item to compare to
        while len(data) > i >= 0:
            if data[i] != fresh:
                res.append(fresh)
                fresh = data[i]
            i += 1
        # appends the last fresh item to the list
        res.append(fresh)
    return res


# orders elements from smallest to biggest
def bubble_sort(data):
    # copies data to result
    res = data[:]
    # creates a check in the end so we don't keep going through the list
    ui = len(res) - 1

    # goes through the list if the ending index is above 0
    while ui > 0:
        si = 0
        i = 0
        while i < ui:
            # if the current element is bigger than the next element they are swapped
            if res[i] > res[i + 1]:
                res[i], res[i + 1] = res[i + 1], res[i]
                si = i
            # indexes are updated
            i += 1
        ui = si
    return res


def main():
    print("incorrect call")



