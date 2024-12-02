import tkinter as tk
from spire.doc import *
from spire.doc.common import *
import random
import time

randomNumber=0
def terminateRanditFunc():
    mylist=[]
    randomNumber=""
    for a in range(10):
        x=random.randint(0,9)
        mylist.append(x)
    for a in mylist:
        randomNumber+=str(a)
    return randomNumber


def checkerFromFile(randomNumber):
    list1=list()
    with open(r"D:\PYHTON\StajProjesi\records.txt","r") as myFile:
        list1=myFile.readlines()
    count=0
    while True:
        for a in list1:
            a=a.rstrip("\n")
            if(a==randomNumber):
                count+=1
        if(count!=0):
            return False
        else:
            with open("D:\\PYHTON\\StajProjesi\\records.txt","a") as myFile:  
                myFile.write(randomNumber)
                myFile.write("\n")
            return True


def initializerDocx(createdNumber, nameDoc):
    
        document = Document()
        txtWatermark = TextWatermark()
        txtWatermark.Text = createdNumber
        txtWatermark.FontSize = 120
        txtWatermark.Color = Color.get_Red()
        txtWatermark.Layout = WatermarkLayout.Diagonal
        
        document.Watermark = txtWatermark
        document.SaveToFile(f"{nameDoc}.docx", FileFormat.Docx2016)
        document.Close()

def buttonFunc2():
    theRealName=input1.get()
    button1.config(state="disabled")
    button1.update()
    time.sleep(1)
    etiket.config(text=etiket.cget("text")+"\nİşlem gerçekleştiriyor...")
    etiket.update()
    time.sleep(1)
    input1.config(state="disabled")
    initializerDocx(randomNumber,theRealName)
    etiket.config(text=etiket.cget("text")+"\nİşlem gerçekleştirildi ve dosya oluşturuldu...")
    etiket.update()
    time.sleep(1)
    


def buttonFunc():
    etiket.config(text="Rastgele sayı oluşturuluyor...")
    etiket.update()
    time.sleep(1)
    global randomNumber
    randomNumber=terminateRanditFunc()
    etiket.config(text=etiket.cget("text")+"\nRastgele sayı oluşturuldu...")
    etiket.update()
    time.sleep(1)
    etiket.config(text=etiket.cget("text")+"\nSayının varlığı kontrol ediliyor...")
    etiket.update()
    time.sleep(1)
    if(checkerFromFile(randomNumber)):
        etiket.config(text=etiket.cget("text")+"\nSayı veritabanına kayıt edildi...")
        etiket.update()
        time.sleep(1)
    else:
        etiket.config(text=etiket.cget("text")+"\nSayı saptandı...")
        etiket.update()
        time.sleep(1)
    input1.config(state="normal")
    button1.config(text="DOSYAYA OLUSTURMAK ICIN TIKLAYIN",command=buttonFunc2)
    button1.update()
    time.sleep(1)
    etiket.config(text=etiket.cget("text")+"\nDosyaya isim girin ve butona tıklayın...")
    etiket.update()
    time.sleep(1)
    

root=tk.Tk()
root.geometry("728x500")
root.title("WATERMARK AUTOMATION")

etiket=tk.Label(root,
                text="Başlatılmayı bekliyor...",
                bg="white",
                fg="black",
                height=20,
                justify="left",
                width=100,
                )

etiket.grid(row=0, column=0, padx=10, pady=2)

input1=tk.Entry(root,
                width=100,
                state="disabled")

input1.grid(row=1,column=0,padx=10,pady=2)



button1=tk.Button(root,
                  text="BASLATMAK ICIN TIKLAYIN",
                  bg="white",
                  fg="black",
                  height=5,
                  width=30,
                  command=buttonFunc)
button1.grid(row=3, column=0, padx=10, pady=15)


root.mainloop()