def calcular_hipotenusa(cateto_a, cateto_b):
  """
  Esta función calcula la hipotenusa de un triángulo rectángulo a partir de los dos catetos.

  Parámetros:
    cateto_a: La longitud del cateto a.
    cateto_b: La longitud del cateto b.

  Retorno:
    La longitud de la hipotenusa.
  """

  if cateto_a <= 0 or cateto_b <= 0:
    raise ValueError("Los catetos deben ser valores positivos.")

  hipotenusa = ((cateto_a ** 2) + (cateto_b ** 2)) ** 0.5

  return hipotenusa

try:
  cateto_a = float(input("Ingrese la longitud del cateto a: "))
  cateto_b = float(input("Ingrese la longitud del cateto b: "))

  hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

  print("La longitud de la hipotenusa es:", hipotenusa)
except ValueError as error:
  print(error)
