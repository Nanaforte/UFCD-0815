word=input("introduza uma palavra: ")

#dic
contagem={}

for l in word:
    contagem[l]=contagem.get(l,0)+1
    
print(contagem)