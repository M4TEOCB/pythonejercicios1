def contar_ocurrencias(caracter, cadena):
  """
  Esta función cuenta el número de ocurrencias de un carácter en una cadena.

  Parámetros:
    caracter: El carácter a buscar.
    cadena: La cadena en la que se busca el carácter.

  Retorno:
    El número de ocurrencias del carácter en la cadena.
  """

  contador = 0
  for letra in cadena:
    if letra == caracter:
      contador += 1

  return contador

try:
  # Leer el carácter y la cadena del teclado
  caracter = input("Ingrese un caracter: ")
  cadena = input("Ingrese una cadena: ")

  # Contar el número de ocurrencias del carácter en la cadena
  numero_ocurrencias = contar_ocurrencias(caracter, cadena)

  # Imprimir el resultado
  print(f"El número de ocurrencias del caracter '{caracter}' en la cadena '{cadena}' es: {numero_ocurrencias}")
except ValueError as error:
  print(error)
