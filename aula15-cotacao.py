import datetime
import time
import requests
import json

while True:

    requisic = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = json.loads(requisic.text)

    print('### COTAÇÃO EM TEMPO REAL ###', datetime.datetime.now())
    print('Dólar:', cotacao['USDBRL']['high'])
    print('Euro:', cotacao['EURBRL']['high'])
    print('BTC:', cotacao['BTCBRL']['high'])
    time.sleep(2)


