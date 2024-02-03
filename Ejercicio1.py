def cociente(a, b):
  """
  Calcula el cociente de dos números enteros.

  Args:
    a: Primer número entero.
    b: Segundo número entero.

  Returns:
    El cociente de a y b como número flotante.

  Raises:
    ValueError: Si b es igual a 0.
  """

  if b == 0:
    raise ValueError("No se puede dividir por 0")
  else:
    return a / b


if __name__ == "__main__":
  a = int(input("Ingrese el primer número: "))
  b = int(input("Ingrese el segundo número: "))

  try:
    print(f"El cociente de {a} y {b} es {cociente(a, b)}")
  except ValueError:
    print("No se puede dividir por 0")
