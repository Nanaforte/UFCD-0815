import json
import re

with open("dados.json","r",encoding="utf-8")as d:
    dados=json.load(d)
    
print("validacao nifs")

nif_regex=r"^[123568]\d{8}$"

for person in dados:
    nome=person["nome"]
    nif=person["nif"]
    
    if re.match(nif_regex,nif):
        print(f"Nome: {nome} -- NIF: {nif} -> valido")
    else:
        print(f"Nome: {nome} -- NIF: {nif} -> invalido")