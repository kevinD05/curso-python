class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print("hola, mi nombre es",self.nombre, self.apellido)

class Admin(Usuario):
    def supersaludo(self):
        print('hola!, me llamo', self.nombre, 'y soy administrador')

usuario = Usuario('felipe','feliz')

usuario.saludo()
usuario.nombre = 'chanchito'
usuario.saludo()

admin = Admin('super','feliz')
admin.saludo()
admin.supersaludo()

usuario.supersaludo()