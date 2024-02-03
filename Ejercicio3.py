PI = 3.1416

def calcular_area(radio):
  """
  Esta función calcula el área de un círculo.

  Parámetros:
    radio: El radio del círculo.

  Retorno:
    El área del círculo.
  """

  if radio <= 0:
    raise ValueError("El radio no puede ser negativo ni cero.")

  area = PI * radio ** 2
  return area

try:
  radio = float(input("Ingrese el radio del círculo: "))
  area = calcular_area(radio)
  print("El área del círculo es:", area)
except ValueError as error:
  print(error)
