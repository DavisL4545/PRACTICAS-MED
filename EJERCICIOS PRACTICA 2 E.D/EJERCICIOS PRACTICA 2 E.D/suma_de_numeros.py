
#EJERCICIO 3 NUMEROS

# Crear la lista de n�meros
numeros = [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8]

# Inicializar listas para n�meros pares e impares
pares = []
impares = []

# Recorrer la lista de n�meros y clasificarlos
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar los resultados
print("Serie:", numeros)
print("Pares:", pares)
print("Impares:", impares)