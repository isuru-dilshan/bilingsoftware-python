from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # =================== Variables ================================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search=StringVar()
        self.product=StringVar()
        self.price=StringVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        # Product Categories List
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]
        # SubCatClothing
        self.SubCatClothing=["Pant","T-Shirt","Shirt"]
        self.Pant=["Levis","Mufti","Spykar"]
        self.price_Levis=5000
        self.price_Mufti=7000
        self.price_Spykar=8000

        self.T_shirt=['Polo','Roadster','Jack&Jones']
        self.price_polo=1500
        self.price_Roadster=1800
        self.price_JackJones=1700

        self.Shirt=['Peter England','Louis Phillipe','Park Avenue']
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_Park=1740

        # SubCatLifeStyle
        self.SubCatLifeStyle=['Bath Soap','Face Cream','Hair Oil']
        self.Bath_Soap=['LifeBuy','Lux','Santoor','Pearl']
        self.price_Life=20
        self.price_Lux=40
        self.price_Santoor=30
        self.price_Pearl=50

        self.Face_Cream=['Fair&Lovely','Ponds','Olay','Garnior']
        self.price_fair=70
        self.price_ponds=100
        self.price_olay=80
        self.price_garnior=90

        self.Hair_oil=['Parachute','Jasmin','Bajaj']
        self.price_para=25
        self.price_jasmin=22
        self.price_bajaj=30

        # SubCatMobiles
        self.SubCatMobiles=['Iphone','Samsung','Xiome','RealMe','One+']
        self.Iphone=['Iphone_X','Iphone_11','Iphone_12']
        self.price_ix=150000
        self.price_i11=200000
        self.price_i12=250000

        self.Samsung=['Samsung M16','Samsung M12','Samsung M21']
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000

        self.Xiome=['RedMe11','RedMe12','RedMePro']
        self.price_r11=11000
        self.price_r12=15000
        self.price_rpro=10000

        self.RealMe=['RealMe 12','RealMe 13','RealMe Pro']
        self.price_rel12=25000
        self.price_rel13=27000
        self.price_relpro=30000

        self.OnePlus=['OnePlus1','OnePlus2','OnePlus3']
        self.price_one1=45000
        self.price_one2=60000
        self.price_one3=45800

    # ================ Image01 ==============================
        img=Image.open(r"E:\Python-projects\photos\shop.jpg")
        img=img.resize((800,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

    # ================ Image02 ==============================
        img2=Image.open(r"E:\Python-projects\photos\download.jpg")
        img2=img2.resize((800,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbl_img2=Label(self.root,image=self.photoimg2)
        lbl_img2.place(x=500,y=0,width=600,height=130)

    # ================ Image03 ==============================
        img3=Image.open(r"E:\Python-projects\photos\D1028_63_099_1200.jpg")
        img3=img3.resize((800,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbl_img3=Label(self.root,image=self.photoimg3)
        lbl_img3.place(x=1050,y=0,width=500,height=130)

    # ================ Main Title ==========================
        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=130,width=1530,height=45)

    # ================ Main_Frame =========================
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)

    #  Customer LabaleFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Information",font=("times new roman",15,"bold"),bg="white",fg="red")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile NO:",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lblCustName=Label(Cust_Frame,text="Customer Name:",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lblEmail=Label(Cust_Frame,text="Email:",font=("times new roman",12,"bold"),bg="white",fg="black")
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Product LableFrame ======================================= #
        Product_Frame=LabelFrame(Main_Frame,text="Product Information",font=("times new roman",15,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)

        # Category
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Select Category:",fg="black")
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        # SubCategory
        self.lblSubCategory=Label(Product_Frame,font=('aria',12,'bold'),bg="white",text="Sub Category:",fg="black")
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.Combo_SubCategory=ttk.Combobox(Product_Frame,value=[""],font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_SubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        # Product Name
        self.lblProductName=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Product Name:",fg="black")
        self.lblProductName.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.Combo_ProductName=ttk.Combobox(Product_Frame,textvariable=self.product,font=('arial',10,'bold'),width=24,state="readonly")
        self.Combo_ProductName.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.Combo_ProductName.bind("<<ComboboxSelected>>",self.prices)

        # Price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Price:",fg="black")
        self.lblPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        self.Combo_Price=ttk.Combobox(Product_Frame,textvariable=self.price,font=('arial',9,'bold'),width=20,state="readonly")
        self.Combo_Price.grid(row=0,column=4,sticky=W,padx=5,pady=2)

        # Quantity
        self.lblQuantity=Label(Product_Frame,font=('arial',12,'bold'),bg="white",text="Quantity:",fg="black")
        self.lblQuantity.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        self.txtQuatity = ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial",10 , "bold"), width=23)
        self.txtQuatity.grid(row=1, column=4, sticky=W, padx=5, pady=2)

        # Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        # Image01
        img12 = Image.open(r"E:\Python-projects\photos\nivea.jpg")
        img12 = img12.resize((500, 340), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        lbl_img12 = Label(MiddleFrame, image=self.photoimg12)
        lbl_img12.place(x=0, y=0, width=500, height=340)

        # Image02
        img13 = Image.open(r"E:\Python-projects\photos\apple-products.jpg")
        img13 = img13.resize((500, 340), Image.ANTIALIAS)
        self.photoimg13 = ImageTk.PhotoImage(img13)

        lbl_img13 = Label(MiddleFrame, image=self.photoimg13)
        lbl_img13.place(x=490, y=0, width=500, height=340)

        # Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=10,width=500,height=40)

        self.lblBill=Label(Search_Frame,font=('arial',14,'bold'),bg="dark blue",fg="white",text="Bill Number:")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search,font=('arial',13,'bold'),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=1)

        self.BtnSearch=Button(Search_Frame,text="Search",font=('arial',13,'bold'),bg="darkgreen",fg="white",width=10,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        # RightFrame Bill Aria
        RightLableFrame=LabelFrame(Main_Frame,text="Bill Aria",font=('times new roman',15,'bold'),bg="white",fg="red")
        RightLableFrame.place(x=1000,y=45,width=480,height=440)

        scoll_y=Scrollbar(RightLableFrame,orient=VERTICAL)
        self.textarea=Text(RightLableFrame,yscrollcommand=scoll_y.set,bg="white",fg="blue",font=('times new roman',13,'bold'))
        scoll_y.pack(side=RIGHT,fill=Y)
        scoll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Bill Counter LableFrame ======================================= #
        Button_Frame = LabelFrame(Main_Frame, text="Bill Counter:", font=("times new roman", 15, "bold"),bg="white", fg="red")
        Button_Frame.place(x=0, y=485, width=1520, height=125)

        self.lblSubTotal=Label(Button_Frame,font=('arial',12,'bold'),bg='white',text="Sub Total:",bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntySubTotal=ttk.Entry(Button_Frame,textvariable=self.sub_total,font=('arial',10,'bold'),width=26)
        self.EntySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lbl_tax=Label(Button_Frame,font=('arial',12,'bold'),bg='white',text="Gov Tax:",bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Button_Frame,textvariable=self.tax_input,font=('arial',10,'bold'),width=26)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbl_total=Label(Button_Frame,font=('arial',12,'bold'),bg='white',text="Total:",bd=4)
        self.lbl_total.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txt_Total=ttk.Entry(Button_Frame,textvariable=self.total,font=('arial',10,'bold'),width=26)
        self.txt_Total.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # Button Frame
        Btn_Frame=Frame(Button_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,text="Add To Cart",command=self.AddItem,font=('arial',14,'bold'),bg="dark green",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenerateBill=Button(Btn_Frame,text="Generate Bill",font=('arial',14,'bold'),bg="dark green",fg="white",width=15,cursor="hand2")
        self.BtnGenerateBill.grid(row=0,column=1)

        self.BtnSaveBill=Button(Btn_Frame,text="Save Bill",font=('arial',14,'bold'),bg="dark green",fg="white",width=15,cursor="hand2")
        self.BtnSaveBill.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,text="Print",font=('arial',14,'bold'),bg="dark green",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,text="Clear",font=('arial',14,'bold'),bg="red",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,text="Exit",font=('arial',14,'bold'),bg="red",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()
        self.l = []

    # ======================= Function Declaration =====================

    def AddItem(self):
        Tax=1
        self.n=self.price.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else:
            self.textarea.insert(END,f"\n{self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t ***Welcome Keels Foods City***")
        self.textarea.insert(END,f"\n Bill Number:\t{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:\t{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n=============================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END, "\n=============================================")


    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.Combo_SubCategory.config(value=self.SubCatClothing)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get() == "LifeStyle":
            self.Combo_SubCategory.config(value=self.SubCatLifeStyle)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get() == "Mobiles":
            self.Combo_SubCategory.config(value=self.SubCatMobiles)
            self.Combo_SubCategory.current(0)

    def Product_add(self,event=""):
        if self.Combo_SubCategory.get()=="Pant":
            self.Combo_ProductName.config(value=self.Pant)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get() == "T-Shirt":
            self.Combo_ProductName.config(value=self.T_shirt)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get() == "Shirt":
            self.Combo_ProductName.config(value=self.Shirt)
            self.Combo_ProductName.current(0)

    # LifeStyle
        if self.Combo_SubCategory.get()=="Bath Soap":
            self.Combo_ProductName.config(value=self.Bath_Soap)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get() == "Face Cream":
            self.Combo_ProductName.config(value=self.Face_Cream)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get() == "Hair Oil":
            self.Combo_ProductName.config(value=self.Hair_oil)
            self.Combo_ProductName.current(0)

    # Mobile
        if self.Combo_SubCategory.get()=="Iphone":
            self.Combo_ProductName.config(value=self.Iphone)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get() == "Samsung":
            self.Combo_ProductName.config(value=self.Samsung)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get() == "Xiome":
            self.Combo_ProductName.config(value=self.Xiome)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get() == "RealMe":
            self.Combo_ProductName.config(value=self.RealMe)
            self.Combo_ProductName.current(0)

        if self.Combo_SubCategory.get() == "One+":
            self.Combo_ProductName.config(value=self.OnePlus)
            self.Combo_ProductName.current(0)

    def prices(self,event=""):
        if self.Combo_ProductName.get()=="Levis":
            self.Combo_Price.config(value=self.price_Levis)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Mufti":
            self.Combo_Price.config(value=self.price_Mufti)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Spykar":
            self.Combo_Price.config(value=self.price_Spykar)
            self.Combo_Price.current(0)
            self.qty.set(1)

        # T-Shirt
        if self.Combo_ProductName.get() == "Polo":
            self.Combo_Price.config(value=self.price_polo)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Roadster":
            self.Combo_Price.config(value=self.price_Roadster)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Jack&Jones":
            self.Combo_Price.config(value=self.price_JackJones)
            self.Combo_Price.current(0)
            self.qty.set(1)
        # Shirt

        if self.Combo_ProductName.get() == "Peter England":
            self.Combo_Price.config(value=self.price_Peter)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Louis Phillipe":
            self.Combo_Price.config(value=self.price_Louis)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Park Avenue":
            self.Combo_Price.config(value=self.price_Park)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "LifeBuy":
            self.Combo_Price.config(value=self.price_Life)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Lux":
            self.Combo_Price.config(value=self.price_Lux)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Santoor":
            self.Combo_Price.config(value=self.price_Santoor)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Pearl":
            self.Combo_Price.config(value=self.price_Pearl)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get()=="Fair&Lovely":
            self.Combo_Price.config(value=self.price_fair)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Ponds":
            self.Combo_Price.config(value=self.price_ponds)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Olay":
            self.Combo_Price.config(value=self.price_olay)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Garnier":
            self.Combo_Price.config(value=self.price_garnior)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Parachute":
            self.Combo_Price.config(value=self.price_para)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Jasmin":
            self.Combo_Price.config(value=self.price_jasmin)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Bajaj":
            self.Combo_Price.config(value=self.price_bajaj)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Iphone_X":
            self.Combo_Price.config(value=self.price_ix)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Iphone_11":
            self.Combo_Price.config(value=self.price_i11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Iphone_12":
            self.Combo_Price.config(value=self.price_i12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Samsung M16":
            self.Combo_Price.config(value=self.price_sm16)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Samsung M12":
            self.Combo_Price.config(value=self.price_sm12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "Samsung M21":
            self.Combo_Price.config(value=self.price_sm21)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "RedMe11":
            self.Combo_Price.config(value=self.price_r11)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "RedMe12":
            self.Combo_Price.config(value=self.price_r12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "RedMePro":
            self.Combo_Price.config(value=self.price_rpro)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "RealMe 12":
            self.Combo_Price.config(value=self.price_rel12)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "RealMe 13":
            self.Combo_Price.config(value=self.price_rel13)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "RealMe Pro":
            self.Combo_Price.config(value=self.price_relpro)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "OnePlus1":
            self.Combo_Price.config(value=self.price_one1)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "OnePlus2":
            self.Combo_Price.config(value=self.price_one2)
            self.Combo_Price.current(0)
            self.qty.set(1)

        if self.Combo_ProductName.get() == "OnePlus3":
            self.Combo_Price.config(value=self.price_one3)
            self.Combo_Price.current(0)
            self.qty.set(1)




if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
