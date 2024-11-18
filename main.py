# Program Manajemen Kontak

def melihat_kontak():
    if kontak:
        for n, item in enumerate(kontak, start=1):
            print(f"\n{n}. {item['nama']} ({item['hp']}, {item['email']}) ")
    else:
        print("Kontak masih kosong, silakan pilih menu 2 atau 4.")
        return 1

def menambah_kontak():
    print("Masukan data kontak baru")
    print("===========================")
    nama = input("Masukan nama: ")
    hp = input("Masukan nomor HP: ")
    email = input("Masukan email: ")
    kontak_baru = {"nama": nama, "hp": hp, "email": email}
    kontak.append(kontak_baru)
    print("Kontak baru berhasil ditambahkan")

def menghapus_kontak():
    if melihat_kontak() == 1:
        return

    else:
        i_hapus = int(input("Masukan nomor index kontak yang akan dihapus : "))
        del kontak[i_hapus - 1]
        print("Kontak berhasil dihapus.")

kontak1 ={"nama": "Andi", "hp" : 123866, "email" : "andi@yahoo.com" }
kontak2 ={"nama": "Ani", "hp" : 1253993, "email" : "ani@gmail.com" }
kontak = [kontak1,kontak2]

while True:
    print("\n Menu Kontak")
    print("1. Melihat semua kontak")
    print("2. Menambah Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar dari kontak")
    print("=========================")

    pil = input("Masukan pilihan menu kontak (1,2,3 atau 4): ")

    if pil == "1":
        # melihat seluruh isi kontak
        melihat_kontak()
    elif pil == "2":
        # menambahkan kontak baru
        menambah_kontak()
    elif pil == "3":
        # menghapus kontak
        menghapus_kontak()
    elif pil == "4":
        break
    else:
        print("Anda salah memasukan pilihan")