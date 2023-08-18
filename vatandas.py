# Quartzz <3


import random
import time

i = 0

print("----------------------------")
print("Qua Vatandaş Yönetim Sistemi")
print("----------------------------")
time.sleep(1)

secim = input("""[1] - Vatandaş Ekle
[2] - Vatandaş Sil
[3] - Uygulamadan Çık """)

secim = int(secim)

if secim == 1:
    i=1
elif secim == 2:
    i=2
elif secim == 3:
    print("Programdan Çıkış Yaptınız . .")
else:
    print("Yanlış Giriş Yaptınız")



def parse_date(date_str):
    day, month, year = map(int, date_str.split('/'))
    return day, month, year


def VatandasEkle():
    isim = input("Vatandaşın İsmini Giriniz : ")
    time.sleep(1)
    soyisim = input("Vatandaşın Soy İsmini Giriniz : ")
    time.sleep(1)
    yas = input("Vatandaşın Yaşını Giriniz : ")   
    yas = int(yas)
    time.sleep(1)
    dogusTarih = input("Lütfen tarihi (gün/ay/yıl) formatında giriniz: ")
    day, month, year = parse_date(dogusTarih)
    time.sleep(1)
    sehir = input("Vatandaşın İkamet Ettiği Şehri Giriniz : ")
    time.sleep(1)
    semt = input("Vatandaşın İkamet Ettiği Semti Giriniz : ")
    time.sleep(1)
    mahalle = input("Vatandaşın İkamet Ettiği Mahalleyi Giriniz : ")
    time.sleep(1)
    sokak = input("Vatandaşın İkamet Ettiği Sokağı Giriniz : ")

    kimlikIlk3 = random.randint(99,1000)     # Kimliğin İlk 3 Hanesi
    kimlikSon4 = random.randint(1000,10000)     # Kimliğin Son 4 Hanesi

    kimNo = str(kimlikIlk3)+"-"+str(kimlikSon4)

    vatandasInfo = f"{isim},{soyisim},{yas},{day}/{month}/{year},{sehir},{semt},{mahalle},{sokak},{kimNo}\n"

    # Veriyi dosyaya yazma
    with open("vatandas_bilgileri.txt", "a") as dosya:
        dosya.write(vatandasInfo)
        print("Vatandaş Eklendi . .")
        i = 0
    
    
def VatandasSil():
    silinecekKimlik = input("Silinecek vatandaşın kimlik numarasını giriniz: ")

    yeni_veri = []
    with open("vatandas_bilgileri.txt", "r") as dosya:
        for satir in dosya:
            if silinecekKimlik not in satir:
                yeni_veri.append(satir)

    with open("vatandas_bilgileri.txt", "w") as dosya:
        dosya.writelines(yeni_veri)

    print("Vatandaş silindi.")
    i = 0


while i == 1:
    VatandasEkle()
while i == 2:
    VatandasSil()
    
