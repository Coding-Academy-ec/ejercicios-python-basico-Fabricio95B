# 1 Escribe un programa en Python que imprima tu nombre en la pantalla.
def imprimir_nombre():
    print("Bryam")
if __name__ == "__main__":
    imprimir_nombre()

# 2 Escribe un programa que calcule la suma de los números del 1 al 10.
def suma_1_al_10():
    """Function printing python version."""
    suma = sum(range(1, 11))
    return suma
if __name__ == "__main__":
    suma_1_al_10()

# 3 Crea variables para almacenar tu edad, nombre y estatura, e imprímelas en pantalla.
def imprimir_datos_personales(nombre, edad, estatura):
    """Function printing python version."""
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Estatura:", estatura)
if __name__ == "__main__":
    # Se definen las variables con los datos personales
    nombre = "Bryam"
    edad = 29
    estatura = 1.8
    imprimir_datos_personales(nombre, edad, estatura)
# 4 Escribe un programa que determine si un número ingresado por el usuario es par o impar.
def par_o_impar(numero):
    """Function printing python version."""
    if numero % 2 == 0:
       return "par"
    else:
       return "impar"
if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
# 5 Crea una función que calcule el área de un círculo dado su radio.
import math

def area_circulo(radio):
    area = math.pi * radio ** 2
    return area
if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))
    area = area_circulo(radio)
    print(f"El area del ciculo es: {radio} es {area:.2f}.")
# 6 Define una función que reciba dos números como argumentos y devuelva su suma.
def suma(num1, num2):
    return num1 + num2 
if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))  
    num2 = int(input("Ingrese el primer número: "))
    print("La suma es:", suma(num1, num2)) 

# 7 Modifica la función que calcula el área del círculo para que reciba el radio como parámetro.
import math

def area_circulo(radio):
    area = math.pi * radio ** 2  
    return area 

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))  
    print("El área del círculo es:", area_circulo(radio))  

# 8 Diseña un programa que convierta grados Celsius a Fahrenheit y viceversa, utilizando funciones para realizar los cálculos.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32  
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9 

if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(celsius)) 
    fahrenheit = float(input("Ingrese la temperatura en grados fahrenheit: "))
    print("Temperatura en Celsius:", fahrenheit_a_celsius(fahrenheit)) 
