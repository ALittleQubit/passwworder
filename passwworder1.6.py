from random import *
from operator import itemgetter
from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
import math
import hashlib
import os.path
from pathlib import Path
import re
from pathlib import PurePosixPath
m1 = ""
m2 = ""
l1 = 0
l2 = 0
l3 = 0
n=0 # 106 symb
mmm = ""
symdecode=["1","2","3","4","5","6","7","8","9","0","!","@","$","%","^","&","*","(",")","-","=","_","+","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","ё","й","ц","у","к","е","н","г","ш","щ","з","х","ъ","ф","ы","в","а","п","р","о","л","д","ж","э","я","ч","с","м","и","т","ь","б","ю"]
symcode = ["4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","-","+","_","+","q","w","e","r","t","y","u","i","o","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","ё","й","ц","у","к","е","н","г","ш","щ","з","х","ъ","ф","ы","в","а","п","р","о","л","д","ж","э","я","ч","с","м","и","т","ь","б","ю","1","2","3"]
message3=""
ent = 0
def passwgen():
    global ent,label
    root = Tk()
    password=""
    l=0
    l2=0
    l3=0
    let="qwertyuiopasdfghjklzxcvbnm"
    root.title("passwworder 1.6 generate password")
    image4= tk.PhotoImage(file='log\\backgrounds\\ges.png')
    root.iconbitmap('log\\icos\\ges.ico')
    ent =Entry(root,width=50,font =("Arial", 10),bg="green",fg="black",textvariable=mmm)
    ent.pack ()
    ent.place(x=170, y=0)
    label=Label(root,text= "" ,font=("Verdana", 25 ), bg="grey", fg="black",justify=CENTER, width=25, height=3)
    label.pack(pady=10)
    label.place(x=0, y=300)
    buttoncopy=Button(root, text="copy", font=("Verdana", 10),bg="grey",padx="10",pady="20", command = copy)
    buttoncopy.pack()
    CheckVar3 = IntVar()
    CheckVar2 = IntVar()
    CheckVar1 = IntVar()
    root.geometry("500x600")
    C1 = Checkbutton(root, text = "russian", variable = CheckVar1, onvalue = 1, offvalue = 0,command = n1)
    C2 = Checkbutton(root, text = "numbers ", variable = CheckVar2, onvalue = 1, offvalue = 0,command = n2)
    C3 = Checkbutton(root, text = "!$%&()*+,-./:;<=>?@[\]^_`{|}~" , variable = CheckVar3, onvalue = 1, offvalue = 0,command = n3)
    buttongen=Button(root, text="generate", font=("Verdana", 30),bg="grey",padx="10",pady="20", command = gen)
    buttongen.pack()
    buttoncopy.place(x=170, y=20)
    C1.pack
    root.configure(background='red')
    C1.place(x=0, y=0)
    C2.pack
    C2.place(x=0, y=50)
    C3.pack
    C3.place(x=0, y=100)
    buttongen.place(x=150, y=200)
    root.mainloop()
def n1 ():
    global l1
    if l1==0:
        l1=1
    else:
        l1=0
def n2 ():
    global l2
    if l2==0:
        print("true")
        l2=1
    else:
        l2=0
    print(l2)
def n3 ():
    global l3
    if l3==0:
        l3=1
    else:
        l3=0
def gen ():
    global ru ,num,let,spsym ,password
    password=""
    let="qwertyuiopasdfghjklzxcvbnm"
    if l1==1:
       ru="йцукенгшщзхъфывапролджэячсмитьбю"
       print("true")
    else :
      ru=""
    if l2==1:
      num="1234567890"
      print("true")
    else :
      num=""
    if l3==1:
      spsym="!$%&()*+,-./:;<=>?@[\]^_`{|}~"
      print("true")
    else :
      spsym=""
      print("false")
    zl = ""
    zl = ent.get()
    nzl= eval(zl)
    let =let+ru+num+spsym
    print (let)
    for i in range (1,nzl+1):
        sv = randrange(0,(len(let)-1))
        password = password +let[sv]
    label.config(text = password)
def copy():
    boot.clipboard_clear()
    boot.clipboard_append(password)
def cnd() :
    global message1,message2,en,en1,a1,n,my_file,messagenam,ennam
    message1 = ""
    message2 = ""
    messagenam = ""
    update = Tk()
    update.title("passwworder 1.6 create data")
    image3= tk.PhotoImage(file='log\\backgrounds\\ges.png')
    update.iconbitmap('log\\icos\\ges.ico')
    update.configure(background='orange')
    update.geometry("500x200")
    update.configure(background="bisque")
    update.title("")
    
    en = Entry(update,font=("Verdana", 15 ), bg="silver", fg="black",textvariable=message1)
    en.pack()
    en1 = Entry(update,font=("Verdana", 15 ), bg="silver", fg="black",textvariable=message2)
    en1.pack()
    ennam = Entry(update,font=("Verdana", 15 ), bg="silver", fg="black",textvariable=messagenam)
    ennam.pack()
    en.insert(0, "Name")
    en1.insert(0, "Password")
    ennam.insert(0, "Save as")
    bz= Button(update, text="save", font=("Verdana", 10),bg="grey",padx="10",pady="20", command = cndu)
    bz.pack()
def rnd () :
    global message3,en2
    lk = Tk()
    en2 = Entry(lk,font=("Verdana", 15 ), bg="silver", fg="black",textvariable=message3)
    en2.pack()
    btn1 = Button (lk, text="read", font=("Verdana", 10),bg="grey",padx="10",pady="20", command = ready)
    btn1.pack()
def ready () :
    global ld,ld1,rom,m1,m2
    a3 = en2.get()
    n= a3
    print(n)
    os.renames('log\\'+str(n)+'.acc', 'log\\'+str(n)+'.acc.txt')
    f = open('log\\'+str(n)+'.acc.txt', 'r', encoding='utf-8')
    ld = f.readline()
    ld1 = f.readline()
    for j in range (0,len(ld) ):
          for i in range (1,106):
             if ld[j] == symcode[i]:
                 m1 = m1 + symdecode[i]
                 i = 106
    for j in range (0,len(ld1) ):
          for i in range (1,106):
             if ld1[j] == symcode[i]:
                 m2 = m2 + symdecode[i]
                 i = 106
    f.close()
    rom = Tk()
    rom.configure(background='green')
    rom.title("passwworder 1.6 load data")
    image2= tk.PhotoImage(file='log\\backgrounds\\ges.png')
    rom.iconbitmap('log\\icos\\ges.ico')
    name = Label(rom,text = m1)
    pas = Label(rom,text = m2)
    name.pack()
    pas.pack()
    nb = Button(rom, text="copy name", font=("Verdana", 10),bg="grey",padx="10",pady="20", command = copyn)
    pb = Button(rom, text="copy password", font=("Verdana", 10),bg="grey",padx="10",pady="20", command = copyp)
    nb.pack()
    pb.pack()
    os.renames('log\\'+str(n)+'.acc.txt', 'log\\'+str(n)+'.acc')
def copyn () :
    boot.clipboard_clear()
    boot.clipboard_append(ld)
def copyp () :
    boot.clipboard_clear()
    boot.clipboard_append(ld1)    
def  cndu () :
    global m1,m2
    a1 = en.get()
    a2 = en1.get()
    an = ennam.get()
    an = str(an)
    print(an)
    f = open('log\\'+str(an)+'.acc.txt',"a")
    f.close()
    f = open('log\\'+str(an)+'.acc.txt', 'w', encoding='utf-8')
    for j in range (0,len(a1) ):
          for i in range (1,106):
             if a1[j] == symdecode[i]:
                 m1 = m1 + symcode[i]
                 i = 106
    for j in range (0,len(a2) ):
          for i in range (1,106):
             if a2[j] == symdecode[i]:
                 m2 = m2 + symcode[i]
                 i = 106
    f.write(str(m1))
    f.write ("\n")
    f.write(str(m2))
    f.close()
    os.renames('log\\'+str(an)+'.acc.txt', 'log\\'+str(an)+'.acc')
    m1 =""
    m2 = ""
boot = Tk()
boot.title("passwworder 1.6")
boot.configure(background='red')
image= tk.PhotoImage(file='log\\backgrounds\\ges.png')
boot.iconbitmap('log\\icos\\ges.ico')
panel1 = tk.Label(boot, image=image)
panel1.pack(side='top', fill='both', expand='yes')
panel1.image = image
photo1= PhotoImage (file='log\\images\\one.png')
photo2= PhotoImage (file='log\\images\\owo.png')
photo3= PhotoImage (file='log\\images\\ohree.png')
bupg = Button(boot,image=photo2,bg="grey",padx="10",pady="20", command = passwgen)
bupg.pack()
cnd = Button(boot,image=photo1,bg="grey",padx="10",pady="20", command = cnd)
cnd.pack()
rnd = Button(boot,image=photo3,bg="grey",padx="10",pady="20", command = rnd)
rnd.pack()
boot.mainloop()
