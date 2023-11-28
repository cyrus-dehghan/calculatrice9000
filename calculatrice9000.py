def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Erreur (Division par zéro)")

def calculatrice():
    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))

        operation = input("Entrez le type d'opération (+, -, *, /) : ")

        if operation == "+":
            resultat = addition(nombre1, nombre2)
        elif operation == "-":
            resultat = soustraction(nombre1, nombre2)
        elif operation == "*":
            resultat = multiplication(nombre1, nombre2)
        elif operation == "/":
            resultat = division(nombre1, nombre2)
        else:
            raise ValueError("Erreur (Opération non valide)")

        print(f"{resultat}")

    except ValueError as e:
        print(f"Erreur : {str(e)}")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")

calculatrice()
