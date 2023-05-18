# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Persona:
    def __init__(self, n=None,a=None,e=None):
        self._nombre = n
        self._apellido =a 
        self._edad = e
        
    def __str__(self):
        return f"Persona(nombre={self._nombre}, apellido={self._apellido}, edad={self._edad})"

    @property
    def atributo(self):
        return self._atributo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    @atributo.setter
    def nombre(self, nom):
        self._nombre = nom
        
    @atributo.setter
    def apellido(self, ape):
        self._apellido = ape

    @atributo.setter
    def edad(self, e):
        self._edad = e

# clase 02
class Perro:
    def __init__(self, n=None,e=None):
        self._nombre = n
        self._edad = e
        
    def __str__(self):
        return f"Perro(nombre={self._nombre}, edad={self._edad})"

    @property
    def atributo(self):
        return self._atributo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    

    @atributo.setter
    def nombreP(self, nom):
        self._nombre = nom

    @atributo.setter
    def edadP(self, e):
        self._edad = e
