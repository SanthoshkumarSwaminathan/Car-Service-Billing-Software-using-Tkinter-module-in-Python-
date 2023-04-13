from tkinter import *
#from tkinter.ttk import *
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import pymysql
import tkinter.messagebox as MessageBox



class Bill(Frame):
    
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x600')
        self.root.title('car service billing software')
        self.bg = Pil_imageTk.PhotoImage(file = r"C:\Python311\backgroundcover.jpg")
  
        # Create Canvas
        self.canvas1 = Canvas( root, width = 1000,
                    height =600)
  
        self.canvas1.pack(fill = "both", expand = True)
  
        # Display image 
        self.canvas1.create_image( 0, 0, image = self.bg, 
                                anchor = "nw")

        def resizer(e):
    
            self.bg1 =Pil_image.open(r"C:\Python311\BG.PNG")    
            self.resized_bg = self.bg1.resize((e.width,e.height),Pil_image.LANCZOS)
            self.new_bg =Pil_imageTk.PhotoImage(self.resized_bg)
            self.canvas1.create_image( 0, 0, image =self.new_bg, 
                                anchor = "nw")      
        
        

          #-----------------VARIABLES---------------------
        self.CustomerName= StringVar()
        self.ContactNumber= StringVar()
        self.CarModel= StringVar()
        self.Kmsdriven= StringVar()
        self.Generalservice= IntVar()
        self.WaterWash= IntVar()
        self.Interiorcleaning= IntVar()
        self.Oilchange= IntVar()
        self.Paor= IntVar()
        self.Tinkering= IntVar()
        self.Painting= IntVar()
        self.Total=IntVar()
        

                #------------------LABEL-------------------------
        name=Label(self.root,text='CustomerName  :')
        name.place(x=50,y=50)
        contactnumber=Label(self.root,text='ContactNumber  :')
        contactnumber.place(x=530,y=50)
        car_model=Label(self.root,text='Car model      :')
        car_model.place(x=50,y=100)
        kms_driven=Label(self.root,text='Kms driven    :')
        kms_driven.place(x=530,y=100)
        label1= Label(self.root,text="General service                    :")
        label1.place(x=30, y=150)
        label2= Label(self.root,text="Waterwash                           :")
        label2.place(x=30, y=200)
        label3= Label(self.root,text="Interior cleaning                  :")
        label3.place(x=30, y=250)
        label4= Label(self.root,text="Oil change                            :")
        label4.place(x=30, y=300)
        label5= Label(self.root,text="Parts altering or replacing  :")
        label5.place(x=30, y=350)
        label6= Label(self.root,text="Tinkering                               :")
        label6.place(x=30, y=400)
        label7= Label(self.root,text="Painting                                 :")
        label7.place(x=30, y=450)

                #-----------------------ENTRY-----------------------
        
        e1=Entry(self.root,textvariable=self.CustomerName, font='arial 15', bd=7, relief=GROOVE)
        e1.place(x=155,y=50)
        e2=Entry(self.root,textvariable=self.ContactNumber, font='arial 15', bd=7, relief=GROOVE)
        e2.place(x=650,y=50)
        e3=Entry(self.root,textvariable=self.CarModel, font='arial 15', bd=7, relief=GROOVE)
        e3.place(x=155,y=100)
        e4=Entry(self.root,textvariable=self.Kmsdriven, font='arial 15', bd=7, relief=GROOVE)
        e4.place(x=650,y=100)
        e5=Entry(self.root,textvariable=self.Generalservice,font='arial 15', bd=7, relief=GROOVE)
        e5.place(x=190,y=150)
        e6=Entry(self.root,textvariable=self.WaterWash,font='arial 15', bd=7, relief=GROOVE)
        e6.place(x=190,y=200)
        e7=Entry(self.root,textvariable=self.Interiorcleaning,font='arial 15', bd=7, relief=GROOVE)
        e7.place(x=190,y=250)      
        e8=Entry(self.root,textvariable=self.Oilchange,font='arial 15', bd=7, relief=GROOVE)
        e8.place(x=190,y=300)
        e9=Entry(self.root,textvariable=self.Paor,font='arial 15', bd=7, relief=GROOVE)
        e9.place(x=190,y=350)
        e10=Entry(self.root,textvariable=self.Tinkering,font='arial 15', bd=7, relief=GROOVE)
        e10.place(x=190,y=400)
        e11=Entry(self.root,textvariable=self.Painting,font='arial 15', bd=7, relief=GROOVE)
        e11.place(x=190,y=450)

                #------------------------bill------------------------
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=550, y=180, width=350, height=380)
        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

 
        #-----------------------button--------------------------
        b1= Button(text='Generate bill',command=self.welcome_bill)
        b1.place(x=100,y=520)
        b2= Button(text='Delete',command=self.clear_data)
        b2.place(x=300,y=520)
        b3= Button(text='Save',command=self.customerdetails)
        b3.place(x=730,y=150)

        #-----------------------totalbill-----------------------
    def total(self):
            self.gsgt=(self.Generalservice.get())
            self.wwgt=(self.WaterWash.get())
            self.icgt=(self.Interiorcleaning.get())
            self.ocgt=(self.Oilchange.get())
            self.paorgt=(self.Paor.get())
            self.tgt=(self.Tinkering.get())
            self.pgt=(self.Painting())
        #Total=(self.gsgt+self.wwgt+self.icgt+self.ocgt+self.paorgt+self.tgt+self.pgt)
        
    def welcome_bill(self):
            self.txtarea.delete('1.0', END)
            self.txtarea.insert(END, "\tWelcome Vijai Motors")
            self.txtarea.insert(END, f"\n Customername:{self.CustomerName.get()}")
            self.txtarea.insert(END, f"\n Conatactnumber:{self.ContactNumber.get()}")
            self.txtarea.insert(END, f"\n Carmodel:{self.CarModel.get()}")
            self.txtarea.insert(END, f"\n KMS:{self.Kmsdriven.get()}")
            self.txtarea.insert(END, f"\n================================")
            self.txtarea.insert(END, f"\n Workdone\t\t\t\tamount")

            self.txtarea.insert(END, f"\n Generalservice : \t\t\t\t {self.Generalservice.get()}")
            self.txtarea.insert(END, f"\n WaterWash : \t\t\t\t {self.WaterWash.get()}")
            self.txtarea.insert(END, f"\n Interiorcleaning : \t\t\t\t {self.Interiorcleaning.get()}")
            self.txtarea.insert(END, f"\n Oilchang : \t\t\t\t {self.Oilchange.get()}")
            self.txtarea.insert(END, f"\n Parts altering or replacing : \t\t{self.Paor.get()}")
            self.txtarea.insert(END, f"\n Tinkering : \t\t\t\t {self.Tinkering.get()}")
            self.txtarea.insert(END, f"\n Painting : \t\t\t\t {self.Painting.get()}")
            self.txtarea.insert(END, f"\n Total : \t\t\t\t {(self.Generalservice.get())+(self.WaterWash.get())+(self.Interiorcleaning.get())+(self.Oilchange.get()) + (self.Paor.get())+ (self.Tinkering.get())+(self.Painting.get()) }")

    def customerdetails(self):
        #self.CustomerName = self.e1.get()
        #self.ContactNumber = self.e2.get()
        #self.CarModel = self.e3.get()
        #self.Kmsdriven =self.e4.get() 

            if(self.CustomerName=='' or self.CarModel=='' or self.ContactNumber=='' or self.Kmsdriven==''):
                MessageBox.showinfo('Insert status','all required')
            else:
                con=pymysql.connect(host='localhost',user='root',password='',database='customername')
                cursor=con.cursor()

                query=('insert into customerinfo(CustomerName,CarModel,ContactNumber,Kmsdriven) values(%s,%s,%s,%s)')
                cursor.execute(query,(self.CustomerName.get(),self.CarModel.get(),self.ContactNumber.get(),self.Kmsdriven.get()))
                con.commit()
                con.close()
                MessageBox.showinfo('insert status','inserted sucessfully')


    def clear_data(self):
            op = MessageBox.askyesno("Clear", "Do you really want to Clear?")
            if op > 0:
                self.CustomerName.set(0)
                self.CarModel.set(0)
                self.ContactNumber.set(0)
                self.Kmsdriven.set(0)
                self.Generalservice.set(0)
                self.WaterWash.set(0)
                self.Interiorcleaning.set(0)
                self.Oilchange.set(0)
                self.Paor.set(0)
                self.Tinkering.set(0)
                self.Painting.set(0)

                self.welcome_bill()
            self.root.bind('<Configure>' ,self.resizer) 

root = Tk()     
#e = Bill(root)
#e.pack(fill=BOTH, expand=YES)


#root.mainloop()

 
obj = Bill(root)    
root.mainloop()
        
      



