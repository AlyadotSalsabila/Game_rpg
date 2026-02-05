# Latihan 5

from abc import ABC, abstractmethod

# 1. Interface/ Abstract Class
# Ini adalah kontrak. Semua turunan wajib punya method di bawah ini

class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

# 2. Implementasi pada Class konkret
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")

class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    # Implementasi serang versi Monster
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")

# -- Uji Coba --
# unit = GameUnit() # ERROR! Abstract class tidak bisa jadi objek
h = Hero("Alucard")
m = Monster("Serigala")

h.info()
m.info()


# Analisis 5
# (1a) Pada class Hero, hapus (atau jadikan komentar #) seluruh blok method def serang(self, target):. Jalankan programnya. Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti pesan error Can't instantiate abstract class Hero with abstract method...? 
# (1b) Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di Interface?
# (2a) Coba aktifkan baris kode unit = GameUnit(). Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek?
# (2b) Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?
# Jawaban:
# (1a) Eror yang muncul adalah TypeError: Can't instantiate abstract class Hero without an implementation for abstract abstract method 'serang'. Artinya class Hero belum mengimplementasikan method serang yang diwajibkan oleh abstract class GameUnit (belum memenuhi syarat).
# (1b) Konsekuensinya adalah program akan menghasilkan error dan tidak bisa dijalankan.
# (2a) Karena GameUnit adalah abstract class yang berisi kontrak (aturan) untuk class turunannya. Abstract class tidak boleh diinstansiasi langsung.
# (2b) Gunanya adalah untuk memastikan bahwa semua class turunan memiliki method-method tertentu yang wajib diimplementasikan, sehingga konsistensi dan struktur kode tetap terjaga.

# Analisis 6: di game_rpg3.py