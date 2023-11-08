from time import sleep
#from snap7.server import mainloop
import requests

res = requests.get("https://api.openaq.org/v2/measurements?location_id=9342&parameter=no2&parameter=co&parameter=pm25&date_from=2023-11-07T10:55:08+01:00&date_to=2023-11-08T10:55:08+01:00&limit=1000").json() #wisniowa
res2 = requests.get("https://api.openaq.org/v2/measurements?location_id=10566&parameter=so2&parameter=pm10&parameter=co&parameter=no2&parameter=bc&parameter=pm25&parameter=o3&date_from=2023-11-07T09:58:56+01:00&date_to=2023-11-08T09:58:56+01:00&limit=1000").json() #conrada



while (True):
    #print('Test')
    print(res2['results'][0]['location'])
    sleep(2)
    #print (res.header)
    sleep(2)



