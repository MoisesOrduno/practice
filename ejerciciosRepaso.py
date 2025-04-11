# ========================================
# Ejercicios clásicos de entrevista en Python
# Incluye explicaciones y múltiples soluciones
# ========================================

# ==========================
# Ejercicio 1: Invertir una cadena
# ==========================

# Versión 1: Sin slicing
texto = "entrevista"
reverso = ""
for letra in texto:
    reverso = letra + reverso  # Insertar cada letra al inicio
print("Texto invertido (manual):", reverso)

# Versión 2: Usando slicing
reverso_slicing = texto[::-1]
print("Texto invertido (slicing):", reverso_slicing)

# ==========================
# Ejercicio 2: Contar frecuencia sin shortcuts
# ==========================

valores = ["Mexico", "Mexico", "Chile", "Peru", "Chile", "Mexico"]
frecuencia = {}
for pais in valores:
    if pais not in frecuencia:
        frecuencia[pais] = 1
    else:
        frecuencia[pais] += 1
print("Frecuencia de elementos:")
for pais, veces in frecuencia.items():
    print(f"{pais}: {veces}")

# ==========================
# Ejercicio 3: Palíndromo sin usar slicing
# ==========================

palabra = "murcielago"
es_palindromo = True
largo = len(palabra)
for i in range(largo // 2):
    if palabra[i] != palabra[largo - 1 - i]:
        es_palindromo = False
        break
print(f"¿'{palabra}' es palindromo? {es_palindromo}")

# ==========================
# Ejercicio 4: Suma de dígitos sin convertir a string
# ==========================

numero = 4873
suma = 0
n = numero
while n > 0:
    suma += n % 10
    n //= 10
print(f"Suma de digitos de {numero} es: {suma}")

# ==========================
# Ejercicio 5: Segundo valor más grande
# ==========================

numeros = [5, 8, 3, 1, 9, 9, 7]
mayor = float('-inf')
segundo = float('-inf')

for n in numeros:
    if n > mayor:
        segundo = mayor
        mayor = n
    elif n > segundo and n != mayor:
        segundo = n
print("Segundo valor mas grande:", segundo)

# ==========================
# Ejercicio 6: Contar dígitos de un número
# ==========================

# Versión 1: Convirtiendo a string
numero = 15000
digitos_str = len(str(numero))
print(f"(string) El numero {numero} tiene {digitos_str} dígitos.")

# Versión 2: Sin convertir a string
n = numero
digitos = 0
if n == 0:
    digitos = 1
else:
    while n > 0:
        n //= 10
        digitos += 1
print(f"(matemático) El numero {numero} tiene {digitos} digitos.")

# ==========================
# Ejercicio 7: Encontrar el número más pequeño en una lista (sin min())
# ==========================

numeros = [12, 4, 7, 1, 9, 3]
minimo = float('inf')
for n in numeros:
    if n < minimo:
        minimo = n
print("Número más pequeño:", minimo)

# ==========================
# Ejercicio 8: Verificar si un número es primo
# ==========================

numero = 4
es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

print(f"¿El número {numero} es primo?: {es_primo}")

# ==========================
# Ejercicio 9: Calcular el factorial de un número (iterativo)
# ==========================

numero = 5
factorial = 1

for i in range(2, numero + 1):
    factorial *= i

print(f"Factorial de {numero} es: {factorial}")

# ==========================
# Ejercicio 10: Eliminar duplicados de una lista (sin set())
# ==========================

valores = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = []

for valor in valores:
    if valor not in sin_duplicados:
        sin_duplicados.append(valor)

print("Lista sin duplicados:", sin_duplicados)
