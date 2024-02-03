def es_multiplo(numero, divisor):
  """
  Esta función determina si un número es múltiplo de otro.

  Parámetros:
    numero: El número que se desea evaluar.
    divisor: El divisor.

  Retorno:
    True si el número es múltiplo del divisor, False si no lo es.
  """

  if numero <= 0:
    raise ValueError("El número no puede ser negativo ni cero.")

  resto = numero % divisor
  return resto == 0

numero = int(input("Ingrese un número: "))

if es_multiplo(numero, 2):
  print("El número", numero, "es múltiplo de 2.")

if es_multiplo(numero, 3):
  print("El número", numero, "es múltiplo de 3.")

if not es_multiplo(numero, 2) and not es_multiplo(numero, 3):
  print("El número", numero, "no es múltiplo de 2 ni de 3.")
