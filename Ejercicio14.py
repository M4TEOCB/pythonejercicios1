def es_palindromo(cadena):
  """
  Esta función verifica si una cadena es palíndroma.

  Parámetros:
    cadena: La cadena a verificar.

  Retorno:
    True si la cadena es palíndroma, False en caso contrario.
  """

  longitud = len(cadena)

  for i in range(longitud // 2):
    if cadena[i] != cadena[longitud - i - 1]:
      return False

  return True

try:
  # Leer la cadena del teclado
  cadena = input("Ingrese una cadena: ")

  # Verificar si la cadena es palíndroma
  if es_palindromo(cadena):
    print("La cadena es palíndroma.")
  else:
    print("La cadena no es palíndroma.")
except ValueError as error:
  print(error)
