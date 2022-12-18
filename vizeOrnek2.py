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
    Seçiminiz:"""))

def veriGiris() :
    ad.append(input("İsim Giriniz: "))
    vn1 = int(input("Vize Notu Giriniz : "))
    vn.append(vn1)
    fn1= int(input("Final Notu Giriniz :"))
    fn.append(fn1)
    bn.append(vn1*.4+fn1*.6)

def adArama() :
    arananAd= input("Aranacak ismi giriniz: ")
    indis= ad.index(arananAd)
    print("Adınız:", ad[indis])
    print("Vize notunuz:", vn[indis])
    print("Final notunuz:", fn[indis])
    print("Başarı notunuz:", bn[indis])

def adDüzeltme() :
    arananAd = input("Düzeltilecek isim giriniz: ")
    indis= ad.index(arananAd)
    ad[indis]=input("Yeni isim giriniz:")
    vn1=int(input("Yeni Vize Notu Giriniz"))
    vn[indis]=vn1
    fn1=int(input("Yeni final notu giriniz:"))
    fn[indis]=fn1
    bn[indis]=vn1*0.4+fn1*0.6

def adSilme() :

    silinenAd= input("Silinecek isim giriniz: ")
    indis = ad.index(silinenAd)
    ad.remove(indis)
    vn.remove(indis)
    fn.remove(indis)
    bn.remove(indis)

def veriListeleme() :

    for i in range(len(ad)):
        print("Adınız:",ad[i])
        print("Vize notunuz:", vn[i])
        print("Final notunuz:", fn[i])
        print("Başarı notunuz:", bn[i])
        print("-"*30)
def enBuyukler(notlar) :
    enb=notlar[0]
    for i in range(1, len(notlar)):
        if  notlar[i] > enb:
            enb = notlar[i]
    return enb


def Ortalamalar(notlar):
    nt=0
    for i in range(len(notlar)):
        nt+=notlar[i]
    return nt

while True:
    menu=menuIslem()
    if menu==1:
        veriGiris()
    elif menu==2:
        adArama()
    elif menu==3:
        adDüzeltme()
    elif menu==4:
        adSilme()
    elif menu==5:
        veriListeleme()

    elif menu==6:
        enbvn=enBuyukler(vn)
        enbfn = enBuyukler(fn)
        enbbn = enBuyukler(bn)
        print("En büyük vize notu : {}\nFinal notu : {}\nBaşarı Notu : {}".format(enbvn,enbfn,enbbn))
    elif menu==7:
        vnt=Ortalamalar(vn)
        fnt=Ortalamalar(fn)
        bnt=Ortalamalar(bn)
        print("Vize Not ortalaması {0}\nFinal Not ort : {1}\nBaşarı Not ort{2}".format((vnt/len(ad)),(fnt/len(ad)),(bnt/len(ad))))

    elif menu==8:
        print("Program Bitti")
        exit(0)
    else:
        print("Yanlış menü değeri")

