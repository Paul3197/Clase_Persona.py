class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola me llamo {self.nombre} y tengo {self.edad} años"

# Crear instancias de la clase Persona
Juan = Persona(nombre="Juan", edad=12)
Pedro = Persona(nombre="Pedro", edad=18)

# Imprimir saludos
print(Juan.saludar())
print(Pedro.saludar())

