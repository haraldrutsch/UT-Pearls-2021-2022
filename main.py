import filter_tweet
import counter
from parser import *
#Main is going to be our Program.
url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"
file = urllib.request.urlopen(url)
time_interval = 10

new_data = parser(file, time_interval)
