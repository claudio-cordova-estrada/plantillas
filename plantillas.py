# ---------------- Función validador de vacío ----------------
# Cuando sea llamado validará si posee algo, sino preguntará de vuelta por este mismo con el codigo del "else"
def validador_vacio(p_algo):
    while True:
        if p_algo:
            print('Todo nice')
            return p_algo
        else:
            print('Campo vacío, intente ingresar algo')
            p_algo = input('Ingrese algo => ')

algo = input("==> ") # Esta linea habrá de estar dentro del codigo principal
validador_vacio(algo) # Forma de llamar a la función

# Comentario: no es necesario ocupar el validador de vacío con un "int", puesto que el solo ingresar un valor vacío lanzará error.
# Se recomienda para el caso anterior tener siempre un "try/except ValueError" para prevenir de que el sistema se caiga

# ---------------- Función validador de lista ----------------
# Dentro de lista con algún tipo de ID (identificador único) numerico

lista = [] # Dejar al principio del codigo como buena practica de declaración de variables
contador = 0 # Dejar al principio del codigo como buena practica de declaración de variables
def validadorListaID(validador):
    if not lista:
        print("Su lista se encuentra vacía, intentelo nuevamente")
    else:
        for i in lista:
            if i[0] == validador:
                for c in i:
                    print(c, end = " ")
                break
            else:
                contador =+ 1
        if contador == len(lista):
            print("Todo mal")

validador = int(input("==> ")) # Esta linea habrá de estar dentro del codigo principal
# En caso de querer validar con un tipo de validador string, sacar "int" del input que le damos a la variable validador que entregamos dentro de la función
validadorListaID(validador) # Forma de llamar a la función

# ---------------- Plantilla de menú ----------------
# Reemplazar los print con el codigo que desee

# Idealmente "opcion = 0" habría de ir al inicio del codigo como una declaración de variable
opcion = 0
# La idea es que mientras la opcion no sea igual al numero de salida (en este caso 5), no saldrá del ciclo
# El "opcion != 5:" puede ser reemplazado con un "True", dejando un break en la opcion de salida
while opcion != 5:
    opcion = int(input("""Por favor ingrese la opción que desee:
1.- primeraOpcion
2.- segundaOpcion
3.- terceraOpcion
4.- cuartaOpcion
5.- Salir

==> """))
    if opcion == 1:
        print("a")
    elif opcion == 2:
        print("b")
    elif opcion == 3:
        print("c")
    elif opcion == 4:
        print("d")
    elif opcion == 5:
        print("Muchas gracias por preferirnos!")

# ---------------- Un while True para validación de inputs numericos ----------------
# Simplemente busca validar que el dato ingresado se corresponda con el tipo numerico

while True:
    try:
        numero = int(input("==> ")) # De querer validar un decimal, cambiar "int" por "float"
        break
    except ValueError:
        print("Tipo de valor ingresado incorrecto, intentelo nuevamente")

# ---------------- Un while True para validación de numeros dentro de rangos ----------------
# Simplemente busca validar que el dato ingresado se corresponda con el tipo numerico

while True:
    try:
        numero = int(input("==> ")) # De querer validar un decimal, cambiar "int" por "float"
    except ValueError:
        print("Tipo de valor ingresado incorrecto, intentelo nuevamente")

    if numero < 1 and numero > 40:
        print("Valor ingresado fuera de rango, intentelo nuevamente") # Caso negativo
    else:
        break # Caso positivo

# 