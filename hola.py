# print("ingrese su nombre")
# nombre=input()
# print("ingrese su edad")

# edad=int(input())
# print("hola" , nombre , "su edad es " , edad)

# if edad>=18:
#     print("Usted es mayor de edad")
# else:
#     print("Usted no es mayor de edad")    

# menor de 12 años es niño
# entre 12 y 17 es adolescente
# mayor de 18, es adulto
# 65 y mas es adulto mayor

# print("ingrese su edad")
# edad=int(input())

# if edad<12:
#    print("usted es niño")
# elif edad>=12 and edad<=17:
#    print("Usted es adolecente")
# elif edad>=18 and edad<=64:
#    print("Usted es adulto")
# else:
#    print("Usted es adulto mayor")

# clave=3344
# pas=int(input("ingrese su clave:"))

# if pas==clave:
#    print("Su clave es correcta")
# else:
#    print("Su clave es incorrecta")


# num=int(input("ingrese un numero"))

# if num % 2==0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

#

# si es azul es de la u
# si es blanco cc
# si es rojo union
# si es verde audax
# si es otro no es color valido

# if color=="azul":
#     print("es de la u")
# elif color=="blanco":
#     print ("es del colo colo")
# elif color=="rojo":
#     print("es de union española")
# elif color=="verde":
#     print("es de audax")
# else:
#     print("no es un color valido")

import random

# numAzar=random.randint(1,30)
# print (numAzar)

# # necesito al menos 20 puntos para abrir la puerta

# if numAzar>=20:
#     print("Puede pasar")
# else:
#     print("Le falta puntaje")

# generar un numero aleatorio entre 1 y 50
# pedir al usuario un numero
# si ingresa un numero mayor decirle "El numero a adivinar es menor"
# Si ingresa un numero menor decirle "El numero a adivinar es mayor"
# Ej numeroAadivinar= 20 
# Si ingresa el 15 debe decir, "El numero a adivinar es mayor"
# Si ingresa el 35 debe decir, "El numero a adivinar es menor"

# Ludo
import time

# meta=30
# turno=1
# j1=0
# j2=0

# while j1<=meta or j2<=meta:
#     if turno % 2==0:
#         print("Turno de j1")
#         time.sleep(1)
#         dado=random.randint(1,6)
#         j1=j1+dado
#         print(f"El j1 sacó {dado}")
#         print(f"Avanza hasta la casilla {j1}")
#     else:
#         print("Turno j2")
#         time.sleep(1)
#         dado=random.randint(1,6)
#         j2=j2+dado
#         print(f"El j2 sacó {dado}")
#         print(f"Anaza hasta la casilla {j2}")
#     turno=turno+1
    
# if j1>j2:
#     print("El ganador es j1")
# else:
#     print("El ganador es j2")

# La florida 20%, la pintana30%, puente alto 25%, san joaquin 15%
# grupo familiar: 1 => 2%, 2 a 4=> 3%, 5 o mas => 4%
# Preguntar al usuario en que comuna vive
# preguntar al usuario con cuantas personas vive
# El arancel actual es de 200.000 por semestre
# basados en las respuestas del usuario y en la informacion dada, calcular su descuento

# ej:
# Ingrese su comuna : La florida
# Ingrese su grupo familiar (numero entero): 4
# El total del descuento es 23%
# El total a pagar es $154.000

descuento=0
arancel=200000

print("""Ingrese su comuna: 
           1. La Florida 20%
           2. La Pintana 30%
           3. Puente Alto 25%
           4. San Joaquin 15%""")
comuna=int(input("Seleccione una comuna"))

if comuna==1:
    descuento=20
elif comuna==2:
    descuento=30
elif comuna==3:
    descuento=25
elif comuna==4:
    descuento=15
else:
    print("Seleccion incorrecta")

grupo=int(input("Ingrese su grupo familiar (numero entero usted incluido)"))

if grupo==1:
    descuento=descuento+2
elif grupo<=4 and grupo>=2:
    descuento=descuento+2
elif grupo>=5:
    descuento=descuento+2
else:
    print("Seleccion incorrecta")

print("El descuento total es ", descuento)
desc=arancel*descuento/100
total=arancel-desc
print ("El total a pagar es", total)













