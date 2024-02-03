def es_par(numero):
  """
  Esta función verifica si un número es par.

  Parámetros:
    numero: El número a verificar.

  Retorno:
    True si el número es par, False en caso contrario.
  """

  return numero % 2 == 0

def es_capicua(numero):
  """
  Esta función verifica si un número es capicúa.

  Parámetros:
    numero: El número a verificar.

  Retorno:
    True si el número es capicúa, False en caso contrario.
  """

  numero_str = str(numero)
  longitud = len(numero_str)

  for i in range(longitud // 2):
    if numero_str[i] != numero_str[longitud - i - 1]:
      return False

  return True

try:
  # Leer el número del teclado
  numero = int(input("Ingrese un número entero positivo: "))

  # Verificar si el número es positivo
  if numero < 0:
    print("El número debe ser positivo.")
    exit()

  # Verificar si el número es par
  if es_par(numero):
    print("El número es par.")
  else:
    print("El número es impar.")

  # Verificar si el número es capicúa
  if es_capicua(numero):
    print("El número es capicúa.")
  else:
    print("El número no es capicúa.")
except ValueError as error:
  print(error)
