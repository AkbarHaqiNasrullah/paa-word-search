# Tugas PTS - Perencanaan dan Analisis Algoritma
# Nama Kelompok:
# 1. Akbar Haqi Nasrullah
# 2. Celsia Gresia

import random
import string
import time

def generate_word_search(size, words):
    # Menghasilkan kisi(grid) kosong
    grid = [[' ' for x in range(size)] for y in range(size)]

    # Tambahkan kata ke kisi(grid)
    for word in words:
        if len(word) > size:
            raise ValueError(f"Kata '{word}' lebih panjang dari ukuran kisi ({size})")
        placed = False
        while not placed:
            # Pilih arah secara acak
            direction = random.choice(['horizontal', 'vertical', 'diagonal'])

            # Pilih posisi awal secara acak
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)

            # Periksa apakah kata tersebut cocok dengan arah yang dipilih
            if direction == 'horizontal' and col + len(word) <= size:
                fits = all(grid[row][col+i] == ' ' or grid[row][col+i] == word[i] for i in range(len(word)))
            elif direction == 'vertical' and row + len(word) <= size:
                fits = all(grid[row+i][col] == ' ' or grid[row+i][col] == word[i] for i in range(len(word)))
            elif direction == 'diagonal' and row + len(word) <= size and col + len(word) <= size:
                fits = all(grid[row+i][col+i] == ' ' or grid[row+i][col+i] == word[i] for i in range(len(word)))
            else:
                fits = False

            # Tempatkan di kisi(grid) jika kata cocok
            if fits:
                for i in range(len(word)):
                    if direction == 'horizontal':
                        grid[row][col+i] = word[i]
                    elif direction == 'vertical':
                        grid[row+i][col] = word[i]
                    elif direction == 'diagonal':
                        grid[row+i][col+i] = word[i]
                placed = True

    # Isi ruang kisi(grid) yang tersisa dengan huruf acak
    for row in range(size):
        for col in range(size):
            if grid[row][col] == ' ':
                grid[row][col] = random.choice(string.ascii_uppercase)

    # Kembalikan kisi(grid) sebagai string
    return '\n'.join(' '.join(row) for row in grid)


# Data Daftar kata dan Kecepatan waktu proses kata
size = 15
words = ['MAKANAN','KUE','SODA','IKAN','AYAM']
start_time = time.time()
word_search = generate_word_search(size, words)
end_time = time.time()
print(word_search)
print(f"Waktu yang dibutuhkan : {end_time - start_time} detik")
