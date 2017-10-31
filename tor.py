# -*- coding: utf-8 -*-
import time
import requests
from bs4 import BeautifulSoup
import os

def get_soup(url):
    try:
        proxies = {
            "http": "socks5://{ip}".format(ip='127.0.0.1:9050'),
            "https": "socks5://{ip}".format(ip='127.0.0.1:9050'),
        }
        response = requests.get(url, proxies=proxies)
        soup = BeautifulSoup(response.text, 'html.parser')
        print soup
        return soup
    except Exception as e:
        print e
        

url = 'https://api.ipify.org?format=json'

def main():
    while 1:
        time.sleep(10)
        print "current tor IP..."
        get_soup(url)
        # os.system("""(echo authenticate '"这里更换成你的tor密码"'; echo signal newnym; echo quit) | nc kongfm.com 9051""")

if __name__ == "__main__":
    main()
