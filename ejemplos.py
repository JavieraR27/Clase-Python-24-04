# FUNDAMENTOS DE PYTHON
# Este archivo contiene ejemplos de las funcionalidades básicas que necesitas 
# para comenzar a programar en Python.

#------------------------------------------------------------------------------
# 1. VARIABLES Y TIPOS DE DATOS
#------------------------------------------------------------------------------

# Las variables son contenedores para almacenar datos
nombre = "Ana"      # String (cadena de texto)
edad = 25           # Integer (número entero)
altura = 1.68       # Float (número decimal)
es_estudiante = True  # Boolean (verdadero/falso)

# Imprimimos los valores y sus tipos
print("VARIABLES Y TIPOS DE DATOS:")
print(f"Nombre: {nombre} - Tipo: {type(nombre)}")
print(f"Edad: {edad} - Tipo: {type(edad)}")
print(f"Altura: {altura} - Tipo: {type(altura)}")
print(f"¿Es estudiante?: {es_estudiante} - Tipo: {type(es_estudiante)}")

#------------------------------------------------------------------------------
# 2. OPERACIONES BÁSICAS
#------------------------------------------------------------------------------

# Operaciones aritméticas
suma = 10 + 5           # 15
resta = 10 - 5          # 5
multiplicacion = 10 * 5  # 50
division = 10 / 5       # 2.0 (siempre devuelve un float)
division_entera = 10 // 3  # 3 (división entera, descarta decimales)
modulo = 10 % 3         # 1 (resto de la división)
potencia = 2 ** 3       # 8 (2 elevado a la 3)

print("\nOPERACIONES BÁSICAS:")
print(f"Suma: 10 + 5 = {suma}")
print(f"Resta: 10 - 5 = {resta}")
print(f"Multiplicación: 10 * 5 = {multiplicacion}")
print(f"División: 10 / 5 = {division}")
print(f"División entera: 10 // 3 = {division_entera}")
print(f"Módulo: 10 % 3 = {modulo}")
print(f"Potencia: 2 ** 3 = {potencia}")

#------------------------------------------------------------------------------
# 3. STRINGS (CADENAS DE TEXTO)
#------------------------------------------------------------------------------

# Operaciones con strings
nombre = "Python"
apellido = "Programming"

# Concatenación
nombre_completo = nombre + " " + apellido  # Python Programming

# Repetición
repetido = nombre * 3  # PythonPythonPython

# Indexación (acceder a caracteres por posición - comienza en 0)
primera_letra = nombre[0]  # P
ultima_letra = nombre[-1]  # n

# Slicing (obtener subcadenas)
primeras_tres = nombre[0:3]  # Pyt
# También se puede escribir como:
primeras_tres_alt = nombre[:3]  # Pyt

# Longitud
longitud = len(nombre)  # 6

# Métodos de string
mayusculas = nombre.upper()  # PYTHON
minusculas = nombre.lower()  # python
titulo = nombre_completo.title()  # Python Programming
reemplazo = nombre.replace("P", "J")  # Jython

print("\nOPERACIONES CON STRINGS:")
print(f"Concatenación: {nombre} + {apellido} = {nombre_completo}")
print(f"Repetición: {nombre} * 3 = {repetido}")
print(f"Primera letra de {nombre}: {primera_letra}")
print(f"Última letra de {nombre}: {ultima_letra}")
print(f"Primeras tres letras de {nombre}: {primeras_tres}")
print(f"Longitud de {nombre}: {longitud}")
print(f"En mayúsculas: {mayusculas}")
print(f"En minúsculas: {minusculas}")
print(f"En formato título: {titulo}")
print(f"Reemplazando P por J: {reemplazo}")

#------------------------------------------------------------------------------
# 4. LISTAS
#------------------------------------------------------------------------------

# Las listas son colecciones ordenadas y modificables
frutas = ["manzana", "banana", "cereza", "durazno"]

# Acceder a elementos
primera_fruta = frutas[0]  # manzana
ultima_fruta = frutas[-1]  # durazno

# Modificar un elemento
frutas[1] = "pera"  # Ahora frutas = ["manzana", "pera", "cereza", "durazno"]

# Agregar elementos
frutas.append("fresa")  # Agrega al final
frutas.insert(2, "uva")  # Inserta en posición específica

# Eliminar elementos
frutas.remove("cereza")  # Elimina por valor
eliminado = frutas.pop(1)  # Elimina por índice y devuelve el valor eliminado

# Otros métodos útiles
cantidad = len(frutas)
frutas.sort()  # Ordena la lista (modifica la original)
frutas_ordenadas = sorted(frutas)  # Devuelve una nueva lista ordenada
frutas.reverse()  # Invierte el orden de la lista

print("\nOPERACIONES CON LISTAS:")
print(f"Lista original: {frutas}")
print(f"Cantidad de elementos: {cantidad}")
print(f"Lista ordenada (nuevo): {frutas_ordenadas}")
print(f"Lista invertida: {frutas}")  # Ya está invertida por el .reverse() anterior

#------------------------------------------------------------------------------
# 5. TUPLAS
#------------------------------------------------------------------------------

# Las tuplas son como listas, pero inmutables (no se pueden modificar después de creadas)
coordenadas = (10, 20)
colores = ("rojo", "verde", "azul")

# Acceder a elementos (igual que en listas)
primer_color = colores[0]  # rojo

# No se puede modificar: colores[0] = "amarillo" daría error

# Desempaquetar tupla
x, y = coordenadas  # x = 10, y = 20
r, g, b = colores   # r = "rojo", g = "verde", b = "azul"

print("\nOPERACIONES CON TUPLAS:")
print(f"Tupla de coordenadas: {coordenadas}")
print(f"Desempaquetado: x = {x}, y = {y}")
print(f"Tupla de colores: {colores}")
print(f"Primer color: {primer_color}")

#------------------------------------------------------------------------------
# 6. DICCIONARIOS
#------------------------------------------------------------------------------

# Los diccionarios almacenan pares clave-valor
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "profesion": "Ingeniero",
    "activo": True
}

# Acceder a valores
nombre_persona = persona["nombre"]  # Carlos
# Alternativa segura (no da error si la clave no existe)
edad_persona = persona.get("edad")  # 30
# Con valor por defecto
telefono = persona.get("telefono", "No disponible")  # "No disponible"

# Modificar valores
persona["edad"] = 31  # Actualiza el valor
persona["ciudad"] = "Madrid"  # Agrega un nuevo par clave-valor

# Eliminar valores
del persona["activo"]  # Elimina el par clave-valor
profesion = persona.pop("profesion")  # Elimina y devuelve el valor

# Métodos útiles
claves = persona.keys()  # Todas las claves
valores = persona.values()  # Todos los valores
items = persona.items()  # Lista de tuplas (clave, valor)

print("\nOPERACIONES CON DICCIONARIOS:")
print(f"Diccionario: {persona}")
print(f"Nombre: {nombre_persona}")
print(f"Teléfono: {telefono}")
print(f"Claves: {list(claves)}")
print(f"Valores: {list(valores)}")

#------------------------------------------------------------------------------
# 7. CONJUNTOS (SETS)
#------------------------------------------------------------------------------

# Los conjuntos son colecciones no ordenadas y sin duplicados
numeros = {1, 2, 3, 4, 5}
letras = {"a", "b", "c", "d"}

# Agregar elementos
numeros.add(6)  # Agrega un elemento
numeros.update([7, 8, 9])  # Agrega varios elementos

# Eliminar elementos
numeros.remove(1)  # Elimina un elemento (da error si no existe)
numeros.discard(10)  # Elimina un elemento (no da error si no existe)

# Operaciones de conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

union = conjunto_a | conjunto_b  # {1, 2, 3, 4, 5, 6}
interseccion = conjunto_a & conjunto_b  # {3, 4}
diferencia = conjunto_a - conjunto_b  # {1, 2}
diferencia_simetrica = conjunto_a ^ conjunto_b  # {1, 2, 5, 6}

print("\nOPERACIONES CON CONJUNTOS:")
print(f"Conjunto de números: {numeros}")
print(f"Conjunto de letras: {letras}")
print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
print(f"Diferencia (A-B): {diferencia}")
print(f"Diferencia simétrica: {diferencia_simetrica}")

#------------------------------------------------------------------------------
# 8. CONDICIONALES (IF-ELIF-ELSE)
#------------------------------------------------------------------------------

edad = 20
tiene_permiso = True

print("\nCONDICIONALES:")

# Ejemplo simple if-else
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Ejemplo con elif (else if)
if edad < 13:
    print("Es un niño")
elif edad < 18:
    print("Es un adolescente")
elif edad < 65:
    print("Es un adulto")
else:
    print("Es un adulto mayor")

# Operadores lógicos: and, or, not
if edad >= 18 and tiene_permiso:
    print("Puede entrar al evento")
else:
    print("No puede entrar al evento")

# Operador ternario (expresión condicional en una línea)
mensaje = "Aprobado" if edad >= 18 else "Rechazado"
print(f"Estado: {mensaje}")

#------------------------------------------------------------------------------
# 9. BUCLES
#------------------------------------------------------------------------------

print("\nBUCLES:")

# Bucle for para iterar sobre una secuencia
print("For con rango:")
for i in range(5):  # Itera de 0 a 4
    print(f"Número: {i}")

# Bucle for con lista
print("\nFor con lista:")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# Bucle for con diccionario
print("\nFor con diccionario:")
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Bucle while
print("\nWhile:")
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa el contador

# Break y continue
print("\nBreak y continue:")
for i in range(10):
    if i == 3:
        continue  # Salta esta iteración
    if i == 7:
        break  # Sale del bucle
    print(f"Valor de i: {i}")

#------------------------------------------------------------------------------
# 10. FUNCIONES
#------------------------------------------------------------------------------

print("\nFUNCIONES:")

# Definición básica
def saludar(nombre):
    """Esta función saluda a la persona indicada"""  # Docstring
    return f"¡Hola, {nombre}!"

# Llamada a la función
saludo = saludar("María")
print(saludo)

# Función con parámetros por defecto
def presentar(nombre, edad=25, ciudad="Desconocida"):
    return f"{nombre} tiene {edad} años y vive en {ciudad}"

print(presentar("Juan"))  # Usa valores por defecto
print(presentar("Pedro", 30))  # Sobreescribe edad
print(presentar("Laura", ciudad="Madrid"))  # Parámetro nombrado

# Función con número variable de argumentos
def sumar(*numeros):
    """Suma todos los números recibidos"""
    total = 0
    for num in numeros:
        total += num
    return total

print(f"Suma: {sumar(1, 2, 3, 4, 5)}")

# Función con número variable de argumentos con nombre
def crear_perfil(**datos):
    """Crea un perfil con los datos proporcionados"""
    return datos

perfil = crear_perfil(nombre="Ana", edad=28, profesion="Diseñadora", ciudad="Valencia")
print(f"Perfil: {perfil}")

#------------------------------------------------------------------------------
# 11. MANEJO DE EXCEPCIONES
#------------------------------------------------------------------------------

print("\nMANEJO DE EXCEPCIONES:")

# Try-except básico
try:
    numero = int(input("Escribe un número (o texto para ver excepción): "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Error: Debes ingresar un número entero")
except ZeroDivisionError:
    print("Error: No puedes dividir por cero")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    # Se ejecuta si no hay excepciones
    print("No hubo errores")
finally:
    # Se ejecuta siempre, haya o no excepciones
    print("Proceso de división finalizado")

#------------------------------------------------------------------------------
# 12. LISTAS POR COMPRENSIÓN
#------------------------------------------------------------------------------

print("\nLISTAS POR COMPRENSIÓN:")

# Forma tradicional de crear una lista
cuadrados_tradicional = []
for x in range(1, 6):
    cuadrados_tradicional.append(x ** 2)
print(f"Cuadrados (tradicional): {cuadrados_tradicional}")

# Con lista por comprensión (más conciso)
cuadrados_comprension = [x ** 2 for x in range(1, 6)]
print(f"Cuadrados (comprensión): {cuadrados_comprension}")

# Con condición
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f"Números pares: {pares}")

# Comprensión de diccionario
cuadrados_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Diccionario de cuadrados: {cuadrados_dict}")

#------------------------------------------------------------------------------
# 13. MÓDULOS Y IMPORTACIÓN
#------------------------------------------------------------------------------

print("\nMÓDULOS Y PAQUETES:")

# Importar un módulo completo
import math
print(f"Pi: {math.pi}")
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")

# Importar funciones específicas
from random import randint, choice
print(f"Número aleatorio entre 1 y 10: {randint(1, 10)}")
print(f"Elemento aleatorio de una lista: {choice(['rojo', 'verde', 'azul'])}")

# Importar con alias
import datetime as dt
ahora = dt.datetime.now()
print(f"Fecha y hora actual: {ahora}")

#------------------------------------------------------------------------------
# 14. TRABAJANDO CON ARCHIVOS
#------------------------------------------------------------------------------

print("\nTRABAJO CON ARCHIVOS:")

# Escribir en un archivo
try:
    with open("ejemplo.txt", "w") as archivo:
        archivo.write("Hola, este es un archivo de ejemplo.\n")
        archivo.write("Python es genial para trabajar con archivos.\n")
    print("Archivo creado correctamente")
    
    # Leer un archivo
    with open("ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
        print(f"Contenido del archivo:\n{contenido}")
    
    # Leer línea por línea
    print("Leyendo línea por línea:")
    with open("ejemplo.txt", "r") as archivo:
        for linea in archivo:
            print(f"  {linea.strip()}")
except Exception as e:
    print(f"Error con archivos: {e}")

#------------------------------------------------------------------------------
# 15. PROGRAMACIÓN ORIENTADA A OBJETOS
#------------------------------------------------------------------------------

print("\nPROGRAMACIÓN ORIENTADA A OBJETOS:")

# Definición de una clase
class Persona:
    # Variable de clase (compartida por todas las instancias)
    especie = "Humano"
    
    # Constructor
    def __init__(self, nombre, edad):
        # Atributos de instancia
        self.nombre = nombre
        self.edad = edad
        self._privado = "Dato privado"  # Convencionalmente privado
    
    # Método de instancia
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
    # Método con argumentos
    def cumplir_years(self, cantidad=1):
        self.edad += cantidad
        return f"¡Feliz cumpleaños #{self.edad}!"
    
    # Método estático (no necesita una instancia)
    @staticmethod
    def es_adulto(edad):
        return edad >= 18
    
    # Método de clase (recibe la clase, no la instancia)
    @classmethod
    def crear_bebe(cls, nombre):
        return cls(nombre, 0)  # Crea una nueva instancia

# Crear instancias de la clase
persona1 = Persona("Carlos", 30)
persona2 = Persona("Ana", 25)

print(f"Persona 1: {persona1.saludar()}")
print(f"Persona 2: {persona2.saludar()}")
print(f"Cumpleaños: {persona1.cumplir_years()}")
print(f"¿Es adulto? {Persona.es_adulto(persona1.edad)}")

# Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Llamada al constructor de la clase padre
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    # Sobrescribir un método
    def saludar(self):
        saludo_base = super().saludar()
        return f"{saludo_base}. Estudio {self.carrera}"

estudiante = Estudiante("Pablo", 22, "Informática")
print(f"Estudiante: {estudiante.saludar()}")

#------------------------------------------------------------------------------
# 16. FUNCIONES LAMBDA (ANÓNIMAS)
#------------------------------------------------------------------------------

print("\nFUNCIONES LAMBDA:")

# Función lambda simple
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")

# Uso con funciones de orden superior
numeros = [1, 5, 3, 9, 2, 6]
numeros_ordenados = sorted(numeros)  # Ordenamiento normal
numeros_ordenados_inv = sorted(numeros, reverse=True)  # Orden inverso

# Uso de lambda con map() para aplicar una función a todos los elementos
cuadrados = list(map(lambda x: x ** 2, numeros))

# Uso de lambda con filter() para filtrar elementos
mayores_que_tres = list(filter(lambda x: x > 3, numeros))

print(f"Lista original: {numeros}")
print(f"Lista ordenada: {numeros_ordenados}")
print(f"Lista ordenada inversa: {numeros_ordenados_inv}")
print(f"Cuadrados con map(): {cuadrados}")
print(f"Números > 3 con filter(): {mayores_que_tres}")

#------------------------------------------------------------------------------
# 17. GENERADORES
#------------------------------------------------------------------------------

print("\nGENERADORES:")

# Función generadora
def cuenta_regresiva(inicio):
    while inicio > 0:
        yield inicio  # Pausa la función y devuelve el valor
        inicio -= 1

# Usar el generador
print("Cuenta regresiva:")
for num in cuenta_regresiva(5):
    print(num)

# Expresión generadora (similar a lista por comprensión pero con paréntesis)
cuadrados_gen = (x ** 2 for x in range(1, 6))
print("Cuadrados con generador:")
for cuadrado in cuadrados_gen:
    print(cuadrado)

#------------------------------------------------------------------------------
# 18. DECORADORES
#------------------------------------------------------------------------------

print("\nDECORADORES:")

# Definir un decorador
def registro(funcion):
    def envolver(*args, **kwargs):
        print(f"Llamando a la función {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"La función {funcion.__name__} ha terminado")
        return resultado
    return envolver

# Aplicar el decorador
@registro
def saludar(nombre):
    print(f"¡Hola, {nombre}!")
    return f"Saludo a {nombre} completado"

# Llamar a la función decorada
resultado = saludar("Elena")
print(f"Resultado: {resultado}")

#------------------------------------------------------------------------------
# 19. COMPRENSIÓN DE ITERABLES
#------------------------------------------------------------------------------

print("\nCOMPRENSIÓN DE ITERABLES:")

# Lista original
numeros = [1, 2, 3, 4, 5]

# Lista por comprensión
cuadrados = [x**2 for x in numeros]
print(f"Cuadrados: {cuadrados}")

# Diccionario por comprensión
cuadrados_dict = {x: x**2 for x in numeros}
print(f"Diccionario de cuadrados: {cuadrados_dict}")

# Conjunto por comprensión
pares_set = {x for x in range(10) if x % 2 == 0}
print(f"Conjunto de números pares: {pares_set}")

# Generador por comprensión
gen = (x**2 for x in numeros)
print("Generador (primeros dos valores):")
print(next(gen))  # 1
print(next(gen))  # 4

#------------------------------------------------------------------------------
# 20. MÓDULOS IMPORTANTES DE LA BIBLIOTECA ESTÁNDAR
#------------------------------------------------------------------------------

print("\nMÓDULOS IMPORTANTES:")

# datetime - Fechas y tiempo
import datetime
ahora = datetime.datetime.now()
print(f"Fecha y hora actual: {ahora}")
print(f"Solo fecha: {ahora.date()}")
print(f"Solo hora: {ahora.time()}")
print(f"Año: {ahora.year}, Mes: {ahora.month}, Día: {ahora.day}")

# random - Generación de números aleatorios
import random
print(f"Número aleatorio entre 1 y 10: {random.randint(1, 10)}")
print(f"Número flotante aleatorio entre 0 y 1: {random.random()}")
lista = ["manzana", "banana", "cereza"]
print(f"Elemento aleatorio de una lista: {random.choice(lista)}")
random.shuffle(lista)  # Mezcla la lista
print(f"Lista mezclada: {lista}")

# sys - Funciones y parámetros específicos del sistema
import sys
print(f"Versión de Python: {sys.version}")
print(f"Plataforma: {sys.platform}")

# os - Funciones del sistema operativo
import os
print(f"Directorio actual: {os.getcwd()}")
print(f"Listado de archivos: {os.listdir('.')}")

# json - Trabajar con datos JSON
import json
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "intereses": ["programación", "música", "deportes"]
}
# Convertir a JSON
json_str = json.dumps(datos, indent=2)
print(f"Datos en formato JSON:\n{json_str}")

# Convertir de JSON a diccionario
nuevos_datos = json.loads(json_str)
print(f"JSON convertido de nuevo a diccionario: {type(nuevos_datos)}")
print(f"Nombre extraído: {nuevos_datos['nombre']}")

print("\n¡Fin del tutorial de Python! 🐍")