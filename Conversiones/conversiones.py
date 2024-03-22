convertir_a_fahrenheit = lambda celsius: (celsius * 9/5) + 32

convertir_a_pies = lambda metros: metros * 3.281

convertir_a_libras = lambda kg: kg * 2.205

convertir_a_millas = lambda km: km * 0.621

while True:
    print("--------------------------------------------------------")
    print("|         Programa de conversiones                     |")
    print("|         1.- Celcius a Fahrenheit                     |")
    print("|         2.- Metros a Pies                            |")
    print("|         3.- Kilogramos a libras                      |")
    print("|         4.- Kilometros a millas                      |")
    print("|         0.- Salir                                    |")
    print("--------------------------------------------------------")
    op = int(input("Ingresa la opción que quieres realizar: "))
    if op == 0:
        print("------------------------------------")
        print("| Gracias por venir, vuelve pronto |")
        print("------------------------------------")
        break
    elif op == 1:
        celsius = float(input("Ingresa la temperatura en grados celsius: "))
        print(f"El resultado de {celsius}ºC (Celsius) es: {convertir_a_fahrenheit(celsius)}ºF (Fahrenheit)")
    elif op == 2:
        metros = float(input("Ingresa los metros que quieres convertir: "))
        print(f"{metros}m (metros) son: {convertir_a_pies(metros)} pies de altura")
    elif op == 3:
        kg = float(input("Ingresa los kg que quieres convertir: "))
        print(f"{kg}kg (kilogramos) son: {convertir_a_libras(kg)} lb (libras)")
    elif op == 4:
        km = float(input("Ingresa los kilometros que quieres transformar: "))
        print(f"{km}km (kilometros) son: {round(convertir_a_millas(km), 6)} mi (millas)")
    else:
        print("Ingresa un número valido")