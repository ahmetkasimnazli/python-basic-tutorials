#Kişinin adı cinsiyeti yaşı maaşı girip
# 1-Kayıt Giriş
# 2-Arama
# 3-Düzeltme
# 4-Silme
# 5-Listeleme
# 6-En Büyükler
# 7-Ortalamalar
# 8-Çıkış
ad=[]
cinsiyet=[]
maas=[]

def menuIslem():
    return int(input("""
    1-Kayıt Giriş
    2-Arama
    3-Düzeltme
    4-Silme
    5-Listeleme
    6-En Büyükler
    7-Ortalamalar
    8-Çıkış
    Seçiminiz: """))

def veriGiris():
    ad.append(input("İsminizi giriniz: "))
    cinsiyet.append(input("Cinsiyetinizi giriniz: "))
    maas.append(input("Maaşınızı giriniz: "))

def isimArama():
    arananAd=(input("Aranacak ismi giriniz: "))
    indis=ad.index(arananAd)
    print("İsim: ",ad[indis])
    print("cinsiyet: ", cinsiyet[indis])
    print("maas: ", maas[indis])

def isimDuzeltme():
    arananAd=input("Düzeltilecek ismi giriniz: ")
    indis=ad.index(arananAd)
    ad[indis]=input("İsminizi giriniz: ")
    cinsiyet[indis]=input("Cinsiyetinizi giriniz: ")
    maas[indis]=input("Maaşınızı giriniz: ")

def isimSilme():
    arananAd=input("Silinecek ismi giriniz: ")
    indis=ad.index(arananAd)
    ad[indis].remove
    cinsiyet[indis].remove
    maas[indis].remove

def listeleme():
    for i in range(len(ad)):
        print("İsim: ", ad[i])
        print("cinsiyet: ", cinsiyet[i])
        print("maas: ", maas[i])
        print("-"*30)

def enBuyuk(maas):
    ebm=maas[0]
    for i in range(1,len(ad)):
        if maas[i] > ebm:
            ebm=maas[i]
    return ebm

def ortalama(maas):
    nt=0
    for i in range(1,len(ad)):
        nt+=maas[i]
    return nt

while True:
    menu=menuIslem()

    if menu==1:
        veriGiris()
    elif menu==2:
        isimArama()
    elif menu==3:
        isimDuzeltme()
    elif menu==4:
        isimSilme()
    elif menu==5:
        listeleme()
    elif menu==6:
        ebm=enBuyuk(maas)
        print("En büyük maas: ",ebm)
    elif menu == 7:
        ort = ortalama(maas)
        print("Maas ortalaması: ", ort/len(maas))
    elif menu==8:
        print("Program bitti")
        exit(0)
    else:
        print("Yanlış değer")