class Insan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk):     # Örnek değişkenleri başlat
        self.__tc_no = tc_no       #TcNo
        self.__ad = ad    #Ad
        self.__soyad = soyad #Soyad
        self.__yas = yas   #Yas
        self.__cinsiyet = cinsiyet   #Cinsiyet
        self.__uyruk = uyruk     #Uyruk

    def get_tc_no(self):
        return self.__tc_no

    def set_tc_no(self, tc_no):
        self.__tc_no = tc_no

    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_yas(self):
        return self.__yas

    def set_yas(self, yas):
        self.__yas = yas

    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    def get_uyruk(self):
        return self.__uyruk

    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    def __str__(self):
        return f"TC No: {self.__tc_no}\nAd: {self.__ad}\nSoyad: {self.__soyad}\nYaş: {self.__yas}\nCinsiyet: {self.__cinsiyet}\nUyruk: {self.__uyruk}"