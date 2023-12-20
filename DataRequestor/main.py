from time import sleep
#from snap7.server import mainloop
import requests

class WeatherRequester:
    def __init__(self, myx):
        self.x = myx
        self.dic = {
            "limit": 100,
            "page": 1,
            "offset": 0,
            "sort":"desc",
            "radius":1000,
            "city":self.x,
            "order_by":"lastUpdated",
            "dump_raw":False}
    def __str__(self):
        return f" lokalizacja to {self.myx}"
    def get_data(self):
        res = requests.get("https://api.openaq.org/v2/locations", params=self.dic).json()
        print(res['results'][0])

while (True):
    s  = input("podaj lokalizacje: ")
    p = WeatherRequester(s)
    print( "Wybrano", p.x)
    p.get_data()
    sleep(30)




