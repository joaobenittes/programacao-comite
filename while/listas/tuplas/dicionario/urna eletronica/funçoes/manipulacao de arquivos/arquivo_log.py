from datetime import datetime

arquivo_log = 'log.txt'

mensagens = ['iniciando o sistema', 'processamento concluido', 'sistema encerrado' ]

with open(arquivo_log, 'a', encoding='utf-8') as log:
    for msg in mensagens:
        horario = datetime.now().strftime