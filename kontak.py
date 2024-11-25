'berisi class kontak untuk menjalankan program kontak'
import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.open_kontak()

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
        dokumen.save_kontak(isi=self.kontak)
