import json
import re

with open("dados.json","r",encoding="utf-8")as d:
    dados=json.load(d)
    
#regex para emai
email_regex=r"^[\w\.-]+@[\w\.-]+\.\w+$"

print("validacao emails")

for person in dados:
    email=person["email"]
    
    valido=bool(re.match(email_regex,email))
    
    if valido:
        print(f"o email {email} de {person["nome"]} é valido")
    else:
        print(f"o email {email} de {person["nome"]} é invalido")