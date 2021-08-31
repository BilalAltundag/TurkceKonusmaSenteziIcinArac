from string import punctuation
import re
import glob
import os
import pickle
from tqdm import tqdm 

def dosya_oku(dosyaIsmi):
  """
      Okunacak dosyanın konumu verilince satirlari dondurur.

      @param string dosyaIsmi : Dosya konumu
      @return list : Dosyanin icindeki satirlar
  """
  dosyaOkuyucu = open(dosyaIsmi,'r',encoding='utf8',errors="ignore")
  satirlar = dosyaOkuyucu.readlines()        
  return satirlar
  dosyaOkuyucu.close()
  
def dosya_yaz(dosyaIsmi,liste):
  """
      Dosyanın yazılacagi konumu ve liste verilince dosyayi kaydeder.
      
      @param string dosyaIsmi : Dosya konumu
      @param list liste : Dosyaya yazilacak satirlar listesi 
  """
  with open(dosyaIsmi,'w',encoding='utf8',errors="ignore") as filehandle:
    for listitem in liste:
        if listitem[-1] != "\n":
            filehandle.write('%s\n' % listitem)
        else:
            filehandle.write('%s' % listitem)
  filehandle.close()        

def on_isleme(dosya):
  """
    Verilen dosyayi noktalama işaretlerini,sayilari kaldirir ve 
    cümleleri belirleyip liste olarak geri dondurur.

    @param list dosya : Dosyaya yazilacak satirlar listesi
    @return list : Duzenlenmis satirlarin listesi
  """
  alfabe = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz '+'\n'
  cumleler = ''.join(dosya)
  cumleler = re.sub(r"\n", "  ", cumleler)
  cumleler = re.sub(r"  ", " ", cumleler)
  cumleler = re.split('[.!?]', cumleler)
  for i in range(len(cumleler)):
        cumleler[i] = re.sub(r"Â", "A", cumleler[i])
        cumleler[i] = re.sub(r"â", "a", cumleler[i])
        cumleler[i] = re.sub(r"Î", "I", cumleler[i])
        cumleler[i] = re.sub(r"î", "ı", cumleler[i])
        cumleler[i] = re.sub(r"Û", "U", cumleler[i])
        cumleler[i] = re.sub(r"û", "u", cumleler[i])
        cumleler[i] = ''.join([x for x in cumleler[i] if x not in punctuation and x not in '\n' and not x.isdigit() and x in alfabe and x != ""])
        cumleler[i] = cumleler[i].strip()
  cumleler = [x for x in cumleler if x != '']
  return cumleler

def uclu_kontrol(uclu):
    """
      Verilen uclulerin anlamsiz olanlari false olarak geri dondurur.
  
      @param string uclu : Bir ses uclusu
      @return boolean : Gecerli bir ucluyse True,degilse False
    """
    sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
    kontrol = []
    for i in uclu:
        if i not in sessiz_harfler:
            kontrol.append(True)
        else:
            kontrol.append(False)
    if kontrol[0]==kontrol[1] and kontrol[0]==kontrol[2] and kontrol[1]==kontrol[2]:
        return False
    else:
        return True
    
def uclu_sayisi():
    """
      Kullanicidan kac tane uclu kullanmak isticegini geri dondurur.
  
      @return int : Kullanıcıdan aldıgı cevap
    """
    kullanici_girdi = int(input("Kac tane üclü kullanmak istediginizi giriniz:"))
    return kullanici_girdi

def butun_ikililer():
    """
      Turkcedeki butun ikilileri liste olarak geri dondurur.
  
      @return list : Turkce alfabesinde harflerle yapilabilecek butun sess ikili listesi
    """
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    ikililer = []
    for i in alfabe:
        for j in range(len(alfabe)):
            ikililer.append(i+alfabe[j])
    return ikililer
def dict_siralama(dic):
    """
      Verilen dict turunu degerlere gore siralayip geri dondurur.
      
      @param dict dic : Herhangi bir sozluk
      @return dict : Sozlugun value ya göre siralanmis sekli
    """
    sirala = sorted(dic, key=dic.get, reverse=True)
    sirali_ucluler = {}
    for i in sirala:
      x = {i : dic[i]}
      sirali_ucluler.update(x) 
    return sirali_ucluler 
    
dosyalar = glob.glob(fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\Kullanilacak_Kitaplar\*.txt")
dosyalar = [isim for isim in dosyalar if ".txt" in isim and "_duz.txt" not in isim]# '.txt' uzantili dosyalarin isimlerini dosyalar a esitler.
#Verilen dosyalari on isleme sokarak '_duz.txt' olarak kaydeder. 
for dosyaIsmi in dosyalar:
  ism = dosyaIsmi.replace(chr(92),"/")
  data = dosya_oku(ism)
  yeni_dosya = on_isleme(data)
  isim =dosyaIsmi.split('.txt')[0]
  dosya_yaz(str(isim)+'_duz.txt',yeni_dosya)    

dosyalar_duz = glob.glob(fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\Kullanilacak_Kitaplar\*_duz.txt")# '_duz.txt' uzantili dosyalarin isimlerini dosyalar_duz e esitler.
ucluler = {}
butun_cumleler = []
#Duzenlenmis dosyalardaki butun ucluleri ucluler degiskenine esitler
with open(fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\Kullanilacak_Kitaplar\Butun_Ucluler.data", 'wb') as filehandle:
    for isimler in dosyalar_duz:
      dosyaOkuyucu = dosya_oku(isimler)
      butun_cumleler += dosyaOkuyucu
      for sat in dosyaOkuyucu:
        for j in range(len(sat)-2):
          uclu = sat[j]+sat[j+1]+sat[j+2]
          uclu = uclu.lower()
          if uclu_kontrol(uclu) and ' ' not in uclu:         
              if uclu in ucluler.keys():
                x = {uclu : ucluler[uclu]+1}
                ucluler.update(x)
              else:
                y = {uclu : 1}
                ucluler.update(y)
    pickle.dump(ucluler, filehandle)
filehandle.close() 

pickle_ucluler = pickle.load( open( fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\Kullanilacak_Kitaplar\Butun_Ucluler.data", "rb" ) )
sirali_ucluler = dict_siralama(pickle_ucluler)#Butun ucluleri degerlerine gore siralar
  
print(str(len(ucluler))," tane uclu bulunmaktadir.")
secilen_ucluler = dict(list(sirali_ucluler.items())[0: uclu_sayisi()])#Kullanicidan ne kadar uclu sayisi kullanıcagini secer
#105 harften az ve 15 harften cok sayida olan butun cumleleri alir
butun_cumleler = [cumle for cumle in butun_cumleler if len(cumle)<105 and len(cumle) > 15]

skorlar = {}
sirali_butun_cumleler = []
#Kac tane okunacak cümle istediğinizi giriniz:
cümle_sayisi = 100 
#Cumleler arasindan cumle_sayisi kadar en iyi skora gore siralar
for i in tqdm(range(cümle_sayisi)):
    sayac = 0
    en_yuksek_skor = 0
    silinecek_ucluler = set()
    indeks = 0
    for cumle in butun_cumleler:
        top_uclu = 0
        ucluler = set()
        cumle = " "+cumle+" "
        #Siralanan uclulerden cumlenin icinde ucluler listesine ekler
        for harf in range(len(cumle)-2):
            uclu = cumle[harf]+cumle[harf+1]+cumle[harf+2]
            if uclu in secilen_ucluler:
                ucluler.add(uclu)
            if ' ' not in uclu or harf==0 or harf==len(cumle)-3:
                top_uclu +=1
        sec_uclu = len(ucluler)
        #En yuksek skorda olan cumleyi bulur
        if (sec_uclu/top_uclu) > en_yuksek_skor:
            en_yuksek_skor = (sec_uclu / top_uclu)
            silinecek_ucluler.clear()
            silinecek_ucluler.update(ucluler)
            indeks = sayac
        sayac+=1 
    #En yuksek skor olan cumledeki ucluleri siler
    for j in silinecek_ucluler:
        secilen_ucluler.pop(j)
    sirali_butun_cumleler.append(butun_cumleler[indeks])
    butun_cumleler.pop(indeks)#En yuksek skor olan cumleyi butun cumlelerden siler
#Okuncak butun cumleleri dosyaya yazar
dosya_yaz(fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\Okunacak_Cumleler\Okunacak_cumleler.txt",sirali_butun_cumleler)       


ikili_dict = {}
for i in butun_ikililer():
    x = {i:0}
    ikili_dict.update(x)
#Okunacak cumledeki ikilileri , butun ikililerde bularak sayar     
for cumle in dosya_oku(fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\Okunacak_Cumleler\Okunacak_cumleler.txt"):
    for harf in range(len(cumle)-1):
        ikili = cumle[harf]+cumle[harf+1]
        ikili = ikili.lower()
        for ikililer in butun_ikililer():
            if ikili in ikililer:
                y = {ikili:ikili_dict[ikili]+1}    
                ikili_dict.update(y)
ikili_dict = dict_siralama(ikili_dict)#Degerlere gore ikilileri siralar

olmayan_ikililer = []
#Okunacak cumlelerde bulunmayan ikilileri olmayan_ikililer e ekler
for key,value in ikili_dict.items():
  if value == 0:
    olmayan_ikililer.append(key)

sozcukler = dosya_oku(fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\\butun_kelimeler.txt") #Turkcede bulunan kelimelerin bir listesi olan dosyayi okur

yeni_sozcukler = []
ek_sozcukler = []
#Olmayan ikilileri olusturmak icin sozcukler listesindeki kelimeleri yan yana getirerek elde eder
for ikili in tqdm(olmayan_ikililer):
  sayac_bir = 0
  sayac_iki = 0
  kelimelik_bir = ""
  kelimelik_iki = ""
  for ind,kelime in enumerate(sozcukler):
    kelime = kelime[:-1]
    if (sayac_bir + sayac_iki) < 2:
      #Ikilinin ikinci harfi ile kelimenin ilk harfi ayni ise ekler
      if kelime[0] == ikili[1] and sayac_bir == 0:
        kelimelik_iki = kelime + kelimelik_iki
        ek_sozcukler.append(kelime) 
        sozcukler.remove(sozcukler[ind])
        sayac_bir += 1
      #Ikilinin birinci harfi ile kelimenin ikinci harfi ayni ise ekler ve 
      #ayni kelimeler olmasin diye ek_sozcuklere ekleyip sozcukler den siliyoruz
      if kelime[-1] == ikili[0] and sayac_iki == 0:
        kelimelik_bir += kelime
        ek_sozcukler.append(kelime)
        sozcukler.remove(sozcukler[ind])
        sayac_iki += 1
      #Eger farkli sozcuk bulamazsa ek_sozcuklerden bulur
      if ind == len(sozcukler)-1 and (kelimelik_bir == "" or kelimelik_iki == ""):
        for ek in ek_sozcukler:
          if ek[0] == ikili[1] and sayac_bir == 0:
            kelimelik_iki = ek + kelimelik_iki
            sayac_bir += 1
          if ek[-1] == ikili[0] and sayac_iki == 0:
            kelimelik_bir += ek
            sayac_iki += 1
  yeni_sozcukler.append(kelimelik_bir +" "+kelimelik_iki)
  
#ikililerden sonu 'ğ' olan sozcukleri siler
for indeks,deger in enumerate(olmayan_ikililer):
  if deger[-1] == "ğ":
    olmayan_ikililer.remove(olmayan_ikililer[indeks])
    yeni_sozcukler.remove(yeni_sozcukler[indeks])

#Olmayan ikilileri de olusturdugumuz cumleleri okunacak cumlelere ekliyoruz
with open(fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\Okunacak_Cumleler\Okunacak_cumleler.txt", 'a',encoding='utf8',errors="ignore") as file:
    for listitem in yeni_sozcukler:
      file.write('%s\n' % listitem)
file.close()      