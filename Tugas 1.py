# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 21:30:53 2023

@author: Arribaat
"""

# Menanyakan ukuran matriks dari pengguna
try:
    n = int(input("Masukkan angka untuk n dari ukuran matriks n x n: "))
except:
    print("Tolong masukkan satu digit angka untuk menentukan n")
    
# Membuat variabel matriks identitas
matriks_identitas = []

# Membuat matriks identitas
for no_baris in range(n): 
    #for loop pertama ini digunakan untuk membuat matriks per baris
    baris = []
    for index_el_satu in range(n):
        #for loop kedua ini digunakan untuk menentukan angka 1 pada setiap barisnya
        if no_baris == index_el_satu:
            baris.append(1)
        else:
            baris.append(0)
    matriks_identitas.append(baris)

# Menampilkan matriks identitas
print("Matriks Identitas dari", n, "x", n, "adalah:")
for baris in matriks_identitas:
    print(baris)



