#i = 0

#while i < 5:
 #   i += 1
  #  if i == 3:
   #     continue
    #print(i)

#usuario = ['alex','diaz','kevin','kira']

 #for usuario in usuario:
    #print(usuario)

#for x in range(3, 30, 5):
 #   print(x)
#else:
#   print("hemos terminado")
 

#usuario =['chanchito feliz','felipe','roberto','nicolas']

#edades = [24, 25, 26, 35]

#for usuario in usuario:
   # for edad in edades:
       #3 print(usuario, edades)

def miFuncion():
    print('mi primera funcion!')

#miFuncion

def imprimeDato(*nombre):
    print("el nombre completo es:", nombre[1])

#imprimeDato("chanchito",'feliz', 'lala',''lele)

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

#nombreCompleto(nombre= 'chanchito', apellido = feliz)

def nombrecompleto2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

nombrecompleto2(nombre= 'chanchito', apellido = 'feliz')
