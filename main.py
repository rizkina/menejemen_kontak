# Program Manajemen Kontak
kontak1 ={"nama": "Andi", "HP" : 123866, "email" : "andi@yahoo.com" }
kontak2 ={"nama": "Ani", "HP" : 1253993, "email" : "ani@gmail.com" }
kontak = [kontak1,kontak2]

while True:
    print("\n Menu Kontak")
    print("1. Melihat semua kontak")
    print("2. Menmbah Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari kontak")
    print("=========================")

    pil = input("Masukan pilihan menu kontak (1,2,3 atau 4): ")

    if pil == "1":
        # melihat seluruh isi kontak
        if kontak:
            for n, item in enumerate(kontak, start=1):
                print(f"\n{n}. {item['nama']} ({item['HP']}, {item['email']}) ")
        else:
            print("Kontak masih kosong, silakan pilih menu 2 atau 4.")
            continue
    elif pil == "2":
        # menambahkan kontak baru
        print("Masukan data kontak baru")
        print("===========================")
        nama = input("Masukan nama: ")
        HP = input("Masukan nomor HP: ")
        email = input("Masukan email: ")
        kontak_baru = {"nama":nama, "HP": HP, "email": email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")
    elif pil == "3":
        # menghapus kontak
        if kontak:
            for n, item in enumerate(kontak, start=1):
                print(f"\n{n}. {item['nama']} ({item['HP']}, {item['email']}) ")
            i_hapus = int(input("Masukan nomor index kontak yang akan dihapus : "))
            del kontak[i_hapus-1]
            print("Kontak berhasil dihapus.")
        else:
            print("Kontak kosong, silakan pilih menu lain.")
            continue
    elif pil == "4":
        break
    else:
        print("Anda salah memasukan pilihan")