numeros = (1, 3, 4, 6, 7, 8, 9, 10, 15, 21)
pares = tuple(num for num in numeros if num % 2 == 0)
print('numeros pares:', pares)