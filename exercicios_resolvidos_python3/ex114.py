"""Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado."""

import requests
url = "http://www.pudim.com.br/"

if requests.get(url).status_code == 200:
    print('Servidor disponível')
else:
    print('Servidor indisponível')
