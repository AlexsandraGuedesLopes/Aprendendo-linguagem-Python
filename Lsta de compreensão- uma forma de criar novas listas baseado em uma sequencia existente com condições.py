numeros = [1, 2, 3, 4, 5]
quadrado = [x**2 for x in numeros if x % 2 == 0]  # Compreensão de lista para calcular o quadrado dos números pares
print(quadrado)  # Saída: [4, 16]