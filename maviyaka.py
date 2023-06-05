from calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi       # Yıpranma payı

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                return self.get_maas() * self.__yipranma_payi * 10
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                return (self.get_maas() * self.get_tecrube() / 100) / 2 + self.__yipranma_payi * 10
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                return (self.get_maas() * self.get_tecrube() / 100) / 3 + self.__yipranma_payi * 10
            else:
                return self.get_maas()
        except ValueError:
            print("Hata: Tecrübe değeri geçersiz.")

    def __str__(self):
        yeni_maas = self.zam_hakki()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()} ay\nYeni Maaş: {yeni_maas}"
    # Çıktı metni oluşturulurken "zam_hakki" metodunu kullanıyoruz