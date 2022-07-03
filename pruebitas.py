"""# Comprobar que los validadores unicos se correspondan con los tipos de datos
lista = [[1, "dos", 3.3, None], [2, "aaa", 4.3, True], [3, "jajas", 14.3, False], [4, 12, "asdlfkasjd", 0]]

# Un validador de lista dentro de lista con algún tipo de ID (identificador único) numerico
# En caso de querer validar con un tipo de validador string, sacar "int" del input que le damos a la variable validador que entregamos dentro de la función
lista = []
sumador = 0
xd = 0
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
                sumador =+ 1
        if sumador == len(lista):
            print("Todo mal")

validador = int(input("==> ")) # Esta linea habrá de estar dentro del codigo principal
validadorListaID(validador) # Forma de llamar a la función
"""
"""while True:
    try:
        asdf = int(input("==> "))
    except ValueError:
        print("Todo mal la verda'")"""

asdf = int(input("==> "))