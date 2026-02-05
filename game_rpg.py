from typing import Self

class Hero:

# Latihan 1
# Constructor: Dijalankan saat Hero baru dibuat
    def __init__(self, name, hp, attack_power):
        self.name = name # Nama Hero
        self.hp = hp # Nyawa (Health Point)
        self.attack_power = attack_power # Kekuatan Serangan

# Method untuk menampilkan info hero
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")


# Latihan 2
# # Method menyerang: Objek ini (self) menyerang objek lain (lawan)
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

# Method diserang: Menerima damage
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

# Latihan 3
# Class Mage adalah anak dari class Hero
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power) # Memanggil constructor milik Parent (Hero)
        self.mana = mana  

    def info(self):
        print(f"{self.name} [Mage] | HP:{self.hp} | Mana:{self.mana}")

    # Mage punya skill khusus
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            lawan.diserang(self.attack_power * 2) # Damage ganda
            self.mana -= 20
            lawan.diserang(self.attack_power * 2) # Damage 2x lipat
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")
        
# Latihan 4
class HeroEnkap:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal # Enkapsulasi: HP bersivat private (hanya bisa diakses di dalam class ini)

    # Getter: Cara untuk melihat HP
    def get_hp(self):
        return self.__hp
        
    # Setter: Cara untuk mengubah HP (dengan validasi)
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
           self.__hp = 0    # hp tdk boleh negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage    # Pakai setter/getter bahkan di dalam class sendiri agar aman
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")

# -- Main Program --

# Membuat Object (Instansiasi)
hero1 = Hero("Layla", 100, 15)
hero1.hp = 500  # Latihan 1
hero2 = Hero("Zilong", 120, 20)

# Memanggil Method
hero1.info()
hero2.info()

print(hero1.hp) # Latihan 1

# Latihan 2
print("\n --- Pertarungan Dimulai ---") 
hero1.serang(hero2) # Layla serang Zilong
hero2.serang(hero1) # Zilong serang Layla

# Latihan 3
print("\n--- Update Class Hero ---")
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
eudora.serang(balmond) # Serangan biasa (warisan dari Hero)
eudora.skill_fireball(balmond) # Skill khusus Mage

# Latihan 4
# -- Uji coba --
hero1 = HeroEnkap("Layla", 100)

# hero1.__hp = 9999 # GAGAL (tidak bisa mengubah hp asli)
# print(hero1.__hp) # EROR (tidak bisa dibaca langsung)

hero1.set_hp(-50) # Coba negatif
print(hero1.get_hp()) # Harusnya 0 

# print(f"Mencoba akses paksa: {hero1._Hero__hp}")

# Analisis 1:
# Apa yang terjadi ketika mengubah hero1.hp menjadi 500 setelah baris hero1 = hero..?
# Jawaban: Nilai hp dari objek hero1 diubah menjadi 500.   
# Output: dari Hero: Layla | HP:100 |Power: 15 menjadi Hero: Layla | HP:500 |Power: 15

# Analisis 2:
# Perhatikan parameter lawan pada method serang. Parameter tersebut menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?
# Jawaban: Karena objek utuh memungkinkan kita untuk mengakses semua properti dan method dari objek lawan, seperti hp, attack_power, dll. Jika hanya menerima string nama, kita tidak bisa mengakses informasi lain dari objek lawan.

# Analisis 3:
# Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan komentar #) baris kode super().__init__(name, hp, attack_power). Kemudian jalankan programnya.
# (1) Error apa yang muncul saat kamu mencoba melihat info Eudora (eudora.info())? Mengapa error tersebut mengatakan Mage object has no attribute 'name', padahal kita sudah mengirim nama "Eudora" saat pembuatan objek?
# (2) Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke class Induk!
# Jawaban:
# (1) Eror yg muncul adalah AttributeError: 'Mage' object has no attribute 'name'. Hal ini terjadi karena membuat atribut name, hp, dan attack_power tidak terpanggil/tidak bisa dijalankan.
# (2) super() berfungsi untuk memanggil constructor atau method milik class Induk sehingga data dan atribut dari class Induk dapat digunakan oleh class Anak secara utuh.

# Analisis 4:
# (1) Tambahkan print(f"Mencoba akses paksa: {hero1._Hero__hp}") - Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan temanmy mengapa Python masih mengizinkan akses ini (konsep Name Mangling) dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman yang baik.
# (2) Hapus logika if dan elif di dalam method set_hp, sehingga isinya hanya self.__hp = nilai_baru. - Kemudian lakukan hero1.set_hp(-100). Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method Setter sangat penting untuk menjaga integritas data dalam game!
# Jawaban:
# (1) Hasilnya eror. Namun, kita tetap tidak boleh melakukannya karena melanggar prinsip enkapsulasi dan dapat menyebabkan kerusakan data.
# (2) hp hero1 menjadi -50. Keberadaan setter penting untuk menjaga integritas data dengan memastikan bahwa nilai yang diberikan valid dan sesuai dengan aturan yang ditetapkan dalam game.

# Analisis 5: di game_rpg2.py