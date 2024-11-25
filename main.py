# Program Manajemen Kontak
import kontak
def main():
    kontak_kantor = kontak.Kontak()
    kontak_keluarga = kontak.Kontak()

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

if __name__ == "__main__":
    main()