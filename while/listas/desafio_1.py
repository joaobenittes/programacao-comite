numeros = []
for i in range(5):
    num = float(input(f'digite o {i+1}° numero: '))
    numeros.append(num)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f'numeros digitados: {numeros}')
print(f'maior numero: {maior}')
print(f'menor numero:  {menor}')
print(f'media numero:  {media:.2f}')