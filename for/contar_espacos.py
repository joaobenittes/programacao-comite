frase = 'boa noite turma do comite'
qtd_espacos = 0

for letra in frase:
    if letra == ' ':
       qtd_espacos += 1

print(f'existem (qtd_espacos) espacos na frase')