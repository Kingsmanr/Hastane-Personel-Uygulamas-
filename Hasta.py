
class Hasta():

    def __init__(self,hasta_no,ad,soyad,dogum_tarihi,hastalik,tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi
        # nesne oluşturuken aldığımız değerleri değişkenlere atıyoruz


    def __str__(self):
        return f"\nHasta No: {self.__hasta_no} \nAd: {self.__ad} \nSoyad: {self.__soyad} \nDoğum Tarihi: {self.__dogum_tarihi} \nHastalik: {self.__hastalik} \nTedavi: {self.__tedavi}"
    # nesnenin yazdırılması istenmesi durumunda bilgileri nesnenin bilgilerini yazdırmak için bu fonksiyonu kullanıyoruz
    

    def get_hasta_no(self):
        return self.__hasta_no
    
    def get_ad(self):
        return self.__ad
    
    def get_soyad(self):
        return self.__soyad
    
    def get_dogum_tarihi(self):
        return self.__dogum_tarihi
    
    def get_hastalik(self):
        return self.__hastalik
                                                            # get/set metodları
    def get_tedavi(self):
        return self.__tedavi
    
    def set_hasta_no(self,hasta_no):
        self.__hasta_no = hasta_no

    def set_ad(self,ad):
        self.__ad = ad
    
    def set_soyad(self,soyad):
        self.__soyad = soyad

    def set_dogum_tarihi(self,doğum_tarihi):
        self.__dogum_tarihi = doğum_tarihi
    
    def set_hastalik(self,hastalik):
        self.__hastalik = hastalik

    def set_tedavi(self,tedavi):
        self.__tedavi = tedavi

    def tedavi_suresi_hesapla(self):
        return len(self.__tedavi) * 10 
    # tedavi süresini hesaplamak için kullandığımız fonksiyon

    