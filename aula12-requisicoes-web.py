import requests  #Beautiful Soup 4 . INSTALARA --> pip install bs4

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com',
             '_CF_IPcountry':'US' }

meus_cookies = {'Ultima-visita': '10-12-2024'}

dados = {'username': 'dom',
         'password': 'Cesar123'}

infor = None
try:
    requisicao = requests.post('https://putsreq.com/WU4oK4LRKa4nqKJxihX0',
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)
    infor = requisicao.text
except Exception as e:
     print('A Requisiçao deu erro', e)
print(infor)