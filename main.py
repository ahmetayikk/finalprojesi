import pandas as pd
from insan import Insan
from issiz import Issiz
from calisan import Calisan
from maviyaka import MaviYaka
from beyazyaka import BeyazYaka

# insan sınıfı için 2 nesne oluşturma
insan1 = Insan("12345678910", "Ahmet", "Ayik", 30, "Erkek", "Türk")
insan2 = Insan("98765432100", "Mehmet", "Ayik", 25, "Erkek", "Türk")

# İnsan nesnelerini __str__ metoduyla bilgilerini yazdırma
print(insan1)
print(insan2)

# İşsiz sınıfı için 3 nesne oluşturma
issiz1 = Issiz("12345678910", "Elif", "Ayik", 28, "Kadin", "Türk", {"mavi yaka": [2018], "beyaz yaka": [2019, 2020]})
issiz2 = Issiz("98765432100", "Dila", "Turkar", 32, "Kadin", "Türk", {"beyaz yaka": [2021]})
issiz3 = Issiz("55555555555", "Mehmet", "Kara", 26, "Erkek", "Türk", {"mavi yaka": [2017, 2018, 2019]})

# İşsiz nesnelerini __str__ metoduyla bilgilerini yazdırma
print(issiz1)
print(issiz2)
print(issiz3)

# Çalışan sınıfı için 3 nesne oluşturma
calisan1 = Calisan("12345678910", "Burcu", "Guzelyali", 28, "Kadin", "Türk", "teknoloji", 36, 12000)
calisan2 = Calisan("98765432100", "Ulas", "Ermis", 32, "Erkek", "Türk", "muhasebe", 48, 18000)
calisan3 = Calisan("55555555555", "Ceren", "Erbas", 18, "Kadin", "Türk", "inşaat", 24, 9000)

# Çalışan nesnelerini __str__ metoduyla bilgilerini yazdırma
print(calisan1)
print(calisan2)
print(calisan3)

# Mavi yaka sınıfı için 3 nesne oluşturma
maviyaka1 = MaviYaka("12345678910", "Ali", "Yilmaz", 28, "Erkek", "Türk", "teknoloji", 36, 12000, 0.2)
maviyaka2 = MaviYaka("98765432100", "Ayşe", "Kara", 32, "Kadin", "Türk", "muhasebe", 48, 18000, 0.5)
maviyaka3 = MaviYaka("55555555555", "Kerem", "Akturk", 26, "Erkek", "Türk", "inşaat", 24, 9000, 0.3)

# Mavi yaka nesnelerini __str__ metoduyla bilgilerini yazdırma
print(maviyaka1)
print(maviyaka2)
print(maviyaka3)

# Beyaz yaka sınıfı için 3 nesne oluşturma
beyazyaka1 = BeyazYaka("12345678910", "Ayşe", "Yilmaz", 28, "Kadin", "Türk", "teknoloji", 36, 12000, 500)
beyazyaka2 = BeyazYaka("98765432100", "Ahmet", "Kara", 32, "Erkek", "Türk", "muhasebe", 48, 18000, 2500)
beyazyaka3 = BeyazYaka("55555555555", "Mehmet", "Demir", 26, "Erkek", "Türk", "inşaat", 24, 9000, 1000)

# Beyaz yaka nesnelerini __str__ metoduyla bilgilerini yazdırma
print(beyazyaka1)
print(beyazyaka2)
print(beyazyaka3)

# Çalışan, mavi yaka ve beyaz yaka nesnelerinin tüm değerlerini içeren bir DataFrame oluşturma
data = {
    "Nesne": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
    "Tc No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(), beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],
    "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(), beyazyaka1.get_ad(), beyazyaka2.get_ad(), beyazyaka3.get_ad()],
    "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(), beyazyaka1.get_soyad(), beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],
    "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(), beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()],
    "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(), beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
    "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(), beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(), beyazyaka3.get_uyruk()],
    "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), maviyaka1.get_sektor(), maviyaka2.get_sektor(), maviyaka3.get_sektor(), beyazyaka1.get_sektor(), beyazyaka2.get_sektor(), beyazyaka3.get_sektor()],
    "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), maviyaka1.get_tecrube(), maviyaka2.get_tecrube(), maviyaka3.get_tecrube(), beyazyaka1.get_tecrube(), beyazyaka2.get_tecrube(), beyazyaka3.get_tecrube()],
    "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), maviyaka1.get_maas(), maviyaka2.get_maas(), maviyaka3.get_maas(), beyazyaka1.get_maas(), beyazyaka2.get_maas(), beyazyaka3.get_maas()],
    "Yıpranma Payı": [0, 0, 0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(), maviyaka3.get_yipranma_payi(), 0, 0, 0],
    "Teşvik Prim": [0, 0, 0, 0, 0, 0, beyazyaka1.get_tesvik_primi(), beyazyaka2.get_tesvik_primi(), beyazyaka3.get_tesvik_primi()],
    "Yeni Maaş": [calisan1.yeni_maas(), calisan2.yeni_maas(), calisan3.yeni_maas(), maviyaka1.yeni_maas(), maviyaka2.yeni_maas(), maviyaka3.yeni_maas(), beyazyaka1.yeni_maas(), beyazyaka2.yeni_maas(), beyazyaka3.yeni_maas()]
}

df = pd.DataFrame(data)

# Değişken değerlerinin bazılarını 0 atama
df.fillna(0, inplace=True)

# Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş ortalamalarını hesaplama
print("                                                          ")
print("Tecrube ve yeni maas ortalamalari : ")
gruplanmis_df = df.groupby("Nesne").agg({"Tecrübe": "mean", "Yeni Maaş": "mean"})
print(gruplanmis_df)
print("                                                                   ")

# Maaşı 15000 TL üzerinde olanların toplam sayısını bulma
maas_ust_limit = 15000
maas_ust_limit_sayisi = len(df[df["Maaş"] > maas_ust_limit])
print("Maaşı 15000 TL üzerinde olanların toplam sayısı:", maas_ust_limit_sayisi)
print("                                                               ")

# Yeni maaşa göre DataFrame'i küçükten büyüğe sıralama
df_sorted = df.sort_values(by="Yeni Maaş")
print(df_sorted)
print("                                                            ")

# Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulma
tecrube_limit = 35
beyazyaka_tecrube = df[(df["Nesne"] == "Beyaz Yaka") & (df["Tecrübe"] > tecrube_limit)]
print("Tecrubesi 3 yıldan fazla olan beyazyakalılar:")
print(beyazyaka_tecrube)
print("                                                                   ")

# Yeni maaşı 10000 TL üzerinde olanlar için 2-5 satır arasındakileri tc_no ve yeni_maaş sütunlarını seçerek gösterme
print("Yeni maasi 10000 TL uzerinde olanlar : ")
yeni_maas_limit = 10000
yeni_maas_ust_limit_df = df[df["Yeni Maaş"] > yeni_maas_limit][["Tc No", "Yeni Maaş"]]
print(yeni_maas_ust_limit_df)
print("                                                    ")

# Ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame oluşturma
yeni_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]
print(yeni_df)