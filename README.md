# 🎉 **Proyecto: Clase Persona en Python**

Este proyecto contiene una implementación simple de una clase en Python llamada `Persona`. La clase está diseñada para almacenar el nombre y la edad de una persona y proporcionar un método para saludar.

## 📜 **Descripción**

El código define una clase `Persona` con los siguientes atributos y métodos:

- **Atributos:**
  - `nombre`: El nombre de la persona.
  - `edad`: La edad de la persona.

- **Métodos:**
  - `saludar()`: Devuelve un saludo en formato de cadena que incluye el nombre y la edad de la persona.

## 🚀 **Uso**

### **Código**

Aquí hay un ejemplo de cómo usar la clase `Persona`:

```python
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
```
**Salida**
Hola me llamo `Juan` y tengo `12` años
Hola me llamo `Pedro` y tengo `18` años

# 🛠️ **Requisitos**
Este proyecto no requiere dependencias adicionales. Solo necesitas tener Python instalado en tu máquina para ejecutar el código.
