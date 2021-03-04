from textblob import TextBlob
import webbrowser
import datetime
from math import *
from gtts import gTTS
from playsound import playsound
import random
import os

def speak(string):
       try:
              tts = gTTS(string,lang='tr')
              rand = random.randint(1,100000)
              file = "ses-"+str(rand)+".mp3"
              tts.save(file)
              playsound(file)
              os.remove(file)
       except ValueError:
              pass

islemler = ["a","m","s","h","l","k","n","hm","ç","t","y","w"]
while True:     
       print("""
--------------------------
Asistana Hoşgeldiniz
Arama Yapmak için 'A' yı 
Müzik Açmak İçin 'M' yi
Saati Sormak iiçin 'S' yi 
Hava Durumu İçin 'H' yi 
Lig Maçları İçin 'L' yi 
Kapatmak İçin 'K' yi
Navigasyon İçin 'N' yi
Takvim İçin 'T' yi
Çeviri Yapmak İçin 'Ç' yi
Hesap Makinesi İçin 'HM' yi
Youtube İçin 'Y' yi
Wikipedia İçin 'W' yi
Discord İçin 'D' yi
       Tuşlayınız
--------------------------
""")
       speak("Ne Yapmak İstersiniz")
       islem = str(input("Ne Yapmak İstersiniz: "))
       islem = islem.lower()
       if islem == 'a':
              speak("Ne Aramak İstersiniz")
              ara = (input("Ne Aramak İstersiniz "))
              url = "https://www.google.com/search?q=" + ara
              webbrowser.get().open(url)
              speak(ara + "için bulduklarım") 
       
       elif islem == 'm' :
              ac = input("Spotify mı Yotube Müzik mi (Spotify için s Youtube Müzik için ym): ").lower()
              if ac == "s":
                     webbrowser.open("https://accounts.spotify.com/tr/login/?continue=https:%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect&_locale=tr-TR")

              if ac == "ym":
                     webbrowser.open("https://music.youtube.com")
               
       elif islem == 's' :
              an = datetime.datetime.now()
              tarih = datetime.datetime.ctime(an)
              print(tarih)
                             
       elif islem == 'h':
              speak("Hangi İlde Bulunmaktasınız")
              il = input("Hangi İlde Bulunmaktasınız: ")
              url_a = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=" + il
              webbrowser.get().open(url_a)
               
       elif islem == 'l' :
              webbrowser.open("https://www.tff.org/default.aspx?pageID=198")
             
       elif islem == 'k':
              speak("Görüşmek üzere")
              exit()

       elif islem == 'n':
              webbrowser.open("https://www.google.com/maps/dir///@39.0876459,35.1777724,6z?hl=tr")       
       
       elif islem == 't':
              webbrowser.open("http://takvim.ufgu.com/")

       elif islem == 'ç':
              while True:
                     print("""
              ----------------------
              Türkçe-Almanca İçin A
              Türkçe-İngilizce İçin E
              Türkçe-Fransızca İçin F
              Almanca-Türkçe İçin AT
              İngilizce-Türkçe İçin İT
              Fransızca-Türkçe İçin FT
              Kaptmak İçin K
              ----------------------
              """)
              
                     cevir_3 = input("Hangi Dili İstiyorsunuz: ")
                     cevir_3 = cevir_3.lower()

                     if cevir_3 == "a" :
                            cevir = TextBlob(str(input("Türkçe Metin Giriniz: ")))
                            cevir_2=cevir.translate(to="de")
                            print(cevir_2)

                     elif cevir_3 == "e" :
                            cevir = TextBlob(str(input("Türkçe Metin Giriniz: ")))
                            cevir_2=cevir.translate(to="en")
                            print(cevir_2)
              
                     elif cevir_3 == "f" :
                            cevir = TextBlob(str(input("Türkçe Metin Giriniz: ")))
                            cevir_2=cevir.translate(to="fr")
                            print(cevir_2)

                     elif cevir_3 == "at" :
                            cevir = TextBlob(str(input("Almanca Metin Giriniz: ")))
                            cevir_2=cevir.translate(from_lang="de",to="tr")
                            print(cevir_2)
              
                     elif cevir_3 == "it" :
                            cevir = TextBlob(str(input("İngilizce Metin Giriniz: ")))
                            cevir_2=cevir.translate(from_lang="en",to="tr")
                            print(cevir_2)
              
                     elif cevir_3 == "ft" :
                            cevir = TextBlob(str(input("Fransızca Metin Giriniz: ")))
                            cevir_2=cevir.translate(from_lang="fr",to="tr")
                            print(cevir_2)

                     elif cevir_3 == 'k':
                            break
                            

       elif islem == 'y':
              aranacak=str(input("Ne Aramak İstiyorsunuz?:"))
              webbrowser.open("https://www.youtube.com/results?search_query={}".format(aranacak))

       elif islem == "w":
              aranacak=(str(input("Ne Aramak İstiyorsunuz?:")))
              webbrowser.open("https://tr.wikipedia.org/w/index.php?search={}&title=%C3%96zel%3AAra&go=Git".format(aranacak))

       elif islem == "d":
              webbrowser.open("https://discord.com/login")

       elif islem == "hm" :
              def toplama(a,b):
                     print(a+b)
              def cikarma(a,b):
                     print(a-b)
              def carpma(a,b):
                     print(a*b)
              def bolme(a,b):
                     x = (a / b)
                     print("{0:.5f}".format(x)) #sonucu x'e atıp virgülden sonraki 5 hanesini yazdırmak için
              def üsalma(a,b):
                     print(a**b)
              secimler = ["toplama","çıkarma","çarpma","bölme","üsalma","kökalma"]
              while True:
                     secim = input("Seçenekler: toplama, çıkarma, çarpma, bölme, üsalma, kökalma -> ")
                     print(secim)
              
                     if secim == "toplama":
                            a = float(input("İlk sayı: "))
                            b = float(input("İkinci sayı: "))
                            (toplama(a,b))
                     
                     
                     elif secim == "çıkarma":
                            a = float(input("İlk sayı: "))
                            b = float(input("İkinci sayı: "))
                            (cikarma(a,b))
                     
                     
                     elif secim == "çarpma":
                            a = float(input("İlk sayı: "))
                            b = float(input("İkinci sayı: "))
                            (carpma(a,b))
                     
                     
                     elif secim == "bölme":
                            a = float(input("İlk sayı: "))
                            b = float(input("İkinci sayı: "))
                            (bolme(a,b))
                     
              
                     elif secim == "üsalma":
                            a = float(input("Taban: "))
                            b = float(input("Üs: "))
                            (üsalma(a,b))
                     
              
                     elif secim == "kökalma":
                            sayı = float(input("Sayı Giriniz: "))
                            derece = float(input("Kök Derecesini Giriniz:"))
                            hesaplama = pow(sayı,1/derece)
                            print(hesaplama)
                     else:
                            print("Hatalı giriş yaptınız")
                            break
                     break
       else:
              speak("""
       Yanlış Değer Girdiniz Kapatılıyor
       Lütfen Yeniden Başlatın
       """)
              exit()





















