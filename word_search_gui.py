import random
import string
import sys
from PyQt5.QtWidgets import (QApplication, QTableWidget, QTableWidgetItem,
                             QHeaderView, QVBoxLayout, QWidget, QAbstractItemView)
from PyQt5.QtCore import Qt

SIZE = 10  # ukuran kisi (SIZE x SIZE)
DIRECTIONS = [(0, 1), (1, 0), (1, 1)]  # horizontal, vertikal, diagonal


def generate_word_search(size, words):
    # Buat kisi(grid) kosong
    grid = [[' ' for _ in range(size)] for _ in range(size)]

    # Tempatkan setiap kata secara acak
    for word in words:
        if len(word) > size:
            raise ValueError(f"Kata '{word}' lebih panjang dari ukuran kisi ({size})")

        for _ in range(1000):  # batas percobaan agar tidak berulang tanpa henti
            d_row, d_col = random.choice(DIRECTIONS)
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)

            # Pastikan seluruh kata masih berada di dalam kisi
            end_row = row + d_row * (len(word) - 1)
            end_col = col + d_col * (len(word) - 1)
            if end_row >= size or end_col >= size:
                continue

            # Pastikan tidak menimpa huruf kata lain (kecuali hurufnya sama)
            if all(grid[row + d_row * i][col + d_col * i] in (' ', word[i])
                   for i in range(len(word))):
                for i in range(len(word)):
                    grid[row + d_row * i][col + d_col * i] = word[i]
                break
        else:
            raise ValueError(f"Kata '{word}' tidak muat di kisi {size}x{size}")

    # Isi sisa kisi dengan huruf acak
    for row in range(size):
        for col in range(size):
            if grid[row][col] == ' ':
                grid[row][col] = random.choice(string.ascii_uppercase)

    return grid


class WordSearch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Search")
        self.resize(520, 520)

        # Daftar kata yang disembunyikan di dalam kisi
        self.words = ['TARAKAN', 'JAKARTA', 'ACEH', 'ASD', 'WIDGET', 'TABLE', 'ITEM']
        grid = generate_word_search(SIZE, self.words)

        # Siapkan tabel
        self.table = QTableWidget()
        self.table.setColumnCount(SIZE)
        self.table.setRowCount(SIZE)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Isi tabel dengan huruf dari kisi
        for row in range(SIZE):
            for col in range(SIZE):
                item = QTableWidgetItem(grid[row][col])
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)

        # Tampilkan tabel
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WordSearch()
    window.show()
    sys.exit(app.exec_())
