def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

angka = int(input("Masukkan sebuah bilangan: "))
hasil_cek = cek_ganjil_genap(angka)
print(f"{angka} adalah bilangan {hasil_cek}.")
