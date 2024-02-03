def convertir_segundos(segundos):
  """
  Esta función convierte una cantidad de segundos a horas, minutos y segundos.

  Parámetros:
    segundos: La cantidad de segundos a convertir.

  Retorno:
    Una tupla que contiene las horas, minutos y segundos.
  """

  # Calcular las horas
  horas = segundos // 3600

  # Calcular los minutos restantes
  segundos_restantes = segundos % 3600

  # Calcular los minutos
  minutos = segundos_restantes // 60

  # Calcular los segundos restantes
  segundos_finales = segundos_restantes % 60

  return horas, minutos, segundos_finales

try:
  # Leer la cantidad de segundos del teclado
  segundos = int(input("Ingrese la cantidad de segundos: "))

  # Convertir los segundos a horas, minutos y segundos
  horas, minutos, segundos_finales = convertir_segundos(segundos)

  # Imprimir el resultado
  print(f"El tiempo invertido es: {horas} horas, {minutos} minutos y {segundos_finales} segundos.")
except ValueError as error:
  print(error)

