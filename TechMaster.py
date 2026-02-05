from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar, stok):
        self.nama = nama
        self.__harga_dasar = harga_dasar
        self.__stok = 0
        self.set_tambah_stok (stok)

    # Encapsulation
    # Getter
    def get_stok(self):
        return self.__stok
    
    def _get_harga_dasar(self):
        return self.__harga_dasar
    
    # Setter
    def set_tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit. Stok sekarang: {self.__stok}")

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def harga_setelah_pajak(self, jumlah):
        pass

# Pewarisan
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok, processor):
        super().__init__(nama, harga_dasar, stok)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"Laptop: {self.nama}")
        print(f"Processor: {self.processor}")
        print(f"Harga Dasar: {self._get_harga_dasar()}")
        print(f"Stok: {self.get_stok()}")
    
    def harga_setelah_pajak(self, jumlah):
        pajak = self._get_harga_dasar() * 0.10
        subtotal = (self._get_harga_dasar() + pajak) * jumlah
        return pajak, subtotal
    
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok, kamera):
        super().__init__(nama, harga_dasar, stok)
        self.kamera = kamera

    def tampilkan_detail(self, jumlah):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera} MP")
        print(f"Harga Dasar: {self._get_harga_dasar()} | Pajak(5%): Rp{int(self._get_harga_dasar() * 0.05):,}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp{int((self._get_harga_dasar() * 1.05) * jumlah):,}")

    def harga_setelah_pajak(self, jumlah):
        pajak = self._get_harga_dasar() * 0.05
        subtotal = (self._get_harga_dasar() + pajak) * jumlah
        return pajak, subtotal
    
# Polymorphism
def transaksi(daftar_barang):
    total = 0
    print("\n--- STRUK TRANSAKSI ---")
    for i, (barang, jumlah) in enumerate(daftar_barang, start=1):
        print(f"{i}.", end="")

        pajak, subtotal = barang.harga_setelah_pajak(jumlah)
        harga = barang._get_harga_dasar()

        persen = 10 if isinstance(barang, Laptop) else 5

        print(f"Harga dasar: Rp{harga: ,} | Pajak({persen}%): Rp {int(pajak):,}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}\n")

        total += subtotal

    print("-" * 32)
    print(f"Total Belanja: Rp {int(total):,}")
    print("-" * 32)

# Main Program
print("---SETUP DATA ---")
laptop = Laptop("ROG Zephyrus", 20000000, 10, "Ryzen 9")
hp = Smartphone("iPhone 13", 15000000, -5, "12 MP")
hp.set_tambah_stok(20)

keranjang = [
    (laptop, 2),
    (hp, 1)
]

transaksi(keranjang)