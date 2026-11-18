import json
import re

with open("dados.json","r",encoding="utf-8")as d:
    dados=json.load(d)
    
registados_validos=[] 

#padroes regex
email_regex= r"^[\w\.-]+@[\w\.-]+\.\w+$"
nif_regex= r"^[123568]\d{8}$"

for person in dados:
    email=person["email"]
    nif=person["nif"]
    telemovel=person["telemovel"]
    
    validar_email=bool(re.match(email_regex,email))
    validar_nif=bool(re.match(nif_regex,nif))
    only_numbers_tel= re.sub(r"\D","",telemovel)
    validar_telemovel=(len(only_numbers_tel)==9)
    
    if validar_email and validar_nif and validar_telemovel:
        registados_validos.append(person)
        print(f"registo valido: {person["nome"]}")
    else:
        print(f"registo invalido: {person["nome"]}")
        
with open("dados_validos.json","w",encoding="utf-8")as dv:
    json.dump(registados_validos, dv, ensure_ascii=False, indent=4)
    
print("new file criado")