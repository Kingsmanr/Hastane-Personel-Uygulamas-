from Hemşire import Hemşire

# Hemşire nesnesi oluşturma
hemsire = Hemşire(
    personel_no=1,
    ad="Ayşe",
    soyad="Yılmaz",
    departman="Cerrahi",
    maas=5000,
    çalişma_saati=40,
    sertifika="İlk Yardım",
    hastane="Acıbadem Hastanesi"
)

# Hemşire bilgilerini yazdırma
print(hemsire)

# Getter metodu ile hemşire bilgilerini alma
bilgiler = hemsire.getter()
print("Bilgiler:", bilgiler)

# Setter metodu ile hemşire bilgilerini güncelleme
hemsire.setter()

# Güncellenmiş hemşire bilgilerini yazdırma
print("\nGüncellenmiş Bilgiler:")
print(hemsire)
