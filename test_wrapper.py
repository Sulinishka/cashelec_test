import requests
import sys
import random
from datetime import datetime

class RequestAPI():
    api_url = "https://api.coinmarketcap.com/v2/ticker/"
    api_key = "d823f698-42dc-42b4-9984-9a2cb87d9ee9"
    headers = {
     'Accept': 'application/json',
     'Accept-Encoding': 'deflate, gzip',
     'X-CMC_PRO_API_KEY': api_key,
    }
    
    def __init__(self):
        self.ticker = requests.get(self.api_url).json()
        self.top_10 = self.extract_top_10()
        self.urls = self.get_target_urls()
        print("top10 ", self.top_10)
        
    def extract_top_10(self):
        currencies = self.ticker["data"]
        volume_dict = {}
        for key in currencies.keys():
            name = currencies[key]["symbol"]
            volume = currencies[key]["quotes"]["USD"]["volume_24h"]
            volume_dict.update({name:volume })
        return sorted(volume_dict.items(), key=lambda kv: kv[1], reverse=True)[:10]

    def get_target_urls(self):
        crypto_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={}&convert=USD'
        target_urls = [crypto_url.format(tup[0]) for tup in self.top_10]
        return target_urls

    def get_ping(self, url=None):
        """ Returns ping in ms 
            (time taken between sending 
            the first byte of the request and 
            inishing parsing the header)
        """
        if not url:
            url = random.choice(self.urls)
        ping = requests.get(url, headers=self.headers).elapsed.microseconds/1000
        return ping

    def get_packet_size(self, url):
        """ Returns pocket size in kB """
        resp = requests.get(url, headers=self.headers)
        return sys.getsizeof(resp.content)/1024

    def get_last_update_delta(self, url):
        resp = requests.get(url, headers=self.headers).json()
        try:
            curr = list(resp["data"].keys())[0]
            last_updated = resp["data"][curr]["last_updated"].split("T")[0]
            last_updated_dt = datetime.strptime(last_updated, '%Y-%m-%d')
            delta_days = datetime.now() - last_updated_dt
            return delta_days
        except BaseException as e:
            print("\nErr: ", "you banned", e, resp)



