#!/usr/bin/env python
import scanner
import requests

target_url = "http://IP/"
ignored_links = ["http://IP/logout.php"]
data_url = {"username":"admin", "password":"password", "Login":"submit"}
vunscan = scanner.Scanner(target_url, ignored_links)
vunscan.session.post("http://IP/login.php", data = data_url)

vunscan.crawl()
vunscan.run_scan()

