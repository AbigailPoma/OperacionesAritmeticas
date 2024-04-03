print("Universidad Continental")
def get_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num == 0:
                print("El número 0 no es válido. Por favor, ingrese un número distinto de 0.")
                continue
            return num
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def mcd():
    while True:
        # Solicitar los dos números al usuario
        a = get_input("Ingrese el primer número: ")
        b = get_input("Ingrese el segundo número: ")

        # Calcular el MCD
        while b != 0:
            a, b = b, a % b

        # Imprimir el MCD
        print(f"El máximo común divisor es: {a}")
        break

# Imprimir el nombre de la universidad
print("Universidad Continental")

# Llamar a la función
mcd()

