#Multiplicar dos numeros sin usar el simbolo de multiplicacion
from asyncore import write
from curses.ascii import US


a = 4
b = 8
resultado = 0

for x in range (a):
    resultado += b

print(resultado)

#ingresar nombre y apellido e imprimirlo al reves

nombre = 'kevin'
apellido = 'diaz'

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])

# escribir una funcion que encuentre el elemento menor de una lista
 
lista =[1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor 
    
# escribir  una funcion que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calculaVolumen(6)
print(resultado)

#escribir una funcion que indique  si el usuario es mayor de edad 

def esMayor(Usuario):
    return usuario.edad > 17 

class Usuario:
    def __init__(self, edad):
        self.edad = edad


usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

#  escribir una funcion que indique si un numero es par o impar

def esPar(n):
    return n % 2 == 0 

resultado = esPar(10)
print(resultado)

# escribir una funcion que indique cuantas vocales tiene una palabra

palabra = "ChAnchito feliz"
vocales = 0
for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

# escribir una aplicacion que recibe una cantidad infinita de numeros hasta
# decir basta , luego que devuelva la suma de los numeros ingresados

lista = []
print('ingrese numeros y para salir escriba "basta"')
while True:
    valor = input('ingrese valor: ')
    if valor == 'basta':
        break 
    else:
        try:
            valor = int(valor) 
            lista.append(valor)
        except:
            print('dato invalido')
            exit()
        
resultado = 0
for x in lista:
    resultado += x

print(resultado)

# escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo

def agregarNombreAArchivo(nombre, apellido):
    c = open ('nombrecompleto.txt','a')
    c = write(nombre + ' '+ apellido + '\n')
    c.close()

agregarNombreAArchivo('Kevin','diaz')