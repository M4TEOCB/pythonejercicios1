def mostrar_digitos_inversos(numero):
  """
  Esta función muestra los dígitos de un número en orden inverso.

  Parámetros:
    numero: El número a mostrar en orden inverso.

  Retorno:
    None.
  """

  if numero < 0:
    print("El número debe ser positivo.")
    return

  while numero > 0:
    digito = numero % 10
    print(digito, end="")
    numero //= 10

try:
  # Leer el número del teclado
  numero = int(input("Ingrese un número entero positivo: "))

  # Mostrar los dígitos del número en orden inverso
  mostrar_digitos_inversos(numero)
except ValueError as error:
  print(error)
