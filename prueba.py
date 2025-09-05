frase = 'Aprendiendo a programar en Python'
print(frase)
print(frase[1:5])
print(frase[:5])
print(frase[4:])
print(frase[::-1])

frase1 = input("Favor de teclear una frase")
frase2 = frase1.lower().replace(" ","")
if frase2 == frase2[::-1]:
    print(frase1 + " es un palindromo")
else:
    print(frase1 + " no es un palindromo")
