# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:57:11 2023

@author: Acer Gorkem
"""

class Book:
    def __init__(self,name,author,publishing_house,category,floor,ISBN,location):
        
        self.name=name
        self.author=author
        self.publishing_house=publishing_house
        self.category=category
        self.ISBN=ISBN
        self.floor=floor
        self.location=location
        self.status_book="1"
    def show(self):
        print(self.name,self.author,self.publishing_house,self.category,self.floor,self.ISBN,self.location)
        





def object_entry():
    name=input("NAME: ")
    author=input("AUTHOR: ")
    publishing_house=input("PUBLISHING HOUSE: ")
    category=input("CATEGORY: ")
    ISBN=input("ISBN: ")
    floor=input("FLOOR: ")
    location=input("LOCATION: ")
    return Book(name,author,publishing_house,category,floor,ISBN,location)

def entering_system():
    how_many=int(input("HOW MANY BOOK WILL YOU ENTER? "))
    liste=[x for x in range(1,how_many+1)]
     
    for i in liste:
        obje=i
        obje=object_entry()
        writed=obje.name+","+obje.author+","+obje.publishing_house+","+obje.category+","+obje.floor+","+obje.ISBN+","+obje.location+","+obje.status_book
        
        with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","a") as file:
            file.write(writed)
            file.write("\n")
      


def monitoring_system(): 
    listem=["NAME","AUTHOR","PUBLISING HOUSE","CATEGORY","ISBN","FLOOR","LOCATION","STATUS_BOOK"]        
    with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","r") as file:
        all_lines=file.readlines()
    print()
    
    
    all_lines_2=[]
    for i in all_lines:
        a=i.split(",")
        all_lines_2.append(a)
    k=0  
    for i in all_lines_2:
        k=0
        for a in i:
           
               
               if "\n" not in a:
                   z=15-len(listem[k])
                   print(listem[k]," "*z,":",a,end="\n")
                   k+=1
               else:
                   new_a=a.rstrip("\n")
                   z=15-len(listem[k])
                   print(listem[k]," "*z,":",new_a)
                   print()
                   k+=1

def filtering():
    listem=["NAME","AUTHOR","PUBLISING HOUSE","CATEGORY","ISBN","FLOOR","LOCATION","BORROW_STATUS"]   
    my_input=input("PLEASE ENTER THE SEARCH KEY FOR FILTERING...  ")  
    print()
    new_list=[]
    my_input1=my_input.capitalize()
    my_input2=my_input.upper()
    my_input3=my_input.lower()
    
    new_list.append(my_input1)
    new_list.append(my_input2)
    new_list.append(my_input3)
    new_list.append(my_input)
    new_list_2=[]
    for a in new_list:
        if a not in new_list_2:
            new_list_2.append(a)
            
            
   
    
    with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","r") as file:
        all_lines=file.readlines()
    all_lines_2=[]
    for i in all_lines:
        a=i.split(",")
        all_lines_2.append(a)
    for i in all_lines_2:
        for a in i:
           for u in new_list_2:
                if u in a:
                    for k in range(len(i)):
                        z=15-len(listem[k])
                        print(listem[k]," "*z,":",i[k],end="\n")
   
def borrow_system():
    input1=input("PLEASE ENTER THE BARCODE OF THE BOOK... ")
    with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","r") as file:
        all_lines=file.readlines()
    all_lines_2=[]
    for i in all_lines:
        a=i.split(",")
        all_lines_2.append(a)
    temp=0
    for i in all_lines_2:
        temp=5
        if i[4]==input1:
            if "1\n" == i[7]:
                i[7]="0\n"
                
                print("""YOU TOOK THE BOOK THE PROCESS IS DONE...""")
            else :
                print("THIS BOOK IS ALREADY TAKEN")
                
        else:
            temp+=1
            
    if temp>=6:
        print("THE INPUT CAN BE WRONG PLEASE CHECK AGAIN ISBN OF THE BOOK. ")
    with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","w") as file:
        for line in all_lines_2:
            for a in line:
                if "\n" in a:
                    file.write(a)
                else:
                    file.write(a)
                    x=","
                    file.write(x)
                
          
    
def after_borrow():
    input1=input("PLEASE ENTER THE BARCODE OF THE BOOK... ")
    with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","r") as file:
        all_lines=file.readlines()
    all_lines_2=[]
    for i in all_lines:
        a=i.split(",")
        all_lines_2.append(a)
    temp=0
    for i in all_lines_2:
        temp=5
        if i[4]==input1:
            if "0\n" == i[7]:
                i[7]="1\n"
                
                print("""THE STATUS OF THE BOOK HAS BEEN CHANGED""")
        else:
            temp+=1
    if temp>=6:
        print("THE INPUT CAN BE WRONG PLEASE CHECK AGAIN ISBN OF THE BOOK. ")
            
    with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","w") as file:
        for line in all_lines_2:
            for a in line:
                if "\n" in a:
                    file.write(a)
                else:
                    file.write(a)
                    x=","
                    file.write(x)
    

            
                    
def type_ratios():
    dictionary={}
    with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","r") as file:
        all_lines=file.readlines()
    all_lines_2=[]
    for i in all_lines:
        a=i.split(",")
        all_lines_2.append(a)
    
    for i in all_lines_2:
        a=i[3]
        
        if a not in dictionary.keys():
            dictionary[a]=1
        else:
            dictionary[a]+=1
    for a in dictionary:
        
        z=15-len(a)
        print(a," "*z,end=": ")
        print(dictionary[a])
        
    

def last_five_book():  
    listem=["NAME","AUTHOR","PUBLISING HOUSE","CATEGORY","ISBN","FLOOR","LOCATION","STATUS_BOOK"]        
    with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","r") as file:
        all_lines=file.readlines()
    print()
    
    
    all_lines_2=[]
    for i in all_lines:
        a=i.split(",")
        all_lines_2.append(a)
    k=0  
    for i in all_lines_2[-1:-6:-1]:
        k=0
        for a in i:
           
               
               if "\n" not in a:
                   z=15-len(listem[k])
                   print(listem[k]," "*z,":",a,end="\n")
                   k+=1
               else:
                   new_a=a.rstrip("\n")
                   z=15-len(listem[k])
                   print(listem[k]," "*z,":",new_a)
                   print()
                   k+=1



def monitoring_borrowed():
    listem=["NAME","AUTHOR","PUBLISING HOUSE","CATEGORY","ISBN","FLOOR","LOCATION","STATUS_BOOK"]
    with open(r"C:\Users\Acer\Desktop\Baslksz_e-tablo_-_Sayfa1.csv","r") as file:
        all_lines=file.readlines()
    print()
    toplam=0
    all_lines_2=[]
    for i in all_lines:
        a=i.split(",")
        all_lines_2.append(a)
    for i in all_lines_2:
        toplam=0
        l=i[-1]
        if l=="0\n":
            
    
            k=0
            for a in i:
               
                   
                   if "\n" not in a:
                       z=15-len(listem[k])
                       print(listem[k]," "*z,":",a,end="\n")
                       k+=1
                   else:
                       new_a=a.rstrip("\n")
                       z=15-len(listem[k])
                       print(listem[k]," "*z,":",new_a)
                       print()
                       k+=1
        else:
            toplam+=1
    if toplam==0:
        print("THERE IS NO BORROWED BOOK")
        
    
        
        
         
while True:
    print("""

WELCOME TO LIBRARY AUTOMATION

**************************
1- New Book Entry
2- Monitoring Books
3- Borrow System
4- Analysis System

FOR EXIT PRESS 0
**************************""")
    print()
    my_input99=input("PLEASE ENTER THE NUMBER OF PROCESS... ")
    print()
    
    if my_input99=="0":
        print()
        print("PROGRAM HAS BEEN ENDED")
        
        break
                 
            
    if my_input99=="1":
        entering_system()
        continue
    if my_input99=="2":
        print()
        print()
        print("___________________________________________________________")
        print()
        print("""NOTE: 1 IS NOT BORROWED
      0 IS BORROWED
              
1- Observe every book with filtering
2- Observe every book """)
        print("___________________________________________________________")
        print()
        my1=input("PLEASE ENTER THE NUMBER OF PROCESS...")
        if my1=="1":
            filtering()
            continue
        if my1=="2":
            monitoring_system()
            continue
        else:
            print("INVALID PROCESS... ")
            continue
    if my_input99=="3":
        print("___________________________________________________________")
        print()
        print("""NOTE: 1 IS NOT BORROWED
      0 IS BORROWED
              
1- TO BORROW ANY BOOK
2- AFTER BORROWING""")
        print("___________________________________________________________")
        print()
        my2=input("PLEASE ENTER THE NUMBER OF PROCESS... ")
        if my2=="1":
            borrow_system()
            continue
        if my2=="2":
            after_borrow()
            continue
        else:
            print("INVALID PROCESS... ")
            continue
    if my_input99=="4":
        print("___________________________________________________________")
        print()
        print("""1- TO ACCESS TYPE RATIOS
2- TO OBSERVE LAST FIVE BOOK WHICH ARE ENTERED RECENTLY
3- TO OBSERVE BORROWED BOOKS""")
        print("___________________________________________________________")
        print()
        my3=input("PLEASE ENTER THE NUMBER OF PROCESS... ")
        if my3=="1":
            type_ratios()
            continue
        if my3=="2":
            last_five_book()
            continue
        if my3=="3":
            monitoring_borrowed()
            continue
        else:
            print("INVALID PROCESS... ")
            continue
        
        
        
        
        
        
        
        
        
    
            
     
    

       
