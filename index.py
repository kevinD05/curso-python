#esto es un comentario
if 4 < 5:
    print("4 es menor que 5")

if 3 > 5:
    print('esto no se va a imprimir') 

x = 5
y = 'chanchito feliz'
print(x, y)

correo = 'kd186521@gmail.com'

print(correo)
 
#mutiples variables 
#a, b , c = 'lili','lala', 'lolo'

#print(a , b, c)

#concatenacion

inicio = 'Hola'
final = 'Mundo'
print(inicio + final)

#strings
palabra = 'hola' #esto es un strings
oracion = "hola mundo" #esto es un strings

#entero = 20 #integer
#conDecimal = 20.4 #float
#complejo = 5j #complejo

#print(entero, conDecimal, complejo)

#listas
lista = ['hola', 'mundo', 'kevin']
lista2 = lista.copy()
lista.append("triste")
#lista.clear()
#print(lista,lista2.count(2))
#print(len(lista), len(lista2))

largolista = len(lista)
largolista2 = len(lista2)

#print(largolista, largolista2)
#print(lista[1])

#lista.pop() #este es el ultimo elemento de la lista    
#lista.pop()
#lista.remove('hola') #este elimina un elemento por su valor
lista.reverse()
lista.sort()

tupla = ('hola','mundo','somos', 'tupla')
listadetupla = list(tupla)
listadetupla.append('chanchito')
print(listadetupla)

rango = range(6)
#print(rango)

diccionario = {
    "nombre": "loki",
    "raza": "pitbull",
    "edad": 1
}
#print(diccionario)
#print(diccionario['nombre'])
#print(diccionario['raza'])
#print(diccionario.get('nombre))
diccionario['nombre'] = 'zeus'

print(len(diccionario))

diccionario['ladra'] = 'si'

print(diccionario)
#print(diccionario.pop('ladra'))
#diccionario.popitem()
diccionario.clear()
print(diccionario)

kira = {
    "nombre": "kira",
    "Edad" : 1
}

luna = {
    "nombre": "luna",
    "edad": 2

}

Gatos = {
    'Kira':kira,
    'luna':luna
    }

print(Gatos)

perritos =dict(nombre= 'zeus', edad= 5)
print(perritos)