ad=[]
cinsiyet=[]
yas=[]
maas=[]

def menuIslem():
    return int(input("""
    1-Kayıt Giriş
    2-İsim Arama
    3-İsim ile düzeltme
    4-İsim ile silme
    5-Listeleme
    6-Erkeklerin yaş ort
    7-En Büyükler
    8-Ortalamalar
    9-Çıkış
    Seçiminiz:"""))

def veriGiris():
    ad.append(input("İsim Giriniz"))
    cinsiyet1 = int(input("Cinsiyetinizi Giriniz : "))
    cinsiyet.append(cinsiyet1)
    yas1 = int(input("Yaşınızı Giriniz : "))
    yas.append(yas1)
    bn.append(vn1 * .4 + fn1 * .6)
