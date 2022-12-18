
def yaziYaz():#ne veri alır ne de değer gönderir
    print("okan üniversitesi")

yaziYaz()
yaziYaz()

def toplama(i,j):#parametre olarak veri alır
    print(i,"+",j,"=",(i+j))

toplama(3,5)
toplama("ali","veli")

def toplamSonuc(i,j):#parametre olarak veri alıp geriye değer götürür
    return i+j
i=3
j=5
print(i,"+",j,"=",toplamSonuc(i,j))