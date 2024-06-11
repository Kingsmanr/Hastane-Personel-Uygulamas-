from Personel import Personel

class Doktor(Personel):

    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane): 
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane
    # nesne oluşturuken aldığımız değerleri değişkenlere atıyoruz
  
    def __str__(self):
        return f"{super().__str__()}\nUzmanlik: {self.__uzmanlik}\nDeneyim Yili: {self.__deneyim_yili}\nHastane: {self.__hastane}"
       # nesnenin yazdırılması istenmesi durumunda bilgileri nesnenin bilgilerini yazdırmak için bu fonksiyonu kullanıyoruz
    
    def get_uzmanlik(self):
        return self.__uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def get_hastane(self):
        return self.__hastane              # get/set metodları

    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self, hastane):
        self.__hastane = hastane
    
    def maas_arttir(self, yüzde_artis): # bize verilen yüzdelik değer ile maaş değişkenini güncelliyoruz
        self.__maas = int(float(self.__maas) * (100 + yüzde_artis) / 100)
