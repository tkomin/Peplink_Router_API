import requests
from getpass import getpass

user = 'admin'
password = getpass(prompt="Password : ")

url = 'https://router_ip/api/login'
payload = {'username': 'admin', 'password': password}


r1 = requests.post(url , data=payload, verify=False)

print(r1.text)
print(r1.cookies)

cookie = r1.cookies

r2 = requests.get('https://router_ip/api/auth.client', cookies=cookie , auth=('admin', password),
                 verify=False)

print(r2.text)


r3 = requests.get('https://router_ip/api/status.wan.connection', cookies=cookie, auth=('admin', password),
                 verify=False)

print(r3.text)


# if supported
r4 = requests.get('https://router_ip/api/info.location', cookies=cookie, auth=('admin', password),
                 verify=False)

print(r4.text)


r5 = requests.get('https://router_ip/api/status.pepvpn', cookies=cookie, auth=('admin', password),
                 verify=False)

print(r5.text)


r6 = requests.get('https://router_ip/api/status.lan.profile', cookies=cookie, auth=('admin', password),
                 verify=False)

print(r6.text)
