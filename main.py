import parserUT
import counter

time = []
baseball = []
basketball = []
volleyball = []
tennis = []
cricket = []
soccer = []
football = []
rugby = []
new_data = []

#Main is going to be our Program.
url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"
time_interval = 10*60 #in seconds
total_time = 3*60*60
i = 0

for i in range(8):
    new_data = parserUT.parser(url, time_interval)

    temp = counter.counter_for_graph(new_data,time_interval-1)# -1 because some one fucked up on the backend
#print(temp)
    time.append(temp[0][0])
    baseball.append(temp[1][0]/(time_interval / 60))
    basketball.append(temp[2][0]/(time_interval / 60))
    volleyball.append(temp[3][0]/(time_interval / 60))
    tennis.append(temp[4][0]/(time_interval / 60))
    cricket.append(temp[5][0]/(time_interval / 60))
    soccer.append(temp[6][0]/(time_interval / 60))
    football.append(temp[7][0]/(time_interval / 60))
    rugby.append(temp[8][0]/(time_interval / 60))

print(rugby)
def start_time(url):
    json_file = urllib.request.urlopen(url)

    json_aux = ""
    for line in json_file:
        json_aux = json.loads(line)
        break

    first_tweet_time = convert_time_date_to_unix(json_aux['created_at'])
    return first_tweet_time