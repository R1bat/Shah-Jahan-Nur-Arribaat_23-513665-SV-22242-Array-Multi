# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 21:55:06 2023

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

def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

def display_matrix(matrix):
    for row in matrix:
        print(row)

# Input ukuran matriks
rows = int(input("Masukkan jumlah baris: "))
cols = int(input("Masukkan jumlah kolom: "))

if rows <= 0 or cols <= 0:
    print("Ukuran matriks harus positif.")
else:
    # Input matriks
    print("Masukkan matriks:")
    matrix = input_matrix(rows, cols)

    # Menghitung transpose matriks
    transposed_matrix = transpose_matrix(matrix)

    # Menampilkan hasil transpose
    print("Hasil transpose matriks:")
    display_matrix(transposed_matrix)

