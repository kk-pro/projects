import requests 
from bs4 import BeautifulSoup
import urllib.parse

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://IP/index.php"

response = request(target_url)

parsed_html = BeautifulSoup(response.content, 'html.parser')
forms_list = parsed_html.findAll("form")

for form in forms_list:
    action = form.get("action")
    method = form.get("method")
    post_url = urllib.parse.urljoin(target_url, action)
    
    inputs_list = parsed_html.findAll("input")
    post_data = {}
    for inputs in inputs_list:
        inputs_name = inputs.get("name")
        inputs_type = inputs.get("type")
        inputs_value = inputs.get("value")
        if inputs_type =="text":
            inputs_value = "HELLO"
        post_data[inputs_name] = inputs_value
    result = requests.post(target_url, data= post_data)
    print(result.text)
