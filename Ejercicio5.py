def obtener_fecha(fecha_str):
  """
  Esta función obtiene el día, mes y año de una fecha en formato aaaammdd.

  Parámetros:
    fecha_str: La fecha en formato aaaammdd.

  Retorno:
    Una tupla con el día, mes y año de la fecha.
  """

  if not fecha_str.isdigit() or len(fecha_str) != 8:
    raise ValueError("La fecha debe ser un número de 8 dígitos.")

  anio = int(fecha_str[:4])
  mes = int(fecha_str[4:6])
  dia = int(fecha_str[6:])

  return dia, mes, anio

try:
  fecha_str = input("Ingrese la fecha (aaaammdd): ")
  dia, mes, anio = obtener_fecha(fecha_str)
  print("Día:", dia)
  print("Mes:", mes)
  print("Año:", anio)
except ValueError as error:
  print(error)
