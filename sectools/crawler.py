#!/usr/bin/env python
import requests

base_url = ".google.com"

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

with open("/root/wordlist.txt", "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        url = word + base_url
        response = request(url)
        if response:
            print("[-] subdomain fuond  " + url)