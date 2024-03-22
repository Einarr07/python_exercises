# Importación de modulos
import random
import string


# Creando una función para generar contraseñas
def generador_de_contraseña(longitud):
    # Utilizamos la importación string para optener distintos caracteres
    # string.ascii_letters: Es una cadena que contiene todas las letras ASCII, tanto mayúsculas como minúsculas.
    # string.digits: Es una cadena que contiene los dígitos del 0 al 9.
    # string.punctuation: Es una cadena que contiene una serie de caracteres de puntuación.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    """
    random.choice(): Esta función toma una secuencia (como una lista o una cadena) y devuelve un elemento aleatorio 
    de esa secuencia.
    --------------------------------------------------------------------------------------------------------------------
    ''.join(): Es un método de cadena que une los elementos de una secuencia (en este caso, una lista de caracteres)
     en una sola cadena. El primer argumento ('' en este caso) es el separador que se utiliza entre los elementos de la
      secuencia, pero como no queremos ningún separador, usamos una cadena vacía.
    """
    contraseña = "".join(random.choice(caracteres) for i in range(longitud))
    return contraseña


longitud = int(input("Ingresa la longitud que tendra tu núeva contraseña: "))
print(f"Tu núeva contraseña es: {generador_de_contraseña(longitud)}")



