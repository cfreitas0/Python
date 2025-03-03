'''import requests
import json

def requisicao(titulo):

    try:
        req = requests.get('https://www.omdbapi.com/?apikey=c0338204&t=' + titulo + '&type=movie' )
        filme = json.loads(req.text)
        return filme
    except:
        print('Erro ao conectar')
        return None

def printar_detalhes(filme):
    print('Titulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('Prémios', filme['Awards'])
    print('Capa:', filme['Poster'])
    print()

sair = False
while not sair  :
    op = input('Escreva o nome de um Filme ou SAIR para fechar: ')

    if op == 'SAIR':
        sair = True
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            print(printar_detalhes(filme))'''


