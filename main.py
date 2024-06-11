from Personel import Personel
from Doktor import Doktor
from Hemşire import Hemşire
from Hasta import Hasta
import pandas as pd
# gerekli kütüphaneleri ekliyoruz

def main():
    try: # try/except kullanarak olasi hatalarin önüne geçmeye çalişiyoruz
        # Personel nesneleri
        personel1 = Personel(1, "Ahmet", "Yilmaz", "Muhasebe", 5000)
        personel2 = Personel(2, "Mehmet", "Kaya", "İK", 6000)

        print(personel1)
        print(personel2)

        # Doktor nesneleri
        doktor1 = Doktor(3, "Ayşe", "Demir", "Cerrahi", 10000, "Cerrah", 7, "Hastane A")
        doktor2 = Doktor(4, "Fatma", "Kurt", "Dahiliye", 11000, "Dahiliye Uzmani", 5, "Hastane B")
        doktor3 = Doktor(5, "Ali", "Şahin", "Pediatri", 9500, "Pediatrist", 3, "Hastane C")

        print(doktor1)
        print(doktor2)
        print(doktor3)

        # Hemşire nesneleri
        hemsire1 = Hemşire(6, "Zeynep", "Kara", "Cerrahi", 4000, 40, "Yoğun Bakim", "Hastane A")
        hemsire2 = Hemşire(7, "Buse", "Ak", "Dahiliye", 4200, 45, "Acil", "Hastane B")
        hemsire3 = Hemşire(8, "Derya", "Yildiz", "Pediatri", 3800, 35, "Yeni Doğan", "Hastane C")

        print(hemsire1)
        print(hemsire2)
        print(hemsire3)

        # Hasta nesneleri
        hasta1 = Hasta(1, "Ali", "Veli", "2000-01-01", "Grip", "İlaç Tedavisi")
        hasta2 = Hasta(2, "Veli", "Ali", "1990-05-15", "Kirik", "Ameliyat")
        hasta3 = Hasta(3, "Ahmet", "Mehmet", "1985-08-30", "Şeker", "Diyet")

        print(hasta1)
        print(hasta2)
        print(hasta3)

        # Pandas DataFrame işlemleri
        data = [
            [personel1.get_ad(), personel1.get_soyad(), personel1.get_departman(), personel1.get_maas(), None, None, None, None, None, None, None, None, None],
            [personel2.get_ad(), personel2.get_soyad(), personel2.get_departman(), personel2.get_maas(), None, None, None, None, None, None, None, None],
            [doktor1.get_ad(), doktor1.get_soyad(), doktor1.get_departman(), doktor1.get_maas(), doktor1.get_uzmanlik(), doktor1.get_deneyim_yili(), doktor1.get_hastane(), None, None, None, None, None, None],
            [doktor2.get_ad(), doktor2.get_soyad(), doktor2.get_departman(), doktor2.get_maas(), doktor2.get_uzmanlik(), doktor2.get_deneyim_yili(), doktor2.get_hastane(), None, None, None, None, None, None],
            [doktor3.get_ad(), doktor3.get_soyad(), doktor3.get_departman(), doktor3.get_maas(), doktor3.get_uzmanlik(), doktor3.get_deneyim_yili(), doktor3.get_hastane(), None, None, None, None, None, None],
            [hemsire1.get_ad(), hemsire1.get_soyad(), hemsire1.get_departman(), hemsire1.get_maas(), None, None, hemsire1.get_hastane(), hemsire1.get_calisma_saati(), hemsire1.get_sertifika(), None, None, None, None],
            [hemsire2.get_ad(), hemsire2.get_soyad(), hemsire2.get_departman(), hemsire2.get_maas(), None, None, hemsire2.get_hastane(), hemsire2.get_calisma_saati(), hemsire2.get_sertifika(), None, None, None, None],
            [hemsire3.get_ad(), hemsire3.get_soyad(), hemsire3.get_departman(), hemsire3.get_maas(), None, None, hemsire3.get_hastane(), hemsire3.get_calisma_saati(), hemsire3.get_sertifika(), None, None, None, None],
            [hasta1.get_ad(), hasta1.get_soyad(), None, None, None, None, None, None, None, hasta1.get_hasta_no(), hasta1.get_dogum_tarihi(), hasta1.get_hastalik(), hasta1.get_tedavi()],
            [hasta2.get_ad(), hasta2.get_soyad(), None, None, None, None, None, None, None, hasta2.get_hasta_no(), hasta2.get_dogum_tarihi(), hasta2.get_hastalik(), hasta2.get_tedavi()],
            [hasta3.get_ad(), hasta3.get_soyad(), None, None, None, None, None, None, None, hasta3.get_hasta_no(), hasta3.get_dogum_tarihi(), hasta3.get_hastalik(), hasta3.get_tedavi()],
        ]

        columns = ['Ad', 'Soyad', 'Departman', 'Maaş', 'Uzmanlik', 'Deneyim Yili', 'Hastane', 'Çalişma Saati', 'Sertifika', 'Hasta No', 'Doğum Tarihi', 'Hastalik', 'Tedavi']
        df = pd.DataFrame(data, columns=columns)

        # Boş olan değişken değerleri için 0 atama
          
        print("Boş olan değişken değerleri için 0 atandi:")
        print(df, "\n")

        # Doktorlari uzmanlik alanlarina göre gruplandirarak toplam sayisini hesaplama
        doktor_grup = df[df['Uzmanlik'] != 0].groupby('Uzmanlik').size()
        print("Doktorlari uzmanlik alanlarina göre gruplandirarak toplam sayisi:")
        print(doktor_grup, "\n")

        # 5 yildan fazla deneyime sahip doktorlarin toplam sayisini bulma
        deneyimli_doktorlar = df[(df['Deneyim Yili'] > 5) & (df['Deneyim Yili'] != 0)].shape[0]
        print(f"5 yildan fazla deneyime sahip doktor sayisi: {deneyimli_doktorlar}\n")

        # Hasta adina göre DataFrame’i alfabetik olarak siralama
        df_hasta_sirali = df[df['Hasta No'] != 0].sort_values(by='Ad')
        print("Hasta adina göre alfabetik olarak siralanmiş DataFrame:")
        print(df_hasta_sirali, "\n")

        # Maaşi 7000 TL üzerinde olan personelleri bulma
        yuksek_maasli_personel = df[df['Maaş'] > 7000]
        print("Maaşi 7000 TL üzerinde olan personeller:")
        print(yuksek_maasli_personel, "\n")

        # Doğum tarihi 1990 ve sonrasi olan hastalari gösterme
        df['Doğum Tarihi'] = pd.to_datetime(df['Doğum Tarihi'], errors='coerce')
        yeni_hastalar = df[df['Doğum Tarihi'].dt.year >= 1990]
        print("Doğum tarihi 1990 ve sonrasi olan hastalar:")
        print(yeni_hastalar, "\n")

        # Var olan DataFrame’den istenen bilgileri içeren yeni bir DataFrame elde etme
        yeni_df = df[['Ad', 'Soyad', 'Departman', 'Maaş', 'Uzmanlik', 'Deneyim Yili', 'Hastalik', 'Tedavi']]
        print("Yeni DataFrame:")
        print(yeni_df)

    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    main()
