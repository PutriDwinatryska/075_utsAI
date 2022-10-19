#nama   :putri dwnatryska a.r.f
#nim    : 21091397075
#kelas  : D4 MI A 

#multi neuron batch input
#insialisasi numpy
import numpy as np 

#inisialisasi variable dengan matriks 6x10 (variabel 10 dengan 6 batch)
inputs  = [[3, 5, 7, 8, 0.10, 2, 4, 6, 9, 1], 
           [1.22, 2.3, 1.32, 2.22, 1.21, 2.2, 1.1, 2.0, 1.16, 2.40],
           [3.12, 4.11, 3.22, 4.55, 3.21, 4.10, 3.32, 4.0, 3.54, 4.18],
           [5.0, 6.0, 5.11, 6.12, 5.23, 6.34, 5.56, 6.54, 5.55, 6.66],
           [7.0, 8.0, 7.98, 8.78, 9.67, 8.12, 9.23, 8.32, 9.16, 8.41],
           [0.23, 0.34, 0.65, 0.78, 0.90, 0.88, 0.19, 0,30, 0.56, 0.63]]

#inisialisasi bobot variable sama dengan input yaitu 10 dan nilai bobot sama dengan neuron yaitu 5
weights = [ [-1.2, 2, 2.3, 1.5, -2.6, 0.20, -0.15, 2.5, 1.7, 1.6],
            [-4.9, 3, 4.3, 3.8, 4, -4.6, 4.3, 3.7, 4.4, 3.5],
            [5.1, -0.5, 6.5, -0.6, 5.5, 6.4, -6.7, 5.9, 6.6, -5.2],
            [7, -8.2, -7.7, 8.1, 8.6, -7.9, -0.7, 8.8, 7.2, 8]
            [9.3, 1.0, -0.10, 9.5, 9, 0.16, -9.8, 0.4, 9.0, 0.19],]

#jumlah bias sama dengan neuron 
bias = [2.3, 3.5, 0.1, 1.5, 2.0]

#penghitungan ouput hasil perkalian input dengan wight dijumlah dengan bias 
layer_output = np.dot(inputs, np.array(weights).T)+bias

#print output
print(layer_output) 