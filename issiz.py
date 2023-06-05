from insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrubeler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrubeler = tecrubeler   # değişken "__tecrubeler" tanımlanıyor 
        self.__statu = None           #değişken olan "__statu" tanımlanıyor

    def get_tecrubeler(self):
        return self.__tecrubeler

    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler

    def statu_bul(self):
        try:
            statu_etkileri = {
                "mavi yaka": 0.2,
                "beyaz yaka": 0.35,
                "yönetici": 0.45
            }

            en_yuksek_etki = max(self.__tecrubeler.values())
            for statu, etki in self.__tecrubeler.items():
                if etki == en_yuksek_etki:
                    self.__statu = statu           #En yüksek etkiye sahip olan statü belirleniyor
                    break
        except ValueError:
            print("Hata: Tecrübe değerleri geçersiz.")

    def get_statu(self):
        return self.__statu

    def __str__(self):
        self.statu_bul()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nEn Uygun Statü: {self.__statu}"


# Sınıfların kullanımı:
tecrubeler = {
    "mavi yaka": 4,
    "beyaz yaka": 8,
    "yönetici": 6
}

issiz = Issiz("12345678900", "Ahmet", "Yılmaz", 25, "Erkek", "Türkiye", tecrubeler)
print(issiz)