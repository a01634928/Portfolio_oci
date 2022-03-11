import pandas as pd


def daily(data, mean_dataset):
    contador, sumatoria = 0, 0
    for i in range(0, data['Fecha'].size):
        sumatoria = sumatoria + data['Precio marginal local'][i]
        contador += 1
        clave = data['Clave del nodo'][i]
        fecha = data['Fecha'][i]
        if contador == 24:
            daily_mean = sumatoria/24
            mean_dataset.write(str(fecha)+','+str(clave)+','+str(daily_mean)+'\n')
            contador, sumatoria = 0, 0


def start(leercsv_1, leercsv_2, escribir_csv):
    dataset, dataset2 = pd.read_csv(leercsv_1), pd.read_csv(leercsv_2)
    print(dataset.isnull().sum())  # Revisa si hay casillas con valores nulos
    print(dataset2.isnull().sum())  # Revisa si hay casillas con valores nulos
    mean_dataset = open(escribir_csv, 'w', encoding='utf-8')
    mean_dataset.write('Fecha,Clave_del_nodo,pml_mean\n')

    daily(dataset, mean_dataset)
    daily(dataset2, mean_dataset)
    """for i in range(0,dataset['Fecha'].size):
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
            sumatoria=0"""


if __name__ == '__main__':
    for i in range(17, 20):
        for j in range(1, 10):
            leercsv1 = 'pml0' + str(j) + '_1_' + str(i) + '.csv'
            leercsv2 = 'pml0' + str(j) + '_2_' + str(i) + '.csv'
            escribircsv = 'mean0' + str(j) + '_' + str(i) + '.csv'
            start(leercsv1, leercsv2)
        for j in range(10, 13):
            leercsv1 = 'pml' + str(j) + '_1_' + str(i) + '.csv'
            leercsv2 = 'pml' + str(j) + '_2_' + str(i) + '.csv'
            escribircsv = 'mean' + str(j) + '_' + str(i) + '.csv'
            start(leercsv1, leercsv2)