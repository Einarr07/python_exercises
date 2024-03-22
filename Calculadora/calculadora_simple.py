def sumar(num1, num2):
    return num1 + num2


def restar(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    try:
        return num1 / num2
    except Exception as e:
        print(f"Error: {e}")


while True:
    print("----------------------------------------------------------")
    print("|      Bienvenido al menú principal                      |")
    print("|      ¿Qué opción quieres realizar?                     |")
    print("|      1.- Sumar                                         |")
    print("|      2.- Restar                                        |")
    print("|      3.- Multiplicar                                   |")
    print("|      4.- Dividir                                       |")
    print("|      0.- SALIR                                         |")
    print("----------------------------------------------------------")
    op = int(input("Ingresa el número de la operación que quieres realizar: "))

    if op == 1:
        print("Ingresa dos números")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"El resultado de la suma es: {round(sumar(num1, num2), 2)}")
    elif op == 2:
        print("Ingresa dos números")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"El resultado de la resta es: {round(restar(num1, num2), 2)}")
    elif op == 3:
        print("Ingresa dos números")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"El resultado la multiplicación es: {round(mult(num1, num2), 2)}")
    elif op == 4:
        print("Ingresa dos números")
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        if num2 == 0:
            print("NO SE PUEDE DIVIDIR PARA 0")
        print(f"El resultado de la división es: {round(div(num1, num2), 2)}")
    elif op == 0:
        print("----------------------------")
        print("|  Gracias, vuelva pronto  |")
        print("----------------------------")
        break
    else:
        print("Ingresa un valor valido")
        print("Intenta de nuevo ")