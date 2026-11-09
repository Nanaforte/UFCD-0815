d={'a':1, 'b':2, 'c':3}

d_invertido={}
for key, value in d.items():
    d_invertido[value]=key

print(d_invertido)