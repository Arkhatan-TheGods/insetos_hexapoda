from datetime import datetime, timedelta, time, date

dados = [['Start Time', 'Lunch Start', 'Lunch End', 'End Time', 'user ID'],
         ['08:25:00',    '12:15:00',  '12:50:00', '19:20:00',     '452'],
         ['15:40:00',    '12:00:00',  '12:45:00', '17:55:00',     '485'],
         ['07:45:00',    '11:40:00',  '12:33:00', '17:55:00',     '155'],
         ['18:40:00',    '12:25:00',  '12:48:00', '18:20:00',     '854'],
         ['09:10:00',    '12:13:00',  '13:00:00', '10:25:00',     ' 54'],
         ['08:45:00',    '12:25:00',  '13:20:00', '18:10:00',     '201'],
         ['',            '12:10:00',  '13:00:00', '18:05:00',     '120'],
         ['08:15:00',            '',          '', '18:02:00',     '325'],
         ['10:00:00',    '12:10:00',  '13:05:00',         '',     '424'],
         ['09:15:00',    '12:02:00',          '', '18:25:00',     '211'],
         ['08:25:00',    '13:25:00',  '12:15:00', '18:28:00',     '187']]

dados[0].append('Worked Hours')
dados[0].append('Time in Lunch')

start_time = []
lunch_start = []
lunch_end = []
end_time = []
ID = []
worked_hours = []
time_in_lunch = []
time_in_company = []


for lista in dados:
    # print(lista[0])
    start_time.append(lista[0])
    lunch_start.append(lista[1])
    lunch_end.append(lista[2])
    end_time.append(lista[3])
    ID.append(lista[4])


c = 0
while c < 11:
    c += 1
    if start_time[c] in '':
        print(f'O ID: {ID[c]} não bateu ponto de entrada.')
    if lunch_start[c] in '':
        print(f'O ID: {ID[c]}, não informou ida para almoço')
    elif lunch_end[c] in '':
        print(f'O ID: {ID[c]} não informou volta do almoço')
    elif lunch_start[c] in '' and lunch_end[c] in '':
        print(f'O ID: {ID[c]} não foi almoçar.')
    if end_time[c] in '':
        print(f'O ID: {ID[c]} não bateu ponto de saída.')
    if start_time[c] not in '' and end_time[c] not in '':
        entrada = datetime.strptime(start_time[c], '%H:%M:%S')
        saida = datetime.strptime(end_time[c], '%H:%M:%S')
        calculo = saida - entrada
        if calculo < timedelta(days=0):
            calculo += timedelta(days=1)
        print(f'O ID: {ID[c]} trabalhou ao total: {calculo}.')

        # print(f'ID: {ID[c]}')

        # c = 0
        # for t in zip(start_time[c], end_time[c]):
        #    c += 1
        #    print(f'funcionário de ID: {identity[c]} entrou às {start_time[c]}, foi almoçar {lunch_start[c]}, saiu do almoço {lunch_end[c]} e saiu às {end_time[c]}.')

        # for indice, listas in enumerate(dados[1:]):
        #    print(indice, listas)
        #    for c in listas:
        #        #print(c)
        #         print(f''''o funcionário de ID:{c[4]}')
        #         começou o trabalho às {c[0]},
        #         almoçou às {c[1]},
        #         saiu do almoço às {c[2]},
        #         e foi embora às {c[3]}.''')
