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

    def maas_arttir(self, yüzde_artis):
        self.__maas = int(float(self.__maas) * (100 + yüzde_artis) / 100)