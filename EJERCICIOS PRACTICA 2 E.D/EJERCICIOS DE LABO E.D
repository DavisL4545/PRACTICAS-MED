#EJERCICIO 1 SUMA DE NUMEROS ENTEROS DEL 1-100

# Inicializamos la variable para almacenar la suma
suma = 0

# Iteramos desde 1 hasta 100 (incluyendo 100)
for i in range(1, 101):
    suma += i

# Mostramos el resultado
print("La suma de los enteros del 1 al 100 es:", suma)


#EJERCICIO 2 VOCALES

# Solicitamos una frase al usuario
frase = input("Escribe una frase: ")

# Inicializamos contadores para cada vocal
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

# Recorremos la frase y contamos las vocales
for letra in frase:
    if letra.lower() == 'a':
        a_count += 1
    elif letra.lower() == 'e':
        e_count += 1
    elif letra.lower() == 'i':
        i_count += 1
    elif letra.lower() == 'o':
        o_count += 1
    elif letra.lower() == 'u':
        u_count += 1

# Mostramos los resultados
print("a =", a_count)
print("e =", e_count)
print("i =", i_count)
print("o =", o_count)
print("u =", u_count)


#EJERCICIO 3 NUMEROS

# Crear la lista de números
numeros = [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8]

# Inicializar listas para números pares e impares
pares = []
impares = []

# Recorrer la lista de números y clasificarlos
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar los resultados
print("Serie:", numeros)
print("Pares:", pares)
print("Impares:", impares)