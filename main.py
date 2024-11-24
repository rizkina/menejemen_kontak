# Program Manajemen Kontak
def open_kontak(path='kontak.txt'):
    with open(path, mode='r')as file:
        kontak = file.readlines()
    return kontak

def save_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w')as file:
        file.writelines(isi)

class Kontak:
    def __init__(self):
        self.kontak = open_kontak()

    def melihat_kontak(self):
        if self.kontak:
            for n, item in enumerate(self.kontak, start=1):
                print(f"{n}. " + item)
        else:
            print("Kontak masih kosong, silakan pilih menu 2 atau 4.")
            return 1

    def menambah_kontak(self):
        print("Masukan data kontak baru")
        print("===========================")
        nama = input("Masukan nama: ")
        hp = input("Masukan nomor HP: ")
        email = input("Masukan email: ")
        kontak_baru = f"{nama} ({hp}, {email})"+"\n"
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")

    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("Masukan nomor index kontak yang akan dihapus : "))
                del self.kontak[i_hapus - 1]
                print("Kontak berhasil dihapus.")
            except:
                print("Input yang dimasukan salah")

    def keluar_kontak(self):
        save_kontak(isi=self.kontak)

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

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
        kontak_kantor.melihat_kontak()
    elif pil == "2":
        # menambahkan kontak baru
        kontak_kantor.menambah_kontak()
    elif pil == "3":
        # menghapus kontak
        kontak_kantor.menghapus_kontak()
    elif pil == "4":
        kontak_kantor.keluar_kontak()
        break
    else:
        print("Anda salah memasukan pilihan")