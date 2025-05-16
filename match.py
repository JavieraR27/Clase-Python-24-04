# Uso y explicacion de match

# print('''
#       1. suma
#       2. resta
#       3. multiplicacion
#       4. division
#       5. Salir
#       ''')

# def suma():
#     n1=int(input("Ingrese un numero "))
#     n2=int(input("Ingrese otro numero "))
#     print("El resultado de la suma es ", n1+n2)

# def resta():
#     n1=int(input("Ingrese un numero "))
#     n2=int(input("Ingrese otro numero "))
#     print("El resultado de la resta es ", n1-n2)

# def multiplicar():
#     n1=int(input("Ingrese un numero "))
#     n2=int(input("Ingrese otro numero "))
#     print("El resultado de la multiplicacion es ", n1*n2)

# def dividir():
#     try:
#        n1=int(input("Ingrese un numero "))
#        n2=int(input("Ingrese otro numero "))
#        print("El resultado de la division es ", n1/n2)
#     except ZeroDivisionError as division:
#         print("Se produjo una excepcion: ", division)

    

# while True:
#     op=int(input("seleccione una opcion "))
#     match op:
#         case 1:
#             print("Suma ")
#             suma()
#         case 2:
#             print("Resta ")
#             resta()
#         case 3:
#             print("Multiplicacion")
#             multiplicar()
#         case 4:
#             print("División ")
#             dividir()
#         case 5:
#             print("Saliendo")
#             break
#         case _:
#             print("opcion no valida")

#  Nuevo menu recursivo 
#  debe tener 3 programas creados anteriormente
#  Los programas deben estar en una funcion
#  el menu debe llamar a estos programas 
#  y ejecutarlos de manera correcta 
#  debe tener la opcion de salir
#  y la opcion por defecto


# import random
# import time

# print('''
#       1. Numero al azar
#       2. Ludo
#       3. Clave secreta
#       4. Salir
#       ''')

# def numazar():
#         numAzar=random.randint(1,30)
#         print (numAzar)

#         # necesito al menos 20 puntos para abrir la puerta

#         if numAzar>=20:
#             print("Puede pasar")
#         else:
#             print("Le falta puntaje")

# def ludo():
#         meta=30
#         turno=1
#         j1=0
#         j2=0

#         while j1<=meta or j2<=meta:
#             if turno % 2==0:
#                 print("Turno de j1")
#                 time.sleep(1)
#                 dado=random.randint(1,6)
#                 j1=j1+dado
#                 print(f"El j1 sacó {dado}")
#                 print(f"Avanza hasta la casilla {j1}")
#             else:
#                 print("Turno j2")
#                 time.sleep(1)
#                 dado=random.randint(1,6)
#                 j2=j2+dado
#                 print(f"El j2 sacó {dado}")
#                 print(f"Anaza hasta la casilla {j2}")
#             turno=turno+1
            
#         if j1>j2:
#             print("El ganador es j1")
#         else:
#             print("El ganador es j2")

# def clave():
#         clave=3344
#         pas=int(input("ingrese su clave:"))

#         if pas==clave:
#             print("Su clave es correcta")
#         else:
#             print("Su clave es incorrecta")

# while True:
#     op=int(input("seleccione una opcion "))
#     match op:
#         case 1:
#             print("Numero al azar ")
#             numazar()
#         case 2:
#             print("Ludo ")
#             ludo()
#         case 3:
#             print("clave")
#             clave()
#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("Opcion no valida")

#  Crear un menu de carrito con las siguientes opciones
#  1.Ingresar nombre del usuario
#  sera mostrado en la boleta, con un saludo
#  2.comprar, poner productos para poder comprar
#  con su precio correspondiente ej:producto $1000
#  3.Sacar boleta, calcular el precio neto
#  y el precio mas IVA. Mostrar totales
#  bonus, mostrar cant de articulos que lleva
#  4.Salir
#  consideraciones:
#  por lo menos 3 productos
#  no hay limite de compra
#  se puede salir en cualquier momento 
#  los montos de los productos son fijos


print('''
     1. Ingresar nombre: 
     2. Comprar productos
     3. Sacar boleta 
     4. Salir
     ''')
def nombre():
    nom=input("Ingrese su nombre: ")
    print(f"Hola, {nom} bienvenido")

def compra():
    comp=int(input('''Ingrese una opcion
                  1. Leche 1200
                  2. Pan 500
                  3. Queso 2500
                  ''' ))
    while comp:
        if comp==1:
            leche=leche+1200
        elif comp==2:
            pan=pan+500
        elif comp==3:
            queso=queso+2500   
        else:
            print("Terminar compra")
def boleta():
    nombre()
    
   