# '''
# Seleccione una opcion
# 1. Agregar productos (nombre del producto y precio)
# 2. Comprar (submenu mostrando productos y precios)
# 3. Crear boleta
# 4. Salir
# '''

# productos=["shampoo","Jabon","Galleta"]
# precios=[3500,2000,4000]
# carrito=[]

# while True:
#     while True:
#         try:
#             print('''
#                   1. Agregar productos (nombre del producto y precio)
#                   2. Comprar (submenu mostrando productos y precios)
#                   3. Crear boleta
#                   4. Salir
#                   ''')
#             op=int(input("Seleccione una opcion"))
#             break
#         except Exception:
#             print("Solo numeros enteros")
#     match op:
#         case 1:
#             prod=input("Ingrese un producto:")
#             productos.append(prod)
#             pre=int(input("Ingrese el precio: "))
#             precios.append(pre)
#         case 2:
#             while True:
#                 try:
#                     for i in range(len(productos)):
#                         print(i+1,productos[i],"$", precios[i])
#                     op=int(input("Seleccione una opcion: "))
#                     break
#                 except Exception:
#                     print("solo numeros enteros")
#             carrito.append(op)
#             print(carrito)
#         case 3:
#             print("-------------0-------------")
#             print("Articulos de aseo Pola")
#             for i in range(len(carrito)):
#                 print
            
#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("Opcion invalida")

# "diccionario"

# frutas={
#     "Manzana": 1200,
#     "melon": 1500,
#     "piña": 2000
# }

# while True:
#     try:
#         print('''
#               1. Ingresar fruta
#               2. Mostrar fruta
#               3. Actualizar precio
#               4. Eliminar fruta
#               5. Salir
#               ''')
#         op=int(input("Seleccione una opción "))
#         match op:
#             case 1:
#                 fruta=input("Ingrese el nombre de la fruta ")
#                 precio=int(input("Ingrese el precio "))
#                 frutas[fruta]=precio
#             case 2:
#                 for key,dato in frutas.items():
#                     print(key, "$", dato)
#             case 3:
#                 for key,dato in frutas.items():
#                     print(key,"$",dato)
#                 fru=input("Seleccione la fruta cuyo precio desea actualizar")
#                 precio=int(input("Ingrese el nuevo precio"))
#                 frutas[fru]=precio
#             case 4:
#                 for key,dato in frutas.items():
#                     print(key,"$", dato)
#                 borrar=int(input("Ingrese la fruta a borrar"))
#                 del frutas[borrar]
#             case 5:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opción no valida")
#     except Exception as e:
#         print("El error es ", e)

"funciones"
# def suma():
#     n1=int(input("Ingrese un numero"))
#     n2=int(input("Ingrese otro numero"))
#     print(n1+n1)
# suma()

# def suma_arg(n1,n2):
#     print(n1+n2)
# suma_arg(9,8)


# def suma_ret():
#     n1=int(input("Ingrese un numero"))
#     n2=int(input("Ingrese otro numero"))
#     return n1+n2
# suma_arg(9,8)
# print(suma_ret())

# def suma_3000(num):
#     return num+3000
# result=suma_3000(4000)
# print(result)

def iva(num):
    return round(num*1.19)
result=iva(2000)
print(result) 
