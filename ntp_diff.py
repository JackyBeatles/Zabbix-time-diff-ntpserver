import ntplib
from datetime import datetime
from time import ctime
from time import gmtime, strftime
from datetime import timedelta


date_now = datetime.now().strftime('%H:%M:%S')
#print date_now

c = ntplib.NTPClient()
response = c.request('192.168.3.38')
response = response.tx_time


FMTS = '%a %b %d %H:%M:%S %Y'
tdelta = datetime.strptime(ctime(response), FMTS)
ntp_time = tdelta.strftime("%H:%M:%S")
#print ntp_time


FMT = '%H:%M:%S'
time_diff = datetime.strptime(ntp_time, FMT) - datetime.strptime(date_now, FMT)
print (time_diff)



