def capitalizar_frase(frase):
  """
  Esta función capitaliza la primera letra de cada palabra en una frase.

  Parámetros:
    frase: La frase a capitalizar.

  Retorno:
    Una cadena con la frase capitalizada.
  """

  palabras = frase.split()
  palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
  return " ".join(palabras_capitalizadas)

try:
  # Leer la frase del teclado
  frase = input("Ingrese una frase de mínimo 5 palabras: ")

  # Verificar si la frase tiene al menos 5 palabras
  if len(frase.split()) < 5:
    raise ValueError("La frase debe tener al menos 5 palabras.")

  # Capitalizar la frase
  frase_capitalizada = capitalizar_frase(frase)

  # Imprimir la frase capitalizada
  print(f"La frase capitalizada es: {frase_capitalizada}")
except ValueError as error:
  print(error)
