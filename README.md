 # Pertemuan 12 - File I/O dan Error Handling

## Identitas
- Nama: Shofwatunnida
- NIM: 2225250074
- Kelas: 2A

## Tujuan
Mempelajari cara membaca dan menulis file menggunakan Python, mengolah data dari file, serta menangani error menggunakan try-except.

## Struktur Folder
- `data/`: Menyimpan file input dan output.
- `latihan/`: Berisi enam program latihan File I/O dan Error Handling.
- `tugas/`: Berisi program rekap nilai dari file.

## Format Data
File `data/nilai.txt` menggunakan format `NIM,nilai`.

Contoh:
```text
A001,85
A002,78
A003,92
```

## Cara Menjalankan
Jalankan perintah berikut dari folder utama:

```bash
python tugas/rekap_nilai_file.py
```

## Penanganan Error
- `FileNotFoundError`: Menangani file input yang tidak ditemukan.
- `ValueError`: Menangani nilai yang tidak dapat dikonversi menjadi angka.
- Baris kosong dilewati saat pemrosesan data.

## Pengujian Program

| Pengujian | Hasil yang Diharapkan | Status |
|---|---|---|
| Data nilai valid | Rekap berhasil dihitung | Berhasil |
| Nilai tidak valid | Baris bermasalah dilewati | Berhasil |
| File tidak ditemukan | Pesan error ditampilkan | Perlu diuji |
| Baris kosong | Baris dilewati | Perlu diuji |

## Refleksi
Melalui praktikum ini, saya mempelajari cara membaca, menulis, dan menambahkan data pada file menggunakan Python. Saya juga memahami penggunaan try-except untuk menangani error serta penggunaan fungsi untuk mengolah dan menyimpan hasil rekap nilai.
