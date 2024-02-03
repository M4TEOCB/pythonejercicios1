from datetime import datetime

def verificar_fecha(fecha):
    try:
        # Intentamos convertir la cadena de entrada en una fecha
        fecha = datetime.strptime(fecha, '%Y%m%d')
        return True
    except ValueError:
        # Si ocurre un error, la fecha no es válida
        return False

# Solicitamos al usuario que introduzca una fecha
fecha = input("Introduce una fecha en formato aaaammdd: ")

# Verificamos si la fecha es válida
if verificar_fecha(fecha):
    print("La fecha es válida.")
else:
    print("La fecha no es válida.")
