class Informacion:

    def mi_lista(self):
        lista_Nombreperros=["boby","Dollar","Fany"]
        for x in lista_Nombreperros:
            print(x)

    def mi_tupla(self):
        tupla_Nombregato=("Melgaritis","Emmanuel","Omen")
        for x in tupla_Nombregato:
            print(x)

    def mi_Conjuntos(self):
        conjunto_Mainvalo={"Clove","Cypher","Omen"}
        for x in conjunto_Mainvalo:
            print(x)

    def mi_diccionario(self):
        diccionario_valorant={"split" : "haven","bind" : "lamparas","icebox":"amarillo"}
        for x, key in diccionario_valorant.items():
            print(x, " = ",key )

# Creando el objeto

datos=Informacion()
print("Listado de nombre de perros")
print("\n----Mi lista con nombres de perro---\n")
datos.mi_lista()
print("\n----Mi tupla con nombres de gatos---\n")
datos.mi_tupla()
print("\n----Mi conjunto de nombre de mains en valo---\n")
datos.mi_Conjuntos()
print("\n----Mi diccionario de calls en valo---\n")
datos.mi_diccionario()