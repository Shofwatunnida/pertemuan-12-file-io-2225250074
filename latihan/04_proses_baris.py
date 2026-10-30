

with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        if baris == "":
            continue

        nim, nilai = baris.split(",")

        try:
            nilai = float(nilai)
            print("NIM:", nim)
            print("Nilai:", nilai)
        except ValueError:
            print("Nilai untuk NIM", nim, "tidak valid.")
