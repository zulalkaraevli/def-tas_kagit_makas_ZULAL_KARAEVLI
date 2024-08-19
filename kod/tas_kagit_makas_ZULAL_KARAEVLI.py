# Oyunda; tas, kagit, makas sembolleri su sekilde kullanilir :tas, makasi kirar.makas, kağidi keser.kağit, tasi sarar.
# Oyunun turları 3 secenekten olusur: Oyuncu kazanabilir, bilgisayar kazanabilir veya beraberlik olabilir.
# Eger oyundan cikmak isterseniz 'q' tusuna basiniz.
# İlk iki turu kazanan oyunu kazanır yani 20 puana ulaşan oyunun galibi olur.
# kazanan olduktan sonra oyun biter eger oyuna hem siz hem de bilgisayar devam etmek isterse yeni bir oyuna baslarsiniz.




import random
oyun_sayisi = 0 # oyun sayısını tutmak için bir değişken tanımladık



def tas_kagit_makas_ZULAL_KARAEVLI():
     global oyun_sayisi # global değişken tanımladık
     oyun_sayisi += 1 # her oyun başladığında oyun sayısını 1 arttırıyoruz
     print(f"Oyun Sayisi: {oyun_sayisi}") # oyun sayısını ekrana yazdırıyoruz
         
     kullanici_puan = 0
     bilgisayar_puan = 0
     tur_sayisi = 0
     oyun_sayisi = 0
     
    
    

     while True:
        oyun = ["tas", "kagit", "makas"] 
        bilgisayar_tercihi =["evet" , "hayir"]

        kullanici = input("tas, kagit, makas? (Oyundan cikmak icin 'q' tuşuna basin): " )
        
        if kullanici == 'q':  
            print("Oyun sonlandirildi.")  
            break

        if kullanici not in oyun:  
            print("Geçersiz bir seçim yaptiniz. Lütfen tekrar deneyin.")
            continue

        bilgisayar = random.choice(oyun)  
        

        if kullanici == bilgisayar:
            print("Berabere kaldiniz! Her iki kisi de puan alamadi.")
        elif kullanici == "tas":
            if bilgisayar == "kagit":
                bilgisayar_puan += 10
                print("Kagit tasi sarar, bilgisayar 10 puan kazandi.")
            else:
                kullanici_puan += 10
                print("Tas makasi kirar, kullanici 10 puan kazandi.")
        elif kullanici == "makas":
            if bilgisayar == "tas":
                bilgisayar_puan += 10
                print("Tas makasi kirar, bilgisayar 10 puan kazandi.")
            else:
                kullanici_puan += 10
                print("Makas kagidi keser, kullanici 10 puan kazandi.")
        elif kullanici == "kagit":
            if bilgisayar == "makas":
                bilgisayar_puan += 10
                print("Makas kagidi keser, bilgisayar 10 puan kazandi.")
            else:
                kullanici_puan += 10
                print("Kagit tasi sarar, kullanici 10 puan kazandi.")
        else:
            print("Gecersiz bir değer girdiniz.")
        
        print(f"Bilgisayar puani: {bilgisayar_puan}, Kullanici puani: {kullanici_puan}")
        tur_sayisi += 1
        print("tur_sayisi : ", tur_sayisi)

        if bilgisayar_puan >= 20 or kullanici_puan >= 20:
          break
     if bilgisayar_puan > kullanici_puan:
        print("Kazanan: Bilgisayar")
     elif bilgisayar_puan == kullanici_puan:
        print("Berabere! Ayni puana sahipsiniz.")
     else:
        print("Kazanan: Kullanici")

     oyun_sayisi += 1
     bilgisayar_tercihi = random.choice(bilgisayar_tercihi)
     print("bilgisayar oyuna devam etmek istiyor mu? : " , bilgisayar_tercihi)
     devam_etmek = input("Oyuna devam etmek istiyor musunuz? (Evet icin 'e', Hayir için 'h'): ")
     if bilgisayar_tercihi == "evet" :
        if devam_etmek.lower() == 'e':
            print("yeni oyuna basliyorsunuz") 
            tas_kagit_makas_ZULAL_KARAEVLI()
        else :print("Oyun sonlandirildi.")
     else: print("Oyun sonlandirildi.")
tas_kagit_makas_ZULAL_KARAEVLI()