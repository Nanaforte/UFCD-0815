import json

with open("dados.json","r",encoding="utf-8")as d:
    dados=json.load(d)
    
with open("contactos.txt","w",encoding="utf-8")as c:
    for person in dados:
        nome=person["nome"]
        email=person["email"]
        
        c.write(f"Nome: {nome}  |  Email: {email}")
print("file criado com sucesso")