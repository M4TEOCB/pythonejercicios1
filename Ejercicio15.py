def convertir_numero_a_letras(numero):
  """
  Esta función convierte un número entero a una cadena que lo representa en letras.

  Parámetros:
    numero: El número entero a convertir.

  Retorno:
    Una cadena que representa el número en letras.
  """

  unidades = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
  decenas = ["diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
  especiales = ["once", "doce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]

  if numero < 0 or numero > 99:
    raise ValueError("El número debe estar entre 0 y 99.")

  if numero == 0:
    return "cero"

  if numero in especiales:
    return especiales[numero - 11]

  decena = numero // 10
  unidad = numero % 10

  if unidad == 0:
    return decenas[decena - 1]

  return f"{decenas[decena - 1]} y {unidades[unidad - 1]}"

try:
  # Leer el número del teclado
  numero = int(input("Ingrese un número entre 0 y 99: "))

  # Convertir el número a letras
  letras = convertir_numero_a_letras(numero)

  # Imprimir el número en letras
  print(f"El número {numero} se escribe: {letras}")
except ValueError as error:
  print(error)
