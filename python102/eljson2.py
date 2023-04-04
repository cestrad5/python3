import json


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


with open("persona.json", "r") as archivo:
    datos = json.load(archivo)

persona = Persona(**datos)

print(persona.nombre)  # Juan
print(persona.edad)  # 30
