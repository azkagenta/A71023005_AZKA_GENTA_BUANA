class Mobil:
    def move(self):
        print("Berjalan di jalan raya")

class Pesawat:
    def move(self):
        print("Terbang di udara")

class Kapal:
    def move(self):
        print("Berlayar di laut")

# Membuat objek dari masing-masing kelas
mobil = Mobil()
pesawat = Pesawat()
kapal = Kapal()

# Memanggil metode move() pada masing-masing objek
mobil.move()      # Output: Berjalan di jalan raya
pesawat.move()    # Output: Terbang di udara
kapal.move()      # Output: Berlayar di laut  