"""
dicionario sao diferentes de listas
    # not lista "[]" e não é acessível por index

#dicionario "()" é acessível por mapping, ou seja key {"nome":"Dario"}

# Key -> Values

"""

dicpess=[{"nome":"Dario","idade":25,"tel":987654321},{"nome":"Maria","idade":15,"tel":912345678}]

dicpess[0]["nome"]

dicpess={"nome":"Dario","idade":25,"tel":987654321}
print(dicpess)

dicpess["cargo"]="obra"   #se nao existir key cria nova entrada
print(dicpess)

dicpess["nome"]="João"    #se existir key faz replace do value
print(dicpess)

dicpess["nom"]=dicpess["nome"]
print(dicpess)

dicpess.pop("nome")    #apaga a key e o value
print(dicpess)


print(dicpess.keys())    #mostra todas as keys
print(dicpess.values())  #mostra todos os values
print(dicpess.items())   #mostra tudo oq está dentro do dicionario

dicpess.update({"nome":"Pedro"})
print(dicpess)

dicpess.update({"Morada":"Rua do Desespero"})
print(dicpess)

dicpess.popitem()    #remove o ultimo elemento
print(dicpess)

for key,value in dicpess.items():
    print(f"chave: {key}, Valor: {value}")    # listar um a um

#funções úteis
print("items ", dicpess.items() )
print("keys ", dicpess.keys() )
print("values ", dicpess.values() )
print("get ", dicpess.get("nome") )
print("acesso value da key ", dicpess["nome"] )
print("get ", dicpess.get("email") )
#print("acesso value da key ",dicpess["email"] )   #usar get para acesso seguro e if  
