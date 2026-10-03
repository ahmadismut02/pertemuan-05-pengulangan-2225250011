# Pertemuan 05 Perulangan Python

Nama: Ahmad Ismut Thoriequddin
NIM: 2225250011
Kelas: 3A

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Meminta input suku pertama (a) dan beda (d) dari pengguna sebagai tipe data float.
2. Meminta input banyak suku (n) sebagai integer.
3. Melakukan validasi berulang menggunakan while n <= 0: jika nilai n kurang dari atau sama dengan nol, tampilkan pesan error dan minta pengguna memasukkan nilai n kembali sampai didapatkan bilangan bulat positif.
4. Menginisialisasi variabel total = 0.0 sebelum perulangan untuk menampung hasil akumulasi.
5. Melakukan perulangan for i in range(n) sebanyak n kali:
   - Menghitung nilai suku ke-i menggunakan rumus suku = a + (i * d).
   - Menambahkan nilai suku ke dalam variabel total.
   - Menampilkan urutan suku beserta nilainya.
6. Setelah perulangan selesai, menampilkan hasil akumulasi seluruh suku (total) dengan format 2 angka di belakang koma.

## Hasil Pengujian

| Input (a, d, n) | Keluaran yang Diharapkan | Keluaran Aktual | Status |
| :--- | :--- | :--- | :--- |
| a=2, d=3, n=5 | Suku: 2.0, 5.0, 8.0, 11.0, 14.0<br>Jumlah: 40.00 | Suku: 2.0, 5.0, 8.0, 11.0, 14.0<br>Jumlah: 40.00 | Sesuai |
| a=10, d=-2, n=4 | Suku: 10.0, 8.0, 6.0, 4.0<br>Jumlah: 28.00 | Suku: 10.0, 8.0, 6.0, 4.0<br>Jumlah: 28.00 | Sesuai |
| a=1.5, d=0.5, n=3 | Suku: 1.5, 2.0, 2.5<br>Jumlah: 6.00 | Suku: 1.5, 2.0, 2.5<br>Jumlah: 6.00 | Sesuai |
| a=2, d=3, n=-3 lalu 5 | Menolak input -3, meminta input ulang n sampai positif, lalu menghasilkan jumlah 40.00 | Menolak input -3, meminta input ulang n sampai positif, lalu menghasilkan jumlah 40.00 | Sesuai |

## Refleksi
Kesalahan yang ditemui adalah kebingungan dalam memilih penggunaan perondisian `if` dan perulangan `while` saat melakukan validasi input `n`.

* Kesalahan: Menggunakan `if n <= 0` untuk validasi input. Hal ini menyebabkan program hanya memeriksa dan meminta input ulang sebanyak 1 kali. Jika pengguna memasukkan nilai salah dua kali berturut-turut, input salah yang kedua akan tetap lolos dan merusak perhitungan program.
* Cara Memperbaiki: Bertanya kepada AI

---

### Jawaban Refleksi Teknis

1. Bagian yang menentukan jumlah iterasi:
   Variabel n yang dimasukkan pengguna dan digunakan dalam batas fungsi perulangan range(n).

2. Mengapa total harus diinisialisasi sebelum loop:
   Agar variabel total memiliki nilai awal (0.0) untuk menampung hasil penjumlahan suku pada setiap putaran/iterasi loop.

3. Akibat jika total = 0 ditempatkan di dalam loop:
   Nilai total akan selalu tereset kembali menjadi 0 pada setiap awal iterasi, sehingga variabel total hanya menyimpan nilai suku terakhir dan gagal menghitung akumulasi seluruh suku.

4. Mengapa validasi n lebih sesuai menggunakan while:
   Karena jumlah kesalahan input dari pengguna tidak bisa diprediksi. while akan terus mengulang instruksi input sampai pengguna memasukkan nilai n > 0 yang memenuhi syarat.

5. Membuktikan bahwa loop berhenti tepat:
   Dapat dibuktikan dari batasan range(n) di mana perulangan berjalan untuk indeks i = 0 sampai i = n - 1. Jumlah baris output suku yang tercetak dipastikan pas/tepat sebanyak n kali.