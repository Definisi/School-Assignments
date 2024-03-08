def hitung_satuan(input_barang):
    """Menghitung jumlah barang dalam satuan lusin, kodi, dan gross."""
    lusin = input_barang / 12
    kodi = input_barang / 20
    gross = input_barang / 144
    return lusin, kodi, gross

def main():
    try:
        inputan = int(input("Masukkan Jumlah Barang: "))

        lusin, kodi, gross = hitung_satuan(inputan)

        print("Lusin : ", round(lusin))
        print("Kodi : ", round(kodi))
        print("Gross : ", round(gross, 2))
    except ValueError:
        print("Masukan tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()
