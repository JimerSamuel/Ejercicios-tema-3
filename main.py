def sumar_tres_numeros(num1, num2, num3):
    return num1 + num2 + num3

if __name__ == "__main__":
    resultado = sumar_tres_numeros(1, 2, 3)
    print(resultado) # Imprimirá "6"


class Coche:
    def __init__(self):
        self.num_puertas = 0
    
    def agregar_puerta(self):
        self.num_puertas += 1

if __name__ == "__main__":
    miCoche = Coche()
    print("El número de puertas original es:", miCoche.num_puertas) # Imprimirá "El número de puertas original es: 0"
    miCoche.agregar_puerta()
    print("El número de puertas después de agregar una es:", miCoche.num_puertas) # Imprimirá "El número de puertas después de agregar una es: 1"
