from fileinput import filename
import requests, subprocess, os, json, sys

def save_file(filename,data):
    file = open(filename, "w+")
    print("creating " + filename)
    file.write(data)
    file.close()


def get_data():
    url = "http://127.0.0.1:8000/chain"
    response = requests.request("GET", url)
    results = json.loads(response.text)
    chains  = json.loads(response.text)["chain"]
    for chain in chains:
        json_data = chain["transactions"]
        for data in json_data:
            save_file(data['author'],data['content'])
            
        
get_data()