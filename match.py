# Uso y explicacion de match

print('''
      1. suma
      2. resta
      3. multiplicacion
      4. division
      5. Salir
      ''')

def suma():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese otro numero "))
    print("El resultado de la suma es ", n1+n2)

def resta():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese otro numero "))
    print("El resultado de la resta es ", n1-n2)

def multiplicar():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese otro numero "))
    print("El resultado de la multiplicacion es ", n1*n2)

def dividir():
    try:
       n1=int(input("Ingrese un numero "))
       n2=int(input("Ingrese otro numero "))
       print("El resultado de la division es ", n1/n2)
    except ZeroDivisionError as division:
        print("Se produjo una excepcion: ", division)

    

while True:
    op=int(input("seleccione una opcion "))
    match op:
        case 1:
            print("Suma ")
            suma()
        case 2:
            print("Resta ")
            resta()
        case 3:
            print("Multiplicacion")
            multiplicar()
        case 4:
            print("División ")
            dividir()
        case 5:
            print("Saliendo")
            break
        case _:
            print("opcion no valida")

