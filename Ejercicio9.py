def obtener_nombre_mes(numero_mes):
    # Diccionario con los nombres de los meses en español
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    # Obtenemos el nombre del mes
    nombre_mes = meses[numero_mes]
    return nombre_mes

# Solicitamos al usuario que introduzca un número de mes
numero_mes = int(input("Introduce un número de mes entre 1 y 12: "))

# Obtenemos e imprimimos el nombre del mes
nombre_mes = obtener_nombre_mes(numero_mes)
print("El mes corresponiente es: ", nombre_mes)
