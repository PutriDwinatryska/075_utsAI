#instalasi numpy 
import numpy as np 
 
#inisialisasi variable 
inputs = [[2.2, 2.3, 2.4, 2.6, 2.8, 2.9, 2.4, 2.9, 2.7, 2.9], 
        [3.5, 3.7, 3.3, 4.5, 3.6, 4.6, 6.5, 5.9, 4.9, 3.7], 
        [0.4, 4.5, 4.6, 4.8, 4.5, 4.8, 5.7, 5.9, 5.8, 5.7], 
        [7.1, 6.2, 6.1, 7.1, 6.2, 7.2, 6.9, 6.1, 6.3, 6.5], 
        [8.3, 8.4, 8.3, 8.7, 0.8, 0.7, 8.3, 8.2, 8.2, 8.1], 
        [9.8, 9.5, 9.4, 9.8, 9.1, 9.2, 9.3, 6.8, 9.9, 9.8]] 
 
#panjang weights 
weights1 = [[9.8, 9.5, 9.4, 9.8, 9.1, 9.2, 9.3, 6.8, 9.9, 9.8], 
            [7.8, 8.9, 9.1, 2.4, 2.5, 3.5, 3.3, 1.7, 2.5, 6.5], 
            [2.5, 3.5, 3.3, 8.7, 1.4, 2.1, 5.6, 7.7, 1.3, 3.1], 
            [0.4, 4.5, 4.6, 4.8, 4.5, 4.8, 5.7, 5.9, 5.8, 5.7], 
            [3.5, 3.7, 3.3, 4.5, 3.6, 4.6, 6.5, 5.9, 4.9, 3.7]] 
 
#jumlah biases pada layer1 
biases1 = [4.2, 1.4, 5.5, 2.6, 7.9] 
 
#inisialisasi bobot variable 2 
weights2 =  [[3.5, 3.7, 3.3, 4.5, 3.6], 
            [3.2, 1.0, 2.7, 2.8, 1.5], 
            [2.7, 3.4, 5.8, 2.7, 1.4]] 
 
#jumlah biases pada layer2 
biases2= [2.2, 1.1, 7.5] 
 
#oprasi hitung layer 1 
layer1_outputs = np.dot(inputs, np.array(weights1).T) + biases1 
 
#oprasi hitung layer 2 daei hasil perhitungan layer 2 
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2 
 
#print output layer2 
print(layer2_outputs)