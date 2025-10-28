opçao = -1
senha_encerrar = 1903
encerrar_votaçao = 1900
candidatos  = []
contagem_votos = {'nulos': 0}

while opçao != senha_encerrar:
    opçao = input('o que deseja fazer? \n' 'opçao 1: cadastrar candidato \n' 'opçao 2: iniciar votaçao \n' 'opçao 3: mostrar votos e vencedor \n' 'opçao 0: sair \n\n' 'opçao -> ')

    if opçao.isdigit():
        opçao = int(opçao)

        if opçao == 1:
            qtd_candidatos = int(input('quantos candidatos'  'deseja cadastrar -> ' ))

            for c in range(1, qtd_candidatos+1):
                candidato = []
                nome_candidato = input(f'nome do candidato {c+1}')
                num_candidato = int(input(f'numero do candidato {c+1}'))

                candidato.append(nome_candidato)
                candidato.append(num_candidato)

                candidatos.append(tuple(candidato))

            print('\n\n')

        elif opçao == 2:
            voto = -1

            while voto != encerrar_votaçao:

                for candidato in candidatos:
                     print(f'candidato {candidato[0]} | numero {candidato[1]}')

                voto = int(input('vote no numero de um candidato -> '))

                cont = 0
                for candidato in candidatos:
                    cont += 1
                    if voto == candidato[1]:
                       if candidato[0] not in contagem_votos:
                        contagem_votos.update({candidato[0]: 1})
                        break
                    else:
                        contagem_votos[candidato[0]] += 1
                        break
                else:
                    if cont == len(candidatos):
                        contagem_votos['nulos'] += 1

        elif opçao == 3:

            contagem_votos['nulos']  -= 1 

            maior = 0
            vencedor = ''
            for key, value in contagem_votos.items():
                if value > maior:
                    maior = value
                    vencedor = key
                print(F'{key} | votos {value}')

            print(f'o vencedor e {vencedor} com {maior} votos')     
            print('\n\n')
    else:
        print('\n\nopçao invalida\n\n')


                    


                
                    
                       


    



        





                  