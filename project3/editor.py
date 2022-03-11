import pandas as pd
import numpy as np


dataset = pd.read_csv('mean_nodos17a19.csv')
mean_dataset = open('mean_nodos17a19b.csv','w',encoding='utf-8')
mean_dataset.write('Fecha,05AVO-115,02TVS-115,02MTT-115,05CRN-115,03KIM-115,06MEO-230,02THU-115,06VOT-115,01PHC-230,03EAT-115\n')

for i in range(0,dataset['Fecha'].size):
    casilla = dataset['Fecha'][i]
    fecha = dataset['Fecha'][i]
    nodo1 = dataset['05AVO-115'][i]
    nodo2 = dataset['02TVS-115'][i]
    nodo3 = dataset['02MTT-115'][i]
    nodo4 = dataset['05CRN-115'][i]
    nodo5 = dataset['03KIM-115'][i]
    nodo6 = dataset['06MEO-230'][i]
    nodo7 = dataset['02THU-115'][i]
    nodo8 = dataset['06VOT-115'][i]
    nodo9 = dataset['01PHC-230'][i]
    nodo10 = dataset['03EAT-115'][i]
    if str(casilla[0]) != str(0) and len(casilla) != 10:
        casilla = '0' + str(casilla)
        mean_dataset.write(str(casilla) + ',' + str(nodo1) + ',' + str(nodo2) + ',' + str(nodo3) + ',' + str(nodo4) + ',' + str(nodo5) + ',' + str(nodo6) + ',' + str(nodo7) + ',' + str(nodo8) + ',' + str(nodo9) + ',' + str(nodo10) + '\n')
    else:
        mean_dataset.write(str(casilla) + ',' + str(nodo1) + ',' + str(nodo2) + ',' + str(nodo3) + ',' + str(nodo4) + ',' + str(nodo5) + ',' + str(nodo6) + ',' + str(nodo7) + ',' + str(nodo8) + ',' + str(nodo9) + ',' + str(nodo10) + '\n')
