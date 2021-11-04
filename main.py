import filter_tweet
import counter
from parser import *
#Main is going to be our Program.
url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"
time_interval = 10*60 #in seconds
first_tweet

new_data = []
new_data = parser(url, time_interval)

cleaned_data