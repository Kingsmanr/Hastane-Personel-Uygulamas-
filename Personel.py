class Personel(): # personel adında sınıf oluşturuyoruz

    def __init__(self, personel_no, ad, soyad, departman, maas): # nesne oluşturuken aldığımız değerleri değişkenlere atıyoruz
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman    
        self.__maas = maas

    def __str__(self):
        return f"\nPersonel No: {self.__personel_no}\nİsim: {self.__ad}\nSoyad: {self.__soyad}\nDepartman: {self.__departman}\nMaaş: {self.__maas}" 
            # nesnenin yazdırılması istenmesi durumunda bilgileri nesnenin bilgilerini yazdırmak için bu fonksiyonu kullanıyoruz
    
    def get_personel_no(self):
        return self.__personel_no 
    
    def get_ad(self):
        return self.__ad
    
    def get_soyad(self):
        return self.__soyad
    
    def get_departman(self):
        return self.__departman
    
    def get_maas(self):
        return self.__maas                         # get/set metodları
    
    def set_personel_no(self, personel_no):
        self.__personel_no = personel_no
    
    def set_ad(self, ad):
        self.__ad = ad
    
    def set_soyad(self, soyad):
        self.__soyad = soyad
    
    def set_departman(self, departman):
        self.__departman = departman
    
    def set_maas(self, maas):
        self.__maas = maas
