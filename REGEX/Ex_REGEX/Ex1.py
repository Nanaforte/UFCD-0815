import json

#open file json em read - r
with open("dados.json","r",encoding="utf-8") as d:
    dados=json.load(d)
    print(dados)