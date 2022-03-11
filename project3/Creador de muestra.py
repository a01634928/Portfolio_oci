import pandas as pd
import random

def start(leercsv, i):
    dataset = pd.read_csv(leercsv)
    #df = pd.DataFrame(dataset)
    for j in range(0, dataset['Fecha'].size):
        if dataset['Clave_del_nodo'][j] == i:
            clave = dataset['Clave_del_nodo'][j]
            fecha = dataset['Fecha'][j]
            daily_mean = dataset['pml_mean'][j]
            mean_dataset.write(str(fecha) + ',' + str(clave) + ',' + str(daily_mean) + '\n')


random_list = [1663, 745, 555, 1710, 1086, 2025, 698, 2151, 167, 966]
random_nodos = []
mes = 1
nod_dataset = pd.read_csv('mean01_17.csv')
for i in random_list:
    random_nodos.append(nod_dataset['Clave_del_nodo'][i])
print(random_nodos)

#for i in range(10):
    #random_nodos.append(random.randint(1,2254))
#print(random_nodos)

mean_dataset = open('mean_17a19.csv','w',encoding='utf-8')
mean_dataset.write('Fecha,Clave_del_nodo,pml_mean\n')

for i in random_nodos:
    for m in range(17, 20):
        for k in range(1, 10):
            leercsv = 'mean0' + str(k) + '_' + str(m) + '.csv'
            start(leercsv, i)
        leercsv = 'mean10_' + str(m) + '.csv'
        start(leercsv, i)
        leercsv = 'mean11_' + str(m) + '.csv'
        start(leercsv, i)
        leercsv = 'mean12_' + str(m) + '.csv'
        start(leercsv, i)