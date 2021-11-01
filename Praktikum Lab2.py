print ("==========Mencari Bilangan Terbesar Dari Tiga Bilangan==========")
bilangan1 = int(input("Masukkan Bilangan 1:"))
bilangan2 = int(input("Masukkan Bilangan 2:"))
bilangan3 = int(input("Masukkan Bilangan 3:"))

if(bilangan1>bilangan2>bilangan3) :
    print ("Bilangan Pertama adalah Bilangan Terbesar")
elif (bilangan1<bilangan2>bilangan3) :
    print ("Bilangan Kedua adalah Bilangan Terbesar")
else:
    print ("Bilangan Ketiga adalah Bilangan Terbesar")


