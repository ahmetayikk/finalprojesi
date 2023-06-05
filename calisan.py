from insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.kontrol_sektor(sektor)       # Sektörü kontrol etmek için "kontrol_sektor" metodunu kullanıyoruz
        self.__tecrube = tecrube  #Tecrube
        self.__maas = maas  #Maas
        self.tc_no = tc_no   #Tc No

    def kontrol_sektor(self, sektor):
        secenekler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        if sektor.lower() in secenekler:
            return sektor.lower()
        else:
            raise ValueError("Hata: Geçersiz sektor değeri.")

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = self.kontrol_sektor(sektor)

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        try:
            if self.__tecrube < 2:
                return 0
            elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
                return self.__maas * self.__tecrube / 100
            elif self.__tecrube > 4 and self.__maas < 25000:
                return (self.__maas * self.__tecrube) / 200
            else:
                return self.__maas
        except Exception as e:
            print("Hata: ", str(e))
    
    def yeni_maas(self):
        return self.zam_hakki()


    def __str__(self):
        yeni_maas = self.zam_hakki()
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.__tecrube} ay\nYeni Maaş: {yeni_maas}" 
    # Çıktı metni oluşturulurken "zam_hakki" metodunu kullanıyoruz