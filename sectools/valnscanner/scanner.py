#!/usr/bin/env python

import requests
import re
from bs4 import BeautifulSoup
import urllib.parse

class Scanner:
    def __init__(self, url, ignore_links):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = ignore_links

    def extract_link(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

    def crawl(self, url=None):
        if url == None:
            url = self.target_url
        links_list = self.extract_link(url)
        for link in links_list:
            link = urllib.parse.urljoin(url, link)
            if "#" in link:
                link = link.split("#")[0]
            if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:
                self.target_links.append(link)
                print(link)
                self.crawl(link)

    def extract_form(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, features="lxml")
        return parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urllib.parse.urljoin(url, action)
        method = form.get("method")
        input_list = form.findAll("input")
        post_data = {}
        for input in input_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value
            post_data[input_name] = input_value
        if method == "post":
            return self.session.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)

    def run_scan(self):
        for link in self.target_links:
            forms = self.extract_form(link)
            for form in forms:
                print("[+] Testing form in " + link)
                xss_vulnerbility = self.test_xss_in_form(form, link)
                if xss_vulnerbility:
                    print("[+++] XSS discovered in " + link + "in the following form")
                    print(form)

            if "=" in link:
                print("[+] Testing " + link)
                xss_vulnerbility = self.test_xss_in_link(link)
                if xss_vulnerbility:
                    print("[+++] XSS discovered in " + link)

    def test_xss_in_form(self, form, url):
        xss_test_script = "<sCript>alet('test')</scriPt>"
        response = self.submit_form(form, xss_test_script, url)
        return xss_test_script in response.content.decode()

    def test_xss_in_link(self, url):
        xss_test_script = "<sCript>alet('test')</scriPt>"
        url = url.replace("=", "=" + xss_test_script)
        response = self.session.get(url)
        return xss_test_script in response.content.decode()