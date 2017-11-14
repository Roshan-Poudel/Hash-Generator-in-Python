from tkinter import Button,Label,messagebox,Text,Entry,Tk
from tkinter import ttk
from tkinter import *
import hashlib,binascii
class Papu:
    def __init__(self, master):

        self.master = master
        master.title("A simple hash GUI developed by Roshan")

        self.label1=Label(master,text="Enter message here",font=14,activeforeground="red")
        self.label1.place(x=40,y=32)

        self.text1=Text(master,height=10,width=18,font=10)
        self.text1.place(x=40,y=60)

        self.button1=Button(master,text="Show_all_hash",font=20,bg="pink")
        self.button1.place(x=40,y=320)

        self.text2=Entry(master,width=96,font=15)
        self.text2.place(x=410,y=20)


        self.button3=Button(master,text="QUIT",font=20,padx=20,bg="red",pady=20,command=  master.quit)
        self.button3.place(x=55,y=460)

        self.button4 = Button(master, text="CLEAR FIELDS", font=20, padx=10, bg="deep sky blue", pady=10,command=self.clear)
        self.button4.place(x=40, y=390)

        self.button2=Button(master,text="MD_5",font=13,bg="deep sky blue",command=self.sha_224,padx=22)
        self.button2.place(x=280,y=25)

        self.button5=Button(master,text="SHA1",font=13,bg="deep sky blue",padx=22,command=self.sha1)
        self.button5.place(x=280,y=90)

        self.text3 = Entry(master, width=96, font=15)
        self.text3.place(x=410, y=90)

        self.button6 = Button(master, text="SHA2_224", font=13, bg="deep sky blue", padx=2, command=self.sha224)
        self.button6.place(x=280, y=150)

        self.text4 = Entry(master, width=96, font=15)
        self.text4.place(x=410, y=150)

        self.button7 = Button(master, text="SHA2_256", font=13, bg="deep sky blue", padx=2, command=self.sha256)
        self.button7.place(x=280, y=216)

        self.text5 = Entry(master, width=96, font=15)
        self.text5.place(x=410, y=216)

        self.button7 = Button(master, text="SHA2_384", font=13, bg="deep sky blue", padx=2,command=self.sha384 )
        self.button7.place(x=280, y=280)

        self.text6 = Entry(master, width=96, font=15)
        self.text6.place(x=410, y=280)

        self.button8 = Button(master, text="SHA3_224", font=13, bg="deep sky blue", padx=2, command=self.sha3_224)
        self.button8.place(x=280, y=350)

        self.text7 = Entry(master, width=96, font=15)
        self.text7.place(x=410, y=360)

        self.button9 = Button(master, text="SHA3_256", font=13, bg="deep sky blue", padx=2, command=self.sha3_256)
        self.button9.place(x=280, y=420)

        self.text8 = Entry(master, width=96, font=15)
        self.text8.place(x=410, y=425)

        self.button10= Button(master, text="SHA3_384", font=13, bg="deep sky blue", padx=2, command=self.sha3_384)
        self.button10.place(x=280, y=490)

        self.text9 = Entry(master, width=96, font=15)
        self.text9.place(x=410, y=490)
#
        self.button11 = Button(master, text="BLAKE_2b", font=13, bg="deep sky blue", padx=2,command=self.blake_2b)
        self.button11.place(x=20, y=626)

        self.text10 = Entry(master, width=124, font=15)
        self.text10.place(x=150, y=632)

        self.button12= Button(master, text="BLAKE_2s", font=13, bg="deep sky blue", padx=2, command=self.blake_2s)
        self.button12.place(x=280, y=570)

        self.text11 = Entry(master, width=96, font=15)
        self.text11.place(x=410, y=575)

        self.label11=Label(master,text="HASH GENERATOR by ==> Rosan",font=20)
        self.label11.place(x=590,y=700)

        self.po1=ttk.Progressbar(master,length = 570,mode="determinate")
        self.po1.start(200)
        self.po1.step(70000)
        self.po1.place(x=20,y=733)

        self.po2 = ttk.Progressbar(master, length=600,mode="determinate",style="red.Horizontal.TProgressbar", orient="horizontal")
        self.po2.start(200)
        self.po2.step(70000)
        self.po2.place(x=910, y=733)

    def sha_224(self):
        try:
             self.a1=hashlib.md5()
             self.a2=str(self.text1.get(1.0,200.0))
             self.r=self.a2.replace('\n','').encode('utf-8')
             self.r1=self.r
             self.a3=self.a1.update(self.r1)
             self.text2.insert(1, binascii.hexlify(self.a1.digest()))

        except Exception as e:
            messagebox.showinfo("Exception",e)

    def sha1(self):
        try:
             self.b1=hashlib.sha1()
             self.b2=str(self.text1.get(1.0,10000.0))
             self.b3=self.b2.replace('\n','').encode('utf-8')
             self.b4=self.b1.update(self.b3)
             self.text3.insert(1,binascii.hexlify(self.b1.digest()))
        except Exception as e:
            messagebox.showerror("EXCEPTION",e)

    def sha224(self):
        try:
            self.c1=hashlib.sha224()
            self.c2=str(self.text1.get(1.0,10000.0))
            self.c3=self.c2.replace('\n','').encode('utf-8')
            self.c4=self.c1.update(self.c3)
            self.text4.insert(1, binascii.hexlify(self.c1.digest()))
        except Exception as e:
            messagebox.showerror("EXCEPTION",e)

    def sha256(self):
        try:
            self.d1=hashlib.sha256()
            self.d2=str(self.text1.get(1.0,10000.0))
            self.d3=self.d2.replace('\n','').encode('utf-8')
            self.d4=self.d1.update(self.d3)
            self.text5.insert(1, binascii.hexlify(self.d1.digest()))
        except Exception as e:
            messagebox.showerror("EXCEPTION",e)




    def sha384(self):

        try:
            self.e1=hashlib.sha384()
            self.e2=str(self.text1.get(1.0,10000000.0))
            self.e3=self.e2.replace('\n','').encode('utf-8')
            self.e4=self.e1.update(self.e3)
            self.text6.insert(1, binascii.hexlify(self.e1.digest()))
        except Exception as e:
            messagebox.showerror("EXXCEPTION",e)

    def sha3_224(self):
        try:
            self.f1=hashlib.sha3_224()
            self.f2=str(self.text1.get(1.0,1000000000.0))
            self.f3=self.f2.replace('\n','').encode('utf-8')
            self.f4=self.f1.update(self.f3)
            self.text7.insert(1, binascii.hexlify(self.f1.digest()))
        except Exception as e:
            messagebox.showerror("EXCEPTION",e)

    def sha3_256(self):
        try:
            self.g1=hashlib.sha3_256()
            self.g2=str(self.text1.get(1.0,10000.0))
            self.g3=self.g2.replace('\n','').encode('utf-8')
            self.g4=self.g1.update(self.g3)
            self.text8.insert(1, binascii.hexlify(self.g1.digest()))
        except Exception as e:
            messagebox.showerror("EXCEPTION",e)

    def sha3_384(self):
        try:
            self.h1=hashlib.sha3_384()
            self.h2=str(self.text1.get(1.0,10000000.0))
            self.h3=self.h2.replace('\n','').encode()
            self.h4=self.h1.update(self.h3)
            self.text9.insert(1, binascii.hexlify(self.h1.digest()))
        except Exception as  e:
            messagebox.showerror("EXCEPTION",e)


    def blake_2b(self):
        try:
            self.i1=hashlib.blake2b()
            self.i2=self.text1.get(1.0,10000000000000000.0)
            self.i3=self.i2.replace('\n','').encode()
            self.i4=self.i1.update(self.i3)
            self.text10.insert(1, binascii.hexlify(self.i1.digest()))
        except Exception as e:
            messagebox.showerror("Exception",e)

    def blake_2s(self):
        try:
            self.j1 = hashlib.blake2s()
            self.j2 = self.text1.get(1.0, 10000000000000000.0)
            self.j3 = self.j2.replace('\n', '').encode()
            self.j4 = self.j1.update(self.j3)
            self.text11.insert(1, binascii.hexlify(self.j1.digest()))
        except Exception as e:
            messagebox.showerror("Exception", e)

    def clear(self):
        self.text2.delete(0,1000)
        self.text1.delete(1.0,1000.0)
        self.text3.delete(0,1000)
        self.text4.delete(0,10000)
        self.text5.delete(0, 10000)
        self.text6.delete(0, 10000)
        self.text7.delete(0, 10000)
        self.text8.delete(0, 10000)
        self.text9.delete(0, 10000)
        self.text10.delete(0, 10000)
        self.text11.delete(0, 10000)






root = Tk()
my_gui = Papu(root)
root.config(bg="cyan")
root.mainloop()

