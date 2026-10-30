
try:
    with open("data/tidak_ada.txt", "r", encoding="utf-8") as file:
        isi = file.read()
        print(isi)
except FileNotFoundError:
    print("File tidak ditemukan.")
