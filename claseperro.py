print("Clases version 2 el constructor")

class Perro:
    # funcion constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad
    # funciones creadaspor el usuario
    def muerde(self):
        print("Chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"chat perro: {mensaje}")
    def Chatperra(self,mensajep):
        print(f"chat perro: {mensajep}")
    def datos(self):
        print(f"Color: {self.color} edad {self.edad}")
# crear el objeto }
chihuas=Perro("Negro",2)
# llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("Hola canina")
chihuas.Chatperra("Hola boby")
chihuas.chatperro("Quieres ser mi gugguu?")
chihuas.Chatperra("grrrrr.................")