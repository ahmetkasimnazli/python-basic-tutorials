isim =[]
vn=[]
fn=[]
bn=[]

def menuIslem():
    return int(input("""
    1-Kayıt Giriş
    2-Listeleme
    3-Ortalamalar
    4-En Büyükler
    5-En Küçük Başarı ve Kime Ait
    6-İsim Arama
    7-İsim ile düzeltme
    8-İsim ile silme
    9-Çıkış
    Seçiminiz:"""))
def veriGiris():
    isim.append(input("İsim Giriniz"))
    vn1 = int(input("Vize Notu Giriniz : "))
    vn.append(vn1)
    fn1 = int(input("Final Notu Giriniz : "))
    fn.append(fn1)
    bn.append(vn1 * .4 + fn1 * .6)

def veriGoruntule():
    for i in range(len(isim)):
        print("Adınız : ",isim[i])
        print("Vize Notunuz : ", vn[i])
        print("Final Notunuz : ", fn[i])
        print("Başarı Notunuz : ", bn[i])
        print("-" * 30)

def ortalama(notlar):
    nt=0
    for i in range(len(notlar)):
        nt +=notlar[i]
    return nt

def enBuyuk(notlar):
    enb=notlar[0]
    for i in range(1, len(notlar)):
        if notlar[i] > enb:
            enb = notlar[i]
    return enb
def enKucuk():
    enkbn=bn[0]
    for i in range(1,len(isim)):
        if bn[i] < enkbn:
            enkbn = bn[i]
    indis = bn.index(enkbn)
    print("En küçük başarı notu",enkbn)
    print("Adınız: ",isim[indis])
    print("Vize Notunuz : ", vn[indis])
    print("Final Notunuz : ", fn[indis])
    print("Başarı Notunuz : ", bn[indis])
while True:
    menu=menuIslem()
    if menu == 1:
        veriGiris()
    elif menu==2:
        veriGoruntule()
    elif menu==3:
        vnt=ortalama(vn)
        fnt=ortalama(fn)
        bnt=ortalama(bn)
        print("Vize Not ortalaması {0}\nFinal not ort: {1}\nBaşarı Not ort {2}".format((vnt/len(isim)),(fnt/len(isim)),(bnt/len(isim))))
    elif menu== 4:
        enbvn=enBuyuk(vn)
        enbfn=enBuyuk(fn)
        enbbn=enBuyuk(bn)
        print("En büyük vize notu : {}\nFinal notu : {}\nBaşarı notu : {}".format(enbvn,enbfn,enbbn))
    elif menu==5:
        enKucuk()
    elif menu==6:
        print("Program bitti")
        exit(0)
    else:
        print("Yanlış menü değeri")
