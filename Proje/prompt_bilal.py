import os
import sounddevice as sd
from scipy.io.wavfile import write
import tkinter 

pencere = tkinter.Tk()
pencere.title("Ses Kaydedici")
pencere.configure(background = "Yellow")

sayac = 0

#Dosya okuma
dosya =fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\Okunacak_Cumleler\Okunacak_cumleler.txt"
dosyaOkuyucu = open(dosya,'r',encoding='utf8',errors="ignore")
cumleler = dosyaOkuyucu.readlines()        
dosyaOkuyucu.close()

def ses_kaydet():
    global sayac
    global cumlem
    cumle = cumlem["text"]
    her_harf_saniye = 0.2
    Fs = 44100
    d = len(cumle)*her_harf_saniye
    a = sd.rec(int(d*Fs),Fs,1)
    sd.wait()
    newpath = fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\\kayitlar" 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    isim = fr"C:\Users\{os.getlogin()}\\Desktop\\Proje\\kayitlar\\"+str(sayac+1)+".ncı_cumle"
    write(isim+".wav",Fs,a) 
def cumle_degistir():
    global cumlem
    global sayac
    sayac = int(ent_temperature.get())-1
    #(sayac)
    cumle_sayisi["text"] = str(sayac+1)+chr(92)+str(len(cumleler))
    cumlem["text"] = cumleler[sayac]
def ileri_git():
    global sayac 
    global cumlem
    sayac += 1
    if sayac >= len(cumleler):
        sayac = 0
    cumle_sayisi["text"] = str(sayac+1)+chr(92)+str(len(cumleler))
    cumlem["text"] = cumleler[sayac]
def geri_git():
    global sayac 
    global cumlem
    sayac -= 1 
    if sayac < 0:
        sayac = len(cumleler)-1
    cumle_sayisi["text"] = str(sayac+1)+chr(92)+str(len(cumleler))
    cumlem["text"] = cumleler[sayac]

cumlem = tkinter.Label(pencere , text = cumleler[sayac],bg="grey",fg="blue")
cumlem.grid(row = 1 , column = 3)

cumle_sayisi = tkinter.Label(pencere , text = str(sayac+1)+chr(92)+str(len(cumleler)),bg="grey",fg="blue")
cumle_sayisi.grid(row = 1 , column = 1)

ent_temperature = tkinter.Entry(pencere, width=10)
ent_temperature.grid(row=3, column=1, sticky="e") 
      
degistir = tkinter.Button(pencere , text = "Cumleye Git",command=cumle_degistir,fg="white",bg="black")
degistir.grid(row = 2 , column = 1)

ileri = tkinter.Button(pencere , text = ">>",command=ileri_git,fg="white",bg="black")
ileri.grid(row = 2 , column = 4)

geri = tkinter.Button(pencere , text = "<<",command=geri_git,fg="white",bg="black")
geri.grid(row = 2 , column = 2)

kaydet_butonu = tkinter.Button(pencere , text = "Kaydet",command=ses_kaydet,fg="white",bg="black")
kaydet_butonu.grid(row = 2 , column = 3)

cıkıs = tkinter.Button(pencere , text = "Cikis",command=pencere.quit,fg="white",bg="black")
cıkıs.grid(row = 1 , column = 7)

pencere.mainloop()
