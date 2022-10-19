#nama   :putri dwnatryska a.r.f
#nim    : 21091397075
#kelas  : D4 MI A 

#single neuron menggunakan numpy 
#modul numpy
import numpy as np

#input angka sesuai jumlah variabel yaitu 10 variabel 
inputs = [2, 5, 7, 9, 11, 3, 4, 6, 8, 0.1]

#banyak bobot harus sama dengan iput yaitu 10 variabel dan nilai bonot harus sama dengan jumlah neuron yaitu 1
weights = [-2.5, 0.4, 0.8, -3.9, 0.5, 0.7, 0.6, 0.8, 0.9, -1.5]

#inisialisasi bias
bias = 9

#rumus hitung output yang akan keluar(hasil kali antar weight dengan iput ditambah bias) 
output = np.dot(weights, inputs) + bias

#cetak ouput
print(output)