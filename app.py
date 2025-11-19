import utils

PASSWORD = "123456"  # Hardcoded password (vulnerability)

def main():
    print("=== App Insegura ===")
    user_pass = input("Ingresa la contraseña: ")

    if user_pass == PASSWORD:
        print("Acceso permitido.")
    else:
        print("Acceso denegado.")

    expresion = input("Ingresa una expresión matemática: ")
    print("Resultado:", eval(expresion))  # Vulnerabilidad crítica

    utils.funcion_mala(5)

if __name__ == "__main__":
    main()

