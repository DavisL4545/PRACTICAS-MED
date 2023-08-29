#1 ejercicio

meses_del_anio = (
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
)

# Solicitar al usuario que ingrese un número entre 1 y 12
numero_mes = int(input("Ingrese un número entre 1 y 12: "))

# Verificar si el número está en el rango válido
if numero_mes >= 1 and numero_mes <= 12:
    # Restamos 1 al número ingresado para obtener el índice correcto en la tupla
    mes_correspondiente = meses_del_anio[numero_mes - 1]
    print(f"El mes correspondiente al número {numero_mes} es {mes_correspondiente}.")
else:
    print("Número fuera de rango. Por favor, ingrese un número entre 1 y 12.")

#2 ejercicio

cadena = input("Ingrese una cadena de texto: ")

# Dividir la cadena en palabras utilizando el espacio como separador
palabras = cadena.split()

# Contar cuántas palabras tiene la cadena
cantidad_palabras = len(palabras)

# Mostrar el resultado
print(f"La cadena ingresada tiene {cantidad_palabras} palabras.")

#3 ejercicio

notas = []

# Solicitar al usuario ingresar las 5 notas
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 10): "))
    
    # Verificar si la nota está en el rango válido
    if nota < 0 or nota > 10:
        print("La nota ingresada está fuera del rango válido (0-10). Inténtelo nuevamente.")
        exit()  # Salir del programa si una nota está fuera de rango
    
    notas.append(nota)  # Agregar la nota a la lista

# Mostrar todas las notas
print("Notas del alumno:")
for i, nota in enumerate(notas, start=1):
    print(f"Nota {i}: {nota}")

# Calcular la nota media
nota_media = sum(notas) / len(notas)
print(f"Nota media: {nota_media:.2f}")

# Encontrar la nota más alta y la nota más baja
nota_maxima = max(notas)
nota_minima = min(notas)
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")