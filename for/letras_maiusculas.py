frase = "boa noite turma do comite"
alfabeto = 'abcdefghijklmnopqrstuvxz'
 
qtd_maiusculas = 0

for letra in frase:
    for letra_alfabeto in alfabeto:
        if letra == letra_alfabeto:
            qtd_maiusculas += 1

print(f'existem {qtd_maiusculas} letras maiusculas')