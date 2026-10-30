def baca_dan_validasi_nilai(nama_file):
	data_nilai = []

	try:
		with open(nama_file, "r", encoding="utf-8") as file:
			for baris in file:
				baris = baris.strip()

				if baris == "":
					continue

				try:
					nim, nilai = baris.split(",")
					nilai = float(nilai)
					data_nilai.append((nim, nilai))
				except ValueError:
					print("Data tidak valid:", baris)

	except FileNotFoundError:
		print("File nilai tidak ditemukan.")
		return None

	return data_nilai


def tulis_rekap(nama_file, data_nilai):
	if not data_nilai:
		print("Tidak ada data nilai yang valid.")
		return

	jumlah = len(data_nilai)
	total = sum(nilai for nim, nilai in data_nilai)
	rata_rata = total / jumlah
	nilai_min = min(nilai for nim, nilai in data_nilai)
	nilai_maks = max(nilai for nim, nilai in data_nilai)
	jumlah_lulus = sum(1 for nim, nilai in data_nilai if nilai >= 60)

	with open(nama_file, "w", encoding="utf-8") as file:
		file.write("HASIL REKAP NILAI\n")
		file.write("=================\n")
		file.write(f"Jumlah data valid: {jumlah}\n")
		file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
		file.write(f"Nilai minimum: {nilai_min:.2f}\n")
		file.write(f"Nilai maksimum: {nilai_maks:.2f}\n")
		file.write(f"Jumlah nilai lulus: {jumlah_lulus}\n")

	print("Rekap nilai berhasil disimpan.")
	print("Jumlah data valid:", jumlah)
	print(f"Rata-rata nilai: {rata_rata:.2f}")
	print(f"Nilai minimum: {nilai_min:.2f}")
	print(f"Nilai maksimum: {nilai_maks:.2f}")
	print("Jumlah nilai lulus:", jumlah_lulus)


data_nilai = baca_dan_validasi_nilai("data/nilai.txt")

if data_nilai is not None:
	tulis_rekap("data/hasil_rekap.txt", data_nilai)
