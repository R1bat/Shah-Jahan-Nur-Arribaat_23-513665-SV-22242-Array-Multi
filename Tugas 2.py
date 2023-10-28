# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 21:49:25 2023

@author: Arribaat
"""
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Masukkan elemen matriks [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def display_matrix(matrix):
    for row in matrix:
        print(row)

# Input ukuran matriks
rows = int(input("Masukkan jumlah baris: "))
cols = int(input("Masukkan jumlah kolom: "))

if rows <= 0 or cols <= 0:
    print("Ukuran matriks harus positif.")
else:
    # Input matriks pertama
    print("Masukkan matriks pertama:")
    matrix1 = input_matrix(rows, cols)

    # Input matriks kedua
    print("Masukkan matriks kedua:")
    matrix2 = input_matrix(rows, cols)

    # Menjumlahkan kedua matriks
    result_matrix = add_matrices(matrix1, matrix2)

    # Menampilkan hasilnya
    print("Hasil penjumlahan matriks:")
    display_matrix(result_matrix)

