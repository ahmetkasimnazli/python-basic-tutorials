print('a' in 'merhaba')
print('er' in 'merhaba')
print('f' in 'merhaba')
liste=[1,3,5,7,9,11]
print("listeniz: ",liste)
toplam=0
for eleman in liste:
    print(eleman,end="\t")
    toplam+=eleman
print("\nSayıların toplamı : ",toplam)
isim="Ayten"
for karakter in isim:
    print(karakter*3)