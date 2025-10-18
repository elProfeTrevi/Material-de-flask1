def saludo(nombre):
	# codigo de la función
    print("Hola, " + nombre+ ". ¡Bienvenido!")

def saludo2(nombre="Anonimo"):
	# codigo de la función
    print("Hola, " + nombre+ ". ¡Bienvenido!")
    
def suma(a, b):
	return a + b
 
def suma2(*args):
    s1 = 0
    for x in args:
        s1+=x
    return s1

def min1(*args):
    s1 = 0
    for x in args:
        s1+=x
    return s1

def max1(*args):
    s1 = 0
    for x in args:
        s1+=x
    return s1

print(suma(45, 20)) # parámentros posicionales
print(suma2(45, 20, 12, 12, 12, 12, 12))

