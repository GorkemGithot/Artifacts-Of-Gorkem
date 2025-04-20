import customtkinter as tk
from tkinter import filedialog
import aspose.words as aw
from aspose.words import Document
import random
import time
import sqlite3 as sql
import random

conn=sql.connect("veri8.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS RECORDS(
               record text,
               ad text,
               soyad text
               )""")
randomNumber=0
theUserName=""
theUserSurName=""

def new_window():
    def destroyer():
        new_window.destroy()
        new_window.update()
        time.sleep(0.4)
        root.deiconify()
        root.update()
        time.sleep(0.4)
    new_window=tk.CTkToplevel(root)
    new_window.title("WATERMARK AUTOMATION MENU")
    new_window.geometry("400x160")
    new_window.resizable(False,False)
    frame1=tk.CTkFrame(master=new_window)
    frame1.pack(fill=tk.BOTH, expand=True)
    button1=tk.CTkButton(master=frame1,
                  text="DOSYA OLUSTURMAK ICIN TIKLAYIN",
                  width=100,
                  command=lambda: [buttonFunc(), destroyer()])
    button1.pack(padx=5, pady=12)

    button2=tk.CTkButton(master=frame1,
                    text="ISME GORE ARAMA ICIN TIKLAYIN",
                    width=225,
                    command=lambda: [buttonFunc8(), destroyer()])
    button2.pack(padx=5, pady=12)

    button3=tk.CTkButton(master=frame1,
                    text="SOYADA GORE ARAMA ICIN TIKLAYIN",
                    width=225,
                    command=lambda: [buttonFunc9(), destroyer()])
    button3.pack(padx=5, pady=12)
    
def terminateRanditFunc():
    mylist=[]
    randomNumber=""
    for a in range(10):
        x=random.randint(0,9)
        mylist.append(x)
    for a in mylist:
        randomNumber+=str(a)
    return randomNumber


def checkerFromFile(randomNumber,theUserName,theUserSurName):
    conn=sql.connect("veri8.db")
    cursor=conn.cursor()
    cursor.execute("""SELECT record from RECORDS""")
    list1=cursor.fetchall()
    result = [record[0] for record in list1]
    count=0
    for a in result:
        if(a==randomNumber):
            count+=1
    if(count!=0):
        conn.commit()
        conn.close()
        return False
    else:
        addcommand="""INSERT INTO RECORDS VALUES (?,?,?)"""
        data=(randomNumber,theUserName,theUserSurName)
        cursor.execute(addcommand,data)
        conn.commit()
        conn.close()
        return True


def initializerDocx(createdNumber,nameDoc,pathOfDoc):
    doc = Document()
    options = aw.TextWatermarkOptions()
    options.font_family = "Arial"
    options.font_size = 120
    options.layout = aw.WatermarkLayout.DIAGONAL
    options.is_semitrasparent = True
    doc.watermark.set_text(createdNumber, options)
    doc.save(f"{pathOfDoc}/{nameDoc}.docx")


def buttonFunc8():
    button1.configure(state="normal")
    button1.update()
    input1.configure(state="normal")
    input1.update()
    etiket.configure(text="Aratmak istediğiniz adı girin ...")
    etiket.update()
    button1.configure(text="DEVAM ETMEK ICIN TIKLAYIN",command=searchAdFunc)
    button1.update()
    
    
def buttonFunc9():
    button1.configure(state="normal")
    button1.update()
    input1.configure(state="normal")
    input1.update()
    etiket.configure(text="Aratmak istediğiniz soyadı girin ...")
    etiket.update()
    button1.configure(text="DEVAM ETMEK ICIN TIKLAYIN",command=searchSoyAdFunc)
    button1.update()

def searchAdFunc():
    theUserName1=input1.get()
    input1.delete(0, tk.END)
    conn=sql.connect("veri8.db")
    cursor=conn.cursor()
    cursor.execute("""SELECT * from RECORDS""")
    list1=cursor.fetchall()
    etiket.configure(text="")
    new_list=[]
    re=""
    if " " in theUserName1:
        b=theUserName.split(" ")
        for a in b:
            a=a.capitalize()
            re+=a
            re+=" "
        re=re.rstrip()
        my_input2=theUserName1.upper()
        my_input3=theUserName1.lower()
        new_list.append(re) 
        new_list.append(my_input2)
        new_list.append(my_input3)
        
    else:
        my_input1=theUserName1.capitalize()
        my_input2=theUserName1.upper()
        my_input3=theUserName1.lower()
        
        new_list.append(my_input2)
        new_list.append(my_input3)
        new_list.append(my_input1)
    temp=0
    for i in list1:
        for a in new_list:
            if(i[1]==a):
                temp+=1
                print(new_list)
                txt="{0} {1} {2}".format(i[0],i[1],i[2])
                print(txt)
                etiket.configure(text=etiket.cget("text")+"\n"+txt)
                etiket.update()
                continue
    if(temp==0):
        etiket.configure(text="Eşleşme yok...")
        etiket.update() 
    button1.configure(text="ANA MENUYE DONMEK ICIN TIKLAYIN",state="normal",command=lambda: [new_window(),root.withdraw()])
    button1.update()

def searchSoyAdFunc():
    theUserSurName1=input1.get()
    input1.delete(0, tk.END)
    conn=sql.connect("veri8.db")
    cursor=conn.cursor()
    cursor.execute("""SELECT * from RECORDS""")
    list1=cursor.fetchall()
    etiket.configure(text="")
    new_list=[]
    re=""
    if " " in theUserSurName1:
        b=theUserName.split(" ")
        for a in b:
            a=a.capitalize()
            re+=a
            re+=" "
        re=re.rstrip()
        my_input2=theUserSurName1.upper()
        my_input3=theUserSurName1.lower()
        new_list.append(re) 
        new_list.append(my_input2)
        new_list.append(my_input3)
        
    else:
        my_input1=theUserSurName1.capitalize()
        my_input2=theUserSurName1.upper()
        my_input3=theUserSurName1.lower()
        
        new_list.append(my_input2)
        new_list.append(my_input3)
        new_list.append(my_input1)
    temp=0
    for i in list1:
        for a in new_list:
            if(i[2]==a):
                temp+=1
                print(new_list)
                txt="{0} {1} {2}".format(i[0],i[1],i[2])
                print(txt)
                etiket.configure(text=etiket.cget("text")+"\n"+txt)
                etiket.update() 
                time.sleep(0.2)
                continue
    if(temp==0):
        etiket.configure(text="Eşleşme yok...")
        etiket.update() 
        time.sleep(0.2)
    button1.configure(text="ANA MENUYE DONMEK ICIN TIKLAYIN",state="normal",command=lambda: [new_window(),root.withdraw()])
    button1.update()
    time.sleep(0.2)
    
def buttonFunc():
    button1.configure(state="normal")
    button1.update()
    input1.configure(state="normal")
    input1.update()
    etiket.configure(text="Adınızı girin...")
    etiket.update()
    button1.configure(text="DEVAM ETMEK ICIN TIKLAYIN",command=buttonFunc4)
    button1.update()

def buttonFunc4():
    theUserName1=input1.get()
    input1.delete(0, tk.END)
    global theUserName
    theUserName=theUserName1
    etiket.configure(text=etiket.cget("text")+"\nSoyadınızı girin...")
    etiket.update()
    button1.configure(text="DEVAM ETMEK ICIN TIKLAYIN",command=buttonFunc5)
    

def buttonFunc5():
    theUserSurName1=input1.get()
    input1.delete(0, tk.END)
    global theUserSurName
    theUserSurName=theUserSurName1
    button1.configure(state="disabled")
    button1.update()
    time.sleep(0.2)
    etiket.configure(text="Rastgele sayı oluşturuluyor...")
    etiket.update()
    time.sleep(0.4)
    global randomNumber
    randomNumber=terminateRanditFunc()
    etiket.configure(text=etiket.cget("text")+"\nRastgele sayı oluşturuldu...")
    etiket.update()
    time.sleep(0.4)
    etiket.configure(text=etiket.cget("text")+"\nSayının varlığı kontrol ediliyor...")
    etiket.update()
    time.sleep(0.4)
    if(checkerFromFile(randomNumber,theUserName,theUserSurName)):
        etiket.configure(text=etiket.cget("text")+"\nSayı veritabanına kayıt edildi...")
        etiket.update()
        time.sleep(0.4)
    else:
        etiket.configure(text=etiket.cget("text")+"\nSayı saptandı...")
        etiket.update()
        time.sleep(0.4)    
    button1.configure(state="normal")
    button1.update()
    input1.configure(state="normal")
    input1.update()
    etiket.configure(text=etiket.cget("text")+"\nDosyaya isim girin ve butona tıklayın...")
    etiket.update()
    time.sleep(0.4)
    button1.configure(text="DOSYA ADI OLUŞTURUN VE TIKLAYIN",command=buttonFunc2)

def buttonFunc2():
    button1.configure(state="disabled")
    button1.update()
    input1.configure(state="disabled")
    input1.update()
    time.sleep(0.4)
    theRealName=input1.get()
    input1.delete(0, tk.END)
    button1.configure(state="disabled")
    button1.update()
    etiket.configure(text=etiket.cget("text")+"\nİşlem gerçekleştiriyor...")
    etiket.update()
    time.sleep(0.4)
    etiket.configure(text=etiket.cget("text")+"\nLütfen bir dizin seçin...")
    etiket.update()
    time.sleep(0.4)
    input1.configure(state="disabled")
    pathOfDoc = filedialog.askdirectory() 
    try:  
        initializerDocx(randomNumber, theRealName, pathOfDoc)
        etiket.configure(text="\nİşlem gerçekleştirildi ve dosya oluşturuldu...\nUygulamayı kapatabilirsiniz...")
        etiket.update()
        time.sleep(0.4)
        button1.configure(text="ANA MENUYE DONMEK ICIN TIKLAYIN",state="normal",command=lambda: [new_window(),root.withdraw()])
        button1.update()
        time.sleep(0.4)
    except:
        etiket.configure(text=etiket.cget("text")+"\nDosya kaydedilmedi, işlem iptal edildi.")
        etiket.update()
        time.sleep(0.4)
        
    



    
tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")
root=tk.CTk()
root.withdraw()
root.geometry("400x350")
root.title("WATERMARK AUTOMATION")
root.resizable(False,False)
frame=tk.CTkFrame(master=root)
frame.pack(fill=tk.BOTH, expand=True)
etiket = tk.CTkLabel(master=frame,
                     height=150,
                  text="Başlatılmayı bekliyor...")
etiket.pack(padx=10, pady=5)
input1=tk.CTkEntry(master=frame,
                width=270,
                state="disabled")

input1.pack(padx=5,pady=7)
button1=tk.CTkButton(master=frame,
                  text="DEVAM ETMEK ICIN TIKLAYIN",
                  width=100,
                  command=buttonFunc)
button1.pack(padx=10, pady=5)
new_window()
root.mainloop()