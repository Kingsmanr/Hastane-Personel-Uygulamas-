from Personel import Personel

class Doktor(Personel):

    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def __str__(self):
        return f"{super().__str__()}\nUzmanlık: {self.__uzmanlik}\nDeneyim Yılı: {self.__deneyim_yili}\nHastane: {self.__hastane}"
    
    def get_uzmanlik(self):
        return self.__uzmanlik

    def get_deneyim_yili(self):
        return self.__deneyim_yili

    def get_hastane(self):
        return self.__hastane

    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self, hastane):
        self.__hastane = hastane
    
    def getter(self):
        bilgiler = [
            self.get_personel_no(),
            self.get_ad(),
            self.get_soyad(),
            self.get_departman(),
            self.get_maas(),
            self.get_uzmanlik(),
            self.get_deneyim_yili(),
            self.get_hastane()
        ]
        return bilgiler
    
    def setter(self):
        print("-:> Personel No (1)\n-:> Ad (2) \n-:> Soyad (3)\n-:> Departman (4)\n-:> Maaş (5)\n-:> Uzmanlık (6)\n-:> Deneyim Yılı (7)\n-:> Hastane (8)")
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
            self.set_uzmanlik(input("Yeni uzmanlık giriniz: "))
        elif secim == 7:
            self.set_deneyim_yili(input("Yeni deneyim yılını giriniz: "))
        elif secim == 8:
            self.set_hastane(input("Yeni hastane giriniz: "))

    def maaş_arttir(self,yüzde_artiş):
        self.__maas = int(self.__maas) * (100 + yüzde_artiş) / 100
