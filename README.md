# Word Search Generator (Perencanaan dan Analisis Algoritma)

Project mata kuliah Perencanaan dan Analisis Algoritma (PAA). Program pembuat teka-teki kata (word search) yang menyembunyikan daftar kata di dalam kisi huruf acak, dalam tiga arah: horizontal, vertikal, dan diagonal.

## Cara Kerja

1. Buat kisi (grid) kosong berukuran N x N.
2. Untuk setiap kata, pilih arah dan posisi awal secara acak.
3. Periksa apakah seluruh kata muat di dalam kisi dan tidak menimpa huruf kata lain (kecuali hurufnya sama). Jika cocok, kata ditempatkan. Jika tidak, ulangi dengan arah dan posisi baru.
4. Isi semua sel yang masih kosong dengan huruf acak.

## Isi Repository

| File | Keterangan |
|---|---|
| `word_search_console.py` | Versi console (kisi 15 x 15). Mencetak kisi dan waktu proses pembuatannya |
| `word_search_gui.py` | Versi GUI PyQt5 (kisi 10 x 10) yang menampilkan kisi dalam bentuk tabel |

## Teknologi

- Python 3
- PyQt5 (hanya untuk versi GUI)

## Cara Menjalankan

Versi console:

```
python word_search_console.py
```

Versi GUI:

```
pip install -r requirements.txt
python word_search_gui.py
```

Setiap dijalankan, posisi kata di dalam kisi akan berbeda karena diacak.

## Anggota Kelompok

- Akbar Haqi Nasrullah
- Celsia Gresia
