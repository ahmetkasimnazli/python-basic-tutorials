#Kişinin adı cinsiyeti yaşı maaşı girip
# 1-Kayıt Giriş
# 2-Arama
# 3-Düzeltme
# 4-Silme
# 5-Listeleme
# 6-En Büyükler
# 7-Ortalamalar
# 9-Çıkış

ad=[]
vn=[]
fn=[]
bn=[]

def menuIslem():
    return int(input("""
    1-Kayıt Giriş
    2-Arama
    3-Düzeltme
    4-Silme
    5-Listeleme
    7-En Büyükler
    8-Ortalamalar
    9-Çıkış
    Girdiğiniz değer: """))

def veriGiris():
    ad.append(input("Adınızı giriniz: "))
    vn1=int(input("Vize notu giriniz: "))
    vn.append(vn1)
    fn1=int(input("Final notu giriniz: "))
    fn.append(fn1)
    bn.append(vn1*.4+fn1*.6)

def isimArama():
    aranacakAd=input("Aranacak adı giriniz: ")
    indis=ad.index(aranacakAd)
    print("Ad: ",ad[indis])
    print("VN: ", vn[indis])
    print("FN: ", fn[indis])
    print("BN: ", bn[indis])

def isimDuzeltme():
    aranacakAd = input("Aranacak adı giriniz: ")
    indis = ad.index(aranacakAd)
    ad[indis]=input("Yeni isim giriniz: ")
    vn[indis] = int(input("Yeni vn giriniz: "))
    vn1=vn[indis]
    fn[indis] = int(input("Yeni fn giriniz: "))
    fn1 = fn[indis]
    bn[indis] =vn1*.4+fn1*.6

def isimSilme():
    aranacakAd = input("Aranacak adı giriniz: ")
    indis = ad.index(aranacakAd)
    ad.pop(indis)
    vn.pop(indis)
    fn.pop(indis)
    bn.pop(indis)

def listeleme():
    for i in range(len(ad)):
        print("Ad: ", ad[i])
        print("VN: ", vn[i])
        print("FN: ", fn[i])
        print("BN: ", bn[i])
        print("-"*30)

def enBuyuk(notlar):
    enb=notlar[0]
    for i in range(1,len(ad)):
        if notlar[i]> enb:
            enb=notlar[i]
    return enb

def ortalama(notlar):
    nt=0
    for i in range(len(ad)):
        if notlar[i]> nt:
            nt+=notlar[i]
    return nt

while True:
    menu=menuIslem()

    if menu==1:
        veriGiris()
    elif menu==2 :
        isimArama()
    elif menu==3 :
        isimDuzeltme()
    elif menu==4 :
        isimSilme()
    elif menu==5 :
        listeleme()
    elif menu==6 :
        vn1=enBuyuk(vn)
        fn1 = enBuyuk(fn)
        bn1 = enBuyuk(bn)
        print("en büyük vn: {0}\nen büyük fn: {1}\nen büyük bn: {2}".format(vn1,fn1,bn1))
    elif menu==7 :
        vn1 = ortalama(vn)
        fn1 = ortalama(fn)
        bn1 = ortalama(bn)
        print("vize ortalama:{0}\nfinal ortalama:{1}\nbn ortalama:{2}".format(vn1/len(ad),fn1/len(ad),bn1/len(ad)))
    elif menu==8 :
        print("Program bitti")
        exit(0)
    else:
        print("Yanlış değer")
