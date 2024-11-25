'berisi memmbuka dan menyimpan file kontak'

def open_kontak(path='kontak.txt'):
    with open(path, mode='r')as file:
        kontak = file.readlines()
    return kontak

def save_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w')as file:
        file.writelines(isi)