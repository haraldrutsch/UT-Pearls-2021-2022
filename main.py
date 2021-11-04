import parserUT
import counter

#Main is going to be our Program.
url = "https://bronto.ewi.utwente.nl/ecadata/sports-20191117.txt"
time_interval = 10*60 #in seconds
first_time = 1573905101
new_data = []
new_data = parserUT.parserI(url, time_interval, first_time)

print(counter.counter_for_graph(new_data,time_interval))
