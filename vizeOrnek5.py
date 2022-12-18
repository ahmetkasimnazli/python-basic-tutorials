#Kişinin adı cinsiyeti yaşı maaşı girip
# 1-Kayıt Giriş
# 2-Arama
# 3-Düzeltme
# 4-Silme
# 5-Listeleme
# 7-En Büyükler
# 8-Ortalamalar
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
    6-En Büyükler
    7-Ortalamalar
    8-Çıkış
    Girdiğiniz değer: """))

def veriGiris():
    ad.append(input("İsminizi giriniz: "))
    vn1=int(input("Vize notunuzu giriniz: "))
    vn.append(vn1)
    fn1=int(input("Final notunuzu giriniz: "))
    fn.append(fn1)
    bn.append(vn1*0.4+fn1*0.6)

def isimArama():
    aranacakAd=input("Aranacak adı giriniz: ")
    indis=ad.index(aranacakAd)
    print("Ad: ",ad[indis])
    print("VN: ", vn[indis])
    print("FN: ", fn[indis])
    print("BN: ", bn[indis])

def isimDuzeltme():
    aranacakAd=input("Aranacak adı giriniz: ")
    indis = ad.index(aranacakAd)
    ad[indis]=input("Yeni ad giriniz: ")
    vn[indis] = int(input("Yeni VN giriniz: "))
    vn1=vn[indis]
    fn[indis] = int(input("Yeni FN giriniz: "))
    fn1 = fn[indis]
    bn[indis] = (vn1*0.4+fn1*0.6)

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
    for i in range(len(ad)):
        if  notlar[i] > enb:
            enb=notlar[i]

    return enb

def ortalamalar(notlar):
    nt=0
    for i in range(len(ad)):
        if notlar[i] > nt:
            nt+=notlar[i]

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
        vn1=enBuyuk(vn)
        fn1=enBuyuk(fn)
        bn1=enBuyuk(bn)
        print("En büyük vn{0}\nEn büyük fn{1}\nEn büyük bn{2}".format(vn1,fn1,bn1))
    elif menu==7:
        vn1 = ortalamalar(vn)
        fn1 = ortalamalar(fn)
        bn1 = ortalamalar(bn)
        print("vn ort:{0}\nfn ort:{1}\nbn ort:{2}".format(vn1/len(ad), fn1/len(ad), bn1/len(ad)))
    elif menu==8:
        print("Program bitti")
        exit(0)
    else:
        print("Yanlış değer")
