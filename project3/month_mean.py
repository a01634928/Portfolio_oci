import pandas as pd

def start():
    dataset = pd.read_csv('mean_nodos17a19b.csv')
    mean_dataset = open('mean_month.csv','w',encoding='utf-8')
    mean_dataset.write('Fecha,05AVO-115,02TVS-115,02MTT-115,05CRN-115,03KIM-115,06MEO-230,02THU-115,06VOT-115,01PHC-230,03EAT-115\n')

    contador = 0
    sumatoria1 = 0
    sumatoria2 = 0
    sumatoria3 = 0
    sumatoria4 = 0
    sumatoria5 = 0
    sumatoria6 = 0
    sumatoria7 = 0
    sumatoria8 = 0
    sumatoria9 = 0
    sumatoria10 = 0
    for k in range(17,20):
        for i in range(1,10):
            for j in range(0, dataset['Fecha'].size):
                month = '0'+ str(i)
                fecha = dataset['Fecha'][j]
                year = fecha[8:10]
                nodo1 = dataset['05AVO-115'][j]
                nodo2 = dataset['02TVS-115'][j]
                nodo3 = dataset['02MTT-115'][j]
                nodo4 = dataset['05CRN-115'][j]
                nodo5 = dataset['03KIM-115'][j]
                nodo6 = dataset['06MEO-230'][j]
                nodo7 = dataset['02THU-115'][j]
                nodo8 = dataset['06VOT-115'][j]
                nodo9 = dataset['01PHC-230'][j]
                nodo10 = dataset['03EAT-115'][j]
                if str(fecha[0:2]) == str(month) and str(k) == str(year):
                    sumatoria1 = sumatoria1 + nodo1
                    sumatoria2 = sumatoria2 + nodo2
                    sumatoria3 = sumatoria3 + nodo3
                    sumatoria4 = sumatoria4 + nodo4
                    sumatoria5 = sumatoria5 + nodo5
                    sumatoria6 = sumatoria6 + nodo6
                    sumatoria7 = sumatoria7 + nodo7
                    sumatoria8 = sumatoria8 + nodo8
                    sumatoria9 = sumatoria9 + nodo9
                    sumatoria10 = sumatoria10 + nodo10
                    contador = contador + 1
                elif contador > 0:
                    month_mean1 = sumatoria1 / contador
                    month_mean2 = sumatoria2 / contador
                    month_mean3 = sumatoria3 / contador
                    month_mean4 = sumatoria4 / contador
                    month_mean5 = sumatoria5 / contador
                    month_mean6 = sumatoria6 / contador
                    month_mean7 = sumatoria7 / contador
                    month_mean8 = sumatoria8 / contador
                    month_mean9 = sumatoria9 / contador
                    month_mean10 = sumatoria10 / contador
                    fecha = dataset['Fecha'][j-1]
                    mean_dataset.write(str(fecha) + ',' + str(month_mean1) + ',' + str(month_mean2) + ',' + str(month_mean3) + ',' + str(
                        month_mean4) + ',' + str(month_mean5) + ',' + str(month_mean6) + ',' + str(month_mean7) + ',' + str(month_mean8) + ',' + str(
                        month_mean9) + ',' + str(month_mean10) + '\n')
                    contador = 0
                    sumatoria1 = 0
                    sumatoria2 = 0
                    sumatoria3 = 0
                    sumatoria4 = 0
                    sumatoria5 = 0
                    sumatoria6 = 0
                    sumatoria7 = 0
                    sumatoria8 = 0
                    sumatoria9 = 0
                    sumatoria10 = 0

        for i in range(10,13):
            for j in range(0, dataset['Fecha'].size):
                month = str(i)
                fecha = dataset['Fecha'][j]
                year = fecha[8:10]
                nodo1 = dataset['05AVO-115'][j]
                nodo2 = dataset['02TVS-115'][j]
                nodo3 = dataset['02MTT-115'][j]
                nodo4 = dataset['05CRN-115'][j]
                nodo5 = dataset['03KIM-115'][j]
                nodo6 = dataset['06MEO-230'][j]
                nodo7 = dataset['02THU-115'][j]
                nodo8 = dataset['06VOT-115'][j]
                nodo9 = dataset['01PHC-230'][j]
                nodo10 = dataset['03EAT-115'][j]
                if str(fecha[0:2]) == str(month) and str(k) == str(year):
                    sumatoria1 = sumatoria1 + nodo1
                    sumatoria2 = sumatoria2 + nodo2
                    sumatoria3 = sumatoria3 + nodo3
                    sumatoria4 = sumatoria4 + nodo4
                    sumatoria5 = sumatoria5 + nodo5
                    sumatoria6 = sumatoria6 + nodo6
                    sumatoria7 = sumatoria7 + nodo7
                    sumatoria8 = sumatoria8 + nodo8
                    sumatoria9 = sumatoria9 + nodo9
                    sumatoria10 = sumatoria10 + nodo10
                    contador = contador + 1
                elif contador > 0:
                    month_mean1 = sumatoria1 / contador
                    month_mean2 = sumatoria2 / contador
                    month_mean3 = sumatoria3 / contador
                    month_mean4 = sumatoria4 / contador
                    month_mean5 = sumatoria5 / contador
                    month_mean6 = sumatoria6 / contador
                    month_mean7 = sumatoria7 / contador
                    month_mean8 = sumatoria8 / contador
                    month_mean9 = sumatoria9 / contador
                    month_mean10 = sumatoria10 / contador
                    fecha = dataset['Fecha'][j - 1]
                    mean_dataset.write(str(fecha) + ',' + str(month_mean1) + ',' + str(month_mean2) + ',' + str(month_mean3) + ',' + str(
                        month_mean4) + ',' + str(month_mean5) + ',' + str(month_mean6) + ',' + str(month_mean7) + ',' + str(month_mean8) + ',' + str(
                        month_mean9) + ',' + str(month_mean10) + '\n')
                    contador = 0
                    sumatoria1 = 0
                    sumatoria2 = 0
                    sumatoria3 = 0
                    sumatoria4 = 0
                    sumatoria5 = 0
                    sumatoria6 = 0
                    sumatoria7 = 0
                    sumatoria8 = 0
                    sumatoria9 = 0
                    sumatoria10 = 0
                if str(fecha[0:2]) == str(12) and str(19) == str(year) and contador == 31:
                    month_mean1 = sumatoria1 / contador
                    month_mean2 = sumatoria2 / contador
                    month_mean3 = sumatoria3 / contador
                    month_mean4 = sumatoria4 / contador
                    month_mean5 = sumatoria5 / contador
                    month_mean6 = sumatoria6 / contador
                    month_mean7 = sumatoria7 / contador
                    month_mean8 = sumatoria8 / contador
                    month_mean9 = sumatoria9 / contador
                    month_mean10 = sumatoria10 / contador
                    mean_dataset.write(str(fecha) + ',' + str(month_mean1) + ',' + str(month_mean2) + ',' + str(
                        month_mean3) + ',' + str(
                        month_mean4) + ',' + str(month_mean5) + ',' + str(month_mean6) + ',' + str(
                        month_mean7) + ',' + str(month_mean8) + ',' + str(
                        month_mean9) + ',' + str(month_mean10) + '\n')



start()
"""             
for i in range(0,dataset['Fecha'].size):
    sumatoria = sumatoria + dataset['Precio marginal local'][i]
    contador += 1
    clave = dataset['Clave del nodo'][i]
    fecha = dataset['Fecha'][i]
    if contador == 24:
        daily_mean = sumatoria/24
        mean_dataset.write(str(fecha)+','+str(clave)+','+str(daily_mean)+'\n')
        contador = 0
        sumatoria=0

for i in range(0,dataset2['Fecha'].size):
    sumatoria = sumatoria + dataset2['Precio marginal local'][i]
    contador += 1
    clave = dataset2['Clave del nodo'][i]
    fecha = dataset2['Fecha'][i]
    if contador == 24:
        daily_mean = sumatoria/24
        mean_dataset.write(str(fecha)+','+str(clave)+','+str(daily_mean)+'\n')
        contador = 0
        sumatoria=0
"""