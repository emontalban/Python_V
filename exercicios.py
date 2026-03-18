# Cree un bucle For de Python.

colors = ['white','red','blue', 'green', 'yellow']

for color in colors:
    print(color)


# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(numero_uno, numero_dos, numero_tres):
    resultado = numero_uno + numero_dos + numero_tres
    return resultado

print(suma(8,5,3))

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

resultado = lambda numero_uno, numero_dos, numero_tres: numero_uno + numero_dos + numero_tres

print(resultado(4,5,3))

# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 
# Sugerencia, si es necesario, utilice un bucle for in y el operador in.
# nombre = 'Enrique'
# lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
nombre = 'Enrique'

if nombre in lista_nombre:
    print(f'{nombre} esta en la lista de nombres')
else:
    print(f'{nombre} no esta en la lista de nombres')