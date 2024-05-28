from Personel import Personel

class Hemşire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, çalişma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__çalişma_saati = çalişma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def __str__(self):
        return f"{super().__str__()}\nÇalışma Saati: {self.__çalişma_saati}\nSertifika: {self.__sertifika}\nHastane: {self.__hastane}"
    
    def get_çalişma_saati(self):
        return self.__çalişma_saati
    
    def get_sertifika(self):
        return self.__sertifika
    
    def get_hastane(self):
        return self.__hastane
    
    def set_çalişma_saati(self, çalişma_saati):
        self.__çalişma_saati = çalişma_saati

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika
    
    def set_hastane(self, hastane):
        self.__hastane = hastane

    def getter(self):
        bilgiler = [
            self.get_personel_no(),
            self.get_ad(),
            self.get_soyad(),
            self.get_departman(),
            self.get_maas(),
            self.get_çalişma_saati(),
            self.get_sertifika(),
            self.get_hastane()
        ]
        return bilgiler
    
    def setter(self):
        print("-:> Personel No (1)\n-:> Ad (2) \n-:> Soyad (3)\n-:> Departman (4)\n-:> Maaş (5)\n-:> Çalışma Saati (6)\n-:> Sertifika (7)\n-:> Hastane (8)")
        secim = int(input("Değiştirmek istediğiniz kısmı seçiniz: "))
        
        if secim == 1:
            self.set_personel_no(input("Yeni personel no giriniz: "))
        elif secim == 2:
            self.set_ad(input("Yeni ad giriniz: "))
        elif secim == 3:
            self.set_soyad(input("Yeni soyad giriniz: "))
        elif secim == 4:
            self.set_departman(input("Yeni departman giriniz: "))
        elif secim == 5:
            self.set_maas(input("Yeni maaş değerini giriniz: "))
        elif secim == 6:
            self.set_çalişma_saati(input("Yeni çalışma saati giriniz: "))
        elif secim == 7:
            self.set_sertifika(input("Yeni sertifika giriniz: "))
        elif secim == 8:
            self.set_hastane(input("Yeni hastane giriniz: "))

    def maaş_arttir(self,yüzde_artiş):
        self.__maas = int(self.__maas) * (100 + yüzde_artiş) / 100