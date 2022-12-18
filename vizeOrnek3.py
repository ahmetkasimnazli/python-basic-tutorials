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
vn=[]
fn=[]
bn=[]

def menuIslem() :
    return int(input("""
    1-Kayıt Giriş
    2-Arama
    3-Düzeltme
    4-Silme
    5-Listeleme
    7-En Büyükler
    8-Ortalamalar
    9-Çıkış
    Seçiminiz: """))

def veriGiris():
    ad.append(input("İsim giriniz: "))
    vn1=int(input("Vize notunuzu giriniz: "))
    vn.append(vn1)
    fn1 = int(input("Final notunuzu giriniz: "))
    fn.append(fn1)
    bn.append(vn1*.4+fn1*.6)

def adArama():
    arananAd=input("Aranacak adı giriniz: ")
    indis=ad.index(arananAd)
    print("İsim: ",ad[indis])
    print("Vize not: ", vn[indis])
    print("Final not: ", fn[indis])
    print("Başarı not: ", bn[indis])

def adDuzeltme():
    arananAd=input("Aranacak adı giriniz: ")
    indis=ad.index(arananAd)
    ad[indis]=input("Yeni isim giriniz: ")
    vn1 =int(input("Yeni vize notu giriniz: "))
    vn[indis]=vn1
    fn1 = int(input("Yeni final notu giriniz: "))
    fn[indis] = fn1
    bn[indis] = vn1*.4+fn1*.6

def adSilme():
    silinenAd=input("Silinecek adı giriniz: ")
    indis=ad.index(silinenAd)
    ad.remove(indis)
    vn.remove(indis)
    fn.remove(indis)
    bn.remove(indis)

def listeleme():
    for i in range(len(ad)):
        print("İsim: ", ad[i])
        print("Vize not: ", vn[i])
        print("Final not: ", fn[i])
        print("Başarı not: ", bn[i])
        print("-"*30)


while True:
    menu=menuIslem()
    if menu==1:
        veriGiris()
    elif menu==2:
        adArama()
    elif menu==3:
        adDuzeltme()
    elif menu==4:
        adSilme()
    elif menu==5:
        listeleme()
    elif menu==8:
        print("Program bitti")
        exit(0)









