from typing import Self

class Hero:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang dengan tangan kosong.")

# Child class 1
class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")

# Child class 2
class Archer(Hero):
    def tembak_panah(self):
        print(f"{self.nama} (Archer) memanah lebih jauh! jleb!")

# Child class 3
class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")

class Healer(Hero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan")

# -- Penerapan Polymorphism --
# Kita punya daftar hero campuran
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),
    Fighter("Zilong"),
    Mage("Gord"),
    Healer("Angela")
]

print("--- PERANG DIMULAI ---")

# Satu perintah loop, tapi respon berbeda beda (Polymorphism)
for pahlawan in pasukan:
    pahlawan.serang()

# Analisis 6:
# (1) Perintah: tanpa mengubah satu huruf pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class baru bernama Healer(Hero). Isi method serang milik Healer dengan: print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!"). Masukkan objek Healer ke dalam list pasukan
# (1a) Apakah program berjalan lancar?
# (1b) Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer ketika harus mengupdate game dengan karakter baru di masa depan?
# (2) Perintah: Ubah nama method serang pada class Archer menjadi tembak_panah. Jalankan program.
# (2a) Apa yang terjadi?
# (2b) Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan berbagai Child Class harus persis sama?
# Jawaban:
# (1a) Ya
# (1b) Keuntungan Polimorfisme adalah programmer dapat menambahkan karakter baru tanpa perlu mengubah kode yang sudah ada.
# (2a) Hasilnya archer tidak muncul, akan tetapi digantikan oleh "Hero menyerang dengan tangan kosong.
# (2b) Karena Polimorfisme bergantung pada kesamaan nama method untuk memanggil method yang sesuai pada objek yang berbeda.  
