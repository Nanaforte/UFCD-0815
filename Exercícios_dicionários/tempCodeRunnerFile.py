frase=input("escreva uma frase: ")

words=frase.split()   #split divide a frase em palavras
frequencia_words={}

for word in words:
    frequencia_words[word]=frequencia_words.get(word,0)+1
    
print(frequencia_words)