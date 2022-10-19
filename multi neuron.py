#nama   :putri dwnatryska a.r.f
#nim    : 21091397075
#kelas  : D4 MI A 

#multi neuron dengan numpy
#inisialisasi numpy
import numpy as np

#inisialisasi variable angka harus sma dengan jumlah input yaitu 10
inputs = [1.5, 3, 5, 7, 9, 2, 4, 6, 8, 11]

#inisialisasi bobot variable sama dengan jumlah input dan nilai bobot sama dengan neuron yaitu 5
weights = [ [-1.2, 2, 2.3, 1.5, -2.6, 0.20, -0.15, 2.5, 1.7, 1.6],
            [-4.9, 3, 4.3, 3.8, 4, -4.6, 4.3, 3.7, 4.4, 3.5],
            [5.1, -0.5, 6.5, -0.6, 5.5, 6.4, -6.7, 5.9, 6.6, -5.2],
            [7, -8.2, -7.7, 8.1, 8.6, -7.9, -0.7, 8.8, 7.2, 8]
            [9.3, 1.0, -0.10, 9.5, 9, 0.16, -9.8, 0.4, 9.0, 0.19],]

#inisialisasi bias
bias = [8, 4, 1.7, -2.4, 3.5]

#penghitungan output = hasil kali input dengan weight lalu ditambah bias
output = np.dot(weights*inputs)+bias

#cetak output
print(output)