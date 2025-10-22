candidatos_dados = ((10, 'candidato a', 'partido xpto'), (20, 'candidato b', 'partido zyx'), (30, 'candidato c', 'partido abc'))

votos = {10: 0, 20: 0, 30: 0, 'nulo': 0, 'branco': 0}

def exibir_candidatos():
    print('candidatos')
    for numero, nome, partido in candidatos_dados:
        print(f'numero: {numero} | nome: {nome} | partido: {partido}')
        print('para votar,digite o numero do candidato.')
        print('para votar nulo, digite 99.')
        print('para votar em branco, digite 0.')

def iniciar_votaçao():
    eleitores_votaram = 0
    total_eleitores = 10

    while eleitores_votaram < total_eleitores:
        print(f'\neleitor # {eleitores_votaram + 1}')

        try:
            
            voto = int(input('digite seu voto: '))

            if voto in votos:
                if voto == 0:
                    votos['branco'] += 1
                elif voto == 99:
                    votos['nulo'] += 1
                else:
                    votos[voto] += 1


                print('voto registrado com sucesso!')
                eleitores_votaram += 1
            elif voto == 0:
                votos['branco'] += 1
                print('voto nulo registrado com sucesso!')
                eleitores_votaram += 1

            else:
                print('numero de candidato invalido. tente novamente. ')
                
        except ValueError:
            print('entrada invalida. por favor, digite um numero.')

def exibir_resultados():
     print('\n--- apuraçao dos votos ---')

     total_votos = sum(votos.values())
     print(f'total de votos apurados: {total_votos}')  

     for numero, nome, partido in candidatos_dados:
         print(f'\ncandidato: {nome} ({partido}) - votos: {votos[numero]}')  

     print (f'\nvotos nulos: {votos['nulo']}')
     print(f'votos em branco: {votos['branco']}')
 
     print('\resultado final')

     vencedor = nome
     max_votos = -1

     for numero in candidatos_dados:
         if votos[numero] > max_votos:
            max_votos = votos[numero]
            vencedor = (numero, nome, partido)

         elif votos[numero] == max_votos:
              vencedor = nome

     if vencedor:
         print(f'o vencedor e: {vencedor[1]} ({vencedor[2]}) com {max_votos} votos!')
         
     else:
         print('a eleiçao terminou em empate')  

    
         



            

        