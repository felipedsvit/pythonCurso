#array=matrix de datos
import numpy as np

mi_lista=[10, "Hola",3.14,True]

#miArray=np.array([10,20,30,40])
#print(miArray[2])

#Slicing: extrae conjuntos de un array usando la notación np.array[inicioFILA:finCOLUNA:paso]
matriz=np.array([[10,20,30],[40,50,60],[70,80,90]])
sub_array1=matriz[2:2] # el : del fin ES obligatorio
sub_array2=matriz[:2] # el : del paso NO es obligatorio
sub_array3=matriz[1:2] # despues del segundo : vene el paso

sub_array4=matriz[0, :]#saca la primera coluna
sub_array5=matriz[:,1]#saca la segunda coluna
sub_array6=matriz[:]#saca la tercera coluna
sub_array7=""



print(f"{sub_array5}\nMatriz Completa: \n{matriz}")
