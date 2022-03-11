import pandas as pd

def start():
    dataset = pd.read_csv('Petroleo17a19.csv')
    mean_dataset = open('petroleo_month.csv','w',encoding='utf-8')
    mean_dataset.write('Fecha,Precio\n')

    contador = 0
    sumatoria = 0
    for k in range(17,20):
        for i in range(1,10):
            for j in range(0, dataset['Fecha'].size):
                month = '0'+ str(i)
                fecha = dataset['Fecha'][j]
                year = fecha[8:10]
                nodo = dataset['Mezcla_Mexicana'][j]
                if str(fecha[3:5]) == str(month) and str(k) == str(year):
                    sumatoria = sumatoria + nodo
                    contador = contador + 1
                elif contador > 0:
                    month_mean = sumatoria / contador
                    fecha = dataset['Fecha'][j-1]
                    mean_dataset.write(str(fecha) + ',' + str(month_mean) + '\n')
                    contador = 0
                    sumatoria = 0

        for i in range(10,13):
            for j in range(0, dataset['Fecha'].size):
                month = str(i)
                fecha = dataset['Fecha'][j]
                year = fecha[8:10]
                nodo = dataset['Mezcla_Mexicana'][j]
                if str(fecha[3:5]) == str(month) and str(k) == str(year):
                    sumatoria = sumatoria + nodo
                    contador = contador + 1
                elif contador > 0:
                    month_mean = sumatoria / contador
                    fecha = dataset['Fecha'][j - 1]
                    mean_dataset.write(str(fecha) + ',' + str(month_mean) +  '\n')
                    contador = 0
                    sumatoria = 0
                if str(fecha[3:5]) == str(12) and str(19) == str(year) and contador == 31:
                    month_mean = sumatoria / contador
                    mean_dataset.write(str(fecha) + ',' + str(month_mean) + '\n')



start()