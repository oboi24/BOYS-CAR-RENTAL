# Capstone Project (M1)
# Oktandre Boy Parulian (JCDS-0408-BDG)

# Data mobil yang tersedia
car_available = [
    {'id': 1, 'brand': 'Toyota', 'Model': 'Innova', 'Tahun': '2023', 'Warna': 'Hitam', 'harga': 575000},
    {'id': 2, 'brand': 'Toyota', 'Model': 'Fortuner', 'Tahun': '2022', 'Warna': 'Silver', 'harga': 450000},
    {'id': 3, 'brand': 'Mitsubishi', 'Model': 'Pajero', 'Tahun': '2019', 'Warna': 'Hitam', 'harga': 500000},
    {'id': 4, 'brand': 'Mitsubishi', 'Model': 'Xpander', 'Tahun': '2021', 'Warna': 'Merah', 'harga': 350000},
    {'id': 5, 'brand': 'Honda', 'Model': 'Hrv', 'Tahun': '2023', 'Warna': 'Putih', 'harga': 400000},
    {'id': 6, 'brand': 'Honda', 'Model': 'Brio', 'Tahun': '2020', 'Warna': 'Kuning', 'harga': 250000},
    {'id': 7, 'brand': 'Nissan', 'Model': 'Livina', 'Tahun': '2018', 'Warna': 'Hitam', 'harga': 300000},
    {'id': 8, 'brand': 'Nissan', 'Model': 'Terra', 'Tahun': '2023', 'Warna': 'Merah', 'harga': 400000},
    {'id': 9, 'brand': 'Hyundai', 'Model': 'Ioniq', 'Tahun': '2023', 'Warna': 'Silver', 'harga': 550000},
    {'id': 10, 'brand': 'Hyundai', 'Model': 'Creta', 'Tahun': '2022', 'Warna': 'Putih', 'harga': 450000},
]

# READ

# Fungsi untuk menampilkan semua mobilnya
def tampilkan_mobil():
    if car_available:
        print("{:<10} {:<15} {:<10} {:<10} {:<10}".format('id','Brand', 'Model', 'Tahun', 'Warna', 'Harga'))
        print("-" * 55)
        for mobil in car_available:
            print("{:<10} {:<15} {:<10} {:<10} {:<10}".format(mobil['id'],mobil['brand'], mobil['Model'], mobil['Tahun'], mobil['Warna'], mobil['harga']))
    else:
        print("Belum ada mobil yang tersedia.")

# CREATE

# Fungsi untuk menambahkan mobil baru (brand, model, tahun, warna, harga)
def tambah_mobil():
    id = input("Masukkan Id mobil baru : ")

    # Memeriksa apakah ID mobil sudah ada
    for mobil in car_available:
        if mobil['id'] == id:
            print(f"Mobil dengan ID {id} sudah ada dalam daftar. Tidak bisa menambahkan mobil dengan ID yang sama.")
            return

    brand = input("Masukkan brand mobil baru: ")
    model = input("Masukkan model mobil baru: ")
    tahun = input("Masukkan tahun mobil baru: ")
    warna = input("Masukkan warna mobil baru: ")
    while True:
        try:
            harga = int(input("Masukkan harga sewa mobil baru: "))
            break
        except ValueError:
            print("Input harga harus berupa angka.")

    mobil_baru = {
        'id' : id,
        'brand': brand,
        'Model': model,
        'Tahun': tahun,
        'Warna': warna,
        'harga': harga
    }

    car_available.append(mobil_baru)
    print(f"Mobil {brand} {model} tahun {tahun} dengan warna {warna} dan harga {harga} telah ditambahkan.")


# -- model
def cari_mobil_berdasarkan_model(model):
    mobil_ditemukan = False
    for mobil in car_available:
        if mobil['Model'].lower() == model.lower():
            if not mobil_ditemukan:
                mobil_ditemukan = True
                print("Mobil dengan model", model, "yang tersedia:")
            print("{:<10} {:<15} {:<10} {:<10} {:<10}".format(mobil['id'],mobil['brand'], mobil['Model'], mobil['Tahun'], mobil['Warna'], mobil['harga']))
    if not mobil_ditemukan:
        print("Mobil dengan model", model, "tidak ditemukan.")

# -- tahun
def cari_mobil_berdasarkan_tahun(tahun):
    mobil_ditemukan = False
    for mobil in car_available:
        if mobil['Tahun'] == tahun:
            if not mobil_ditemukan:
                mobil_ditemukan = True
                print("Mobil dengan tahun", tahun, "yang tersedia:")
            print("{:<10} {:<15} {:<10} {:<10} {:<10}".format(mobil['brand'], mobil['Model'], mobil['Tahun'], mobil['Warna'], mobil['harga']))
    if not mobil_ditemukan:
        print("Mobil dengan tahun", tahun, "tidak ditemukan.")

# -- warna
def cari_mobil_berdasarkan_warna(warna):
    mobil_ditemukan = False
    for mobil in car_available:
        if mobil['Warna'].lower() == warna.lower():
            if not mobil_ditemukan:
                mobil_ditemukan = True
                print("Mobil dengan warna", warna, "yang tersedia:")
            print("{:<10} {:<15} {:<10} {:<10} {:<10}".format(mobil['id'],mobil['brand'], mobil['Model'], mobil['Tahun'], mobil['Warna'], mobil['harga']))
    if not mobil_ditemukan:
        print("Mobil dengan warna", warna, "tidak ditemukan.")

# -- harga
def cari_mobil_berdasarkan_harga(harga):
    mobil_ditemukan = False
    for mobil in car_available:
        if mobil['harga'] == harga:
            if not mobil_ditemukan:
                mobil_ditemukan = True
                print("Mobil dengan harga", harga, "yang tersedia:")
            print("{:<10} {:<15} {:<10} {:<10} {:<10}".format(mobil['id'],mobil['brand'], mobil['Model'], mobil['Tahun'], mobil['Warna'], mobil['harga']))
    if not mobil_ditemukan:
        print("Mobil dengan harga", harga, "tidak ditemukan.")

# UPDATE FUNCTION

# untuk fungsi updatenya
def update_car_info():
    while True:
        tampilkan_mobil()
        
        # Meminta input ID mobil yang ingin diupdate
        try:
            car_index = int(input("Pilih nomor mobil yang ingin diupdate: ")) - 1
            if car_index < 0 or car_index >= len(car_available):
                print(f"Tidak ada mobil dengan nomor {car_index + 1}. Silakan pilih nomor mobil yang tersedia.")
                continue
            else:
                break
        except ValueError:
            print("Input harus berupa nomor. Silakan coba lagi.")

    # Simpan ID mobil yang akan diupdate
    mobil_id = car_available[car_index]['id']

    print("\nUpdate informasi mobil:")

    print("Apakah Anda ingin mengupdate merek mobil? (yes/no)")
    update_brand = input().strip().lower()

    if update_brand == 'yes':
        new_brand = input(f"Merek ({car_available[car_index]['brand']}): ").strip()
        car_available[car_index]['brand'] = new_brand if new_brand else car_available[car_index]['brand']

    print("Apakah Anda ingin mengupdate model mobil? (yes/no)")
    update_model = input().strip().lower()

    if update_model == 'yes':
        new_model = input(f"Model ({car_available[car_index]['Model']}): ").strip()
        car_available[car_index]['Model'] = new_model if new_model else car_available[car_index]['Model']

    print("Apakah Anda ingin mengupdate tahun mobil? (yes/no)")
    update_tahun = input().strip().lower()

    if update_tahun == 'yes':
        new_tahun = input(f"Tahun ({car_available[car_index]['Tahun']}): ").strip()
        car_available[car_index]['Tahun'] = new_tahun if new_tahun else car_available[car_index]['Tahun']

    print("Apakah Anda ingin mengupdate warna mobil? (yes/no)")
    update_warna = input().strip().lower()

    if update_warna == 'yes':
        new_warna = input(f"Warna ({car_available[car_index]['Warna']}): ").strip()
        car_available[car_index]['Warna'] = new_warna if new_warna else car_available[car_index]['Warna']

    print("Apakah Anda ingin mengupdate harga sewa mobil? (yes/no)")
    update_harga = input().strip().lower()

    if update_harga == 'yes':
        new_harga = input(f"Harga ({car_available[car_index]['harga']}): ").strip()
        car_available[car_index]['harga'] = int(new_harga) if new_harga else car_available[car_index]['harga']

    # Memeriksa apakah ID mobil yang diupdate tetap sama
    if car_available[car_index]['id'] != mobil_id:
        print("Maaf, tidak bisa mengubah ID mobil setelah proses update dimulai.")
        # Mengembalikan ID mobil ke nilai sebelumnya
        car_available[car_index]['id'] = mobil_id

    print("Informasi mobil telah berhasil diupdate.")


# DELETE FUNCTION

# menghapus mobil dari daftar
def delete_car():
    print("Pilih kriteria untuk menghapus mobil:")
    print("1. Brand mobil")
    print("2. Model")
    print("3. Tahun")
    print("4. Warna")
    print("5. Harga sewa")

    choice = int(input("Masukkan pilihan (1-5): "))

    # Membuat list yang berisi nama atribut sesuai dengan indeks pilihan pengguna
    attributes = ['brand', 'Model', 'Tahun', 'Warna', 'harga']

    # Meminta nilai untuk atribut yang dipilih
    value_to_find = input(f"Masukkan nilai {attributes[choice-1]} mobil yang ingin dihapus: ").strip()

    found_cars = []
    # Mencari mobil yang memiliki nilai atribut yang sesuai dengan input pengguna
    for car in car_available:
        if car[attributes[choice-1]] == value_to_find:
            found_cars.append(car)

    if len(found_cars) == 0:
        print(f"Tidak ada mobil dengan {attributes[choice-1]} '{value_to_find}' dalam daftar.")
        return

    print("Berikut mobil yang akan dihapus:")
    for index, car in enumerate(found_cars, start=1):
        print(f"{index}. {car['brand']} {car['Model']} Tahun {car['Tahun']} - Warna: {car['Warna']} - Harga: Rp {car['harga']} per hari")

    confirm_delete = input("Apakah Anda yakin ingin menghapus mobil-mobil ini? (yes/no): ").strip().lower()

    if confirm_delete == 'yes':
        for car in found_cars:
            car_available.remove(car)
        print("Mobil-mobil telah dihapus dari daftar.")
    else:
        print("Penghapusan mobil dibatalkan.")

# MAIN MENU

def main_menu():
    while True:
        print("\n====== BOY'S CAR RENTAL ======")
        print("1. Tampilkan Mobil")
        print("2. Tambah Mobil Baru")
        print("3. Cari Mobil")
        print("4. Update Informasi Mobil")
        print("5. Hapus Mobil")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan Anda (1/2/3/4/5/6): ")

        if pilihan == '1':
            tampilkan_mobil()
            konfirmasi = input("Apakah Anda ingin melanjutkan program? (ya/tidak): ").lower()
            if konfirmasi != 'ya':
                print("Terima kasih telah menggunakan program rental mobil.")
                break
        elif pilihan == '2':
            tambah_mobil()
        elif pilihan == '3':
            print("Pilih kriteria pencarian:")
            print("a. Berdasarkan Model")
            print("b. Berdasarkan Tahun")
            print("c. Berdasarkan Warna")
            print("d. Berdasarkan Harga")

            kriteria = input("Masukkan kriteria pencarian (a/b/c/d): ")

            if kriteria == 'a':
                model = input("Masukkan model mobil yang ingin dicari: ")
                cari_mobil_berdasarkan_model(model)
            elif kriteria == 'b':
                tahun = input("Masukkan tahun mobil yang ingin dicari: ")
                cari_mobil_berdasarkan_tahun(tahun)
            elif kriteria == 'c':
                warna = input("Masukkan warna mobil yang ingin dicari: ")
                cari_mobil_berdasarkan_warna(warna)
            elif kriteria == 'd':
                while True:
                    try:
                        harga = int(input("Masukkan harga mobil yang ingin dicari: "))
                        cari_mobil_berdasarkan_harga(harga)
                        break
                    except ValueError:
                        print("Input harga harus berupa angka.")
        elif pilihan == '4':
            update_car_info()
        elif pilihan == '5':
            delete_car()
        elif pilihan == '6':
            print("Terima kasih telah program BOY'S CAR RENTAL. Sampai jumpa!!!")
            break
        else:
            print("Input tidak valid!!! Pilih angka 1 sampai 6.")

if __name__ == "__main__":     # fungsi utama untuk memulai program (start-nya di main_menu)
    main_menu()
