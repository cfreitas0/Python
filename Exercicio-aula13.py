import requests

requis = requests.get('https://www.msn.com/')

print(requis.text)