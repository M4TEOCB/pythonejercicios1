def ordenar_numeros(a, b, c):
    """
    Este método toma tres números enteros como argumentos y los ordena de mayor a menor.
    Retorna una tupla con los números ordenados.
    """
    # Usamos la función built-in 'sorted' para ordenar los números en una lista
    numeros_ordenados = sorted([a, b, c], reverse=True)

    # Retornamos los números ordenados como una tupla
    return tuple(numeros_ordenados)

# Solicitamos al usuario que ingrese tres números enteros
num1 = int(input("Por favor, ingrese el primer número: "))
num2 = int(input("Por favor, ingrese el segundo número: "))
num3 = int(input("Por favor, ingrese el tercer número: "))

# Llamamos al método 'ordenar_numeros' con los números ingresados
numeros_ordenados = ordenar_numeros(num1, num2, num3)

# Imprimimos los números ordenados
print("El número mayor es: ", numeros_ordenados[0])
print("El número del medio es: ", numeros_ordenados[1])
print("El número menor es: ", numeros_ordenados[2])

