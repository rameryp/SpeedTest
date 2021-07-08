import os
import re
import subprocess
import time
from influxdb import InfluxDBClient

filename = '/home/pi/speedtest/speedtest.csv'
response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
jitter = re.search('\((.*?)\s.+jitter\)\s', response, re.MULTILINE)

ping = ping.group(1)
download = download.group(1)
upload = upload.group(1)
jitter = jitter.group(1)

#try:
#    f = open('/home/pi/speedtest.csv', 'a+')
#    if os.stat('/home/pi/speedtest.csv').st_size == 0:
#            f.write('Date,Time,Ping (ms),Jitter (ms),Download (Mbps),Upload (Mbps)\r\n')
#except:
#    pass

#f.write('{},{},{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), ping, jitter, download, upload))


speed_data = [
    {
        "measurement" : "internet_speed",
        "tags" : {
            "host": "RPI-2B-4"
        },
        "fields" : {
            "download": float(download),
            "upload": float(upload),
            "ping": float(ping),
            "jitter": float(jitter)
        }
    }
]

client = InfluxDBClient('localhost', 8086, 'speemonitor', 'speed1234', 'internetspeed')
client.write_points(speed_data)
