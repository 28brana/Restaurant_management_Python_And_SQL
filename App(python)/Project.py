from tkinter import *
from tkinter.font import families
import cx_Oracle
from tkinter import ttk
import tkinter.messagebox as tmsg
from datetime import date

# connect=cx_Oracle.connect()
connect=cx_Oracle.connect('system/28brana')

class App(Tk):

    def __init__(self):
        super().__init__()
        
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(False,False)
        # self.configure(background="#FC6646")

        header=Frame(self,bg='#FC6646',borderwidth=20,height=80)
        header.pack(fill='x')

        from PIL import Image,ImageTk
        icon=Image.open('restaurant.png')
        icon.thumbnail((75,75))
        photo=ImageTk.PhotoImage(icon)
        icon_pic=Label(header,image=photo,bg='#FC6646')
        icon_pic.photo = photo
        icon_pic.pack(side='left',padx=50)

        Label(header,text='RESTAURANT MANAGEMENT SYSTEM',font=('comic sansns',20,'bold'),bg='#FC6646',fg='white').pack(pady=20,padx=280,side='left')

    #--- Second Frame ---------------------
        container = Frame(self,bg='grey')
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        # frame=Admin_window(container,self)
        # frame.grid(row=0,column=0,sticky='nsew')
        
        self.frames = {}
        for F in (Admin_window,Menu_window,Login_window):

            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

    def show(self,window):
        frame = self.frames[window]
        frame.tkraise()
	   

        




        
class Login_window(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller=controller
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.Login()


    def validation(self,user,password):
        self.user=user
        self.password=password
        try:
            global connect 
            connect=cx_Oracle.connect(f'{self.user}/{self.password}')
            tmsg.showinfo('Successfully connected',f'You been successfully connected to {self.user}\n')
            self.controller.show(Menu_window)
            print('Successfully connected',' You are now Connect !!!!!!\n')
        except cx_Oracle.DatabaseError as e:
            x=tmsg.showerror('Wrong Input','Your Username or Password is wrong\n \n Please Enter correct Username or Password')
        except Exception as e:
            tmsg.showerror('Wrong Input',e)
     
    def Login(self):
        Loginbox=Frame(self,bg='white',borderwidth=6)
        Loginbox.place(x=self.width/3,y=self.height/6,width=400,height=500)
        Label(Loginbox,text='Login',bg='white',fg='blue',font=('comic sansns',19,'bold')).pack(pady=50)
    
    # ----- user input------------------------------------
        uservalue=StringVar()
        user=Label(Loginbox,text="USERNAME",bg='white',font=('comic sansns',12),fg='grey')
        user.pack()
        userinput=Entry(Loginbox,textvariable=uservalue,font=('comic sansns',12))
        userinput.focus()
        userinput.pack(pady=20)
    #----- Password input -------------------------------
        passwordvalue=StringVar()
        password=Label(Loginbox,text="PASSWORD",bg='white',font=('comic sansns',12),fg='grey')
        password.pack(pady=10)
        passwordinput=Entry(Loginbox,textvariable=passwordvalue,font=('comic sansns',12))
        
        passwordinput.pack(pady=10)
    #----- Submit Button  -------------------------
        Button(Loginbox,text='Login',bg='red',fg='white',width=15,font=('comic sansns',12),command=lambda:self.validation(uservalue.get(),passwordvalue.get())).pack(pady=50)
    

class Menu_window(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()
        self.controller=controller
        self.Structure()
        # self.configure(background="#FC6646")
    
    def Structure(self):
    
    #--- MENU-FRAME ------------------------------------
        #----- Menu box --------------
        menubox=Frame(self,borderwidth=3,relief=SUNKEN,width=500,height=650)
        menubox.pack_propagate(0)
        menubox.pack(side=LEFT,padx=20)
        #----- Menu Heading -----------
        menuheader=Frame(menubox,bg='#FC6646')
        menuheader.pack(fill='x')
        Label(menuheader,text='MENU',bg='#FC6646',fg='white',font=('comic sansns',17,'bold')).pack(fill='x')
        #----- Sub Menu Heading -------
        submenu=Frame(menubox,bg='#FC6646')
        submenu.pack(fill='x')

        Label(submenu,text='FOOD_ID',bg='#FC6646',font=('comic sansns',15,'bold'),fg='white').grid(row=0,column=0,padx=30)
        Label(submenu,text='FOOD',bg='#FC6646',font=('comic sansns',15,'bold'),fg='white').grid(row=0,column=1,padx=50)
        Label(submenu,text='Price',bg='#FC6646',font=('comic sansns',15,'bold'),fg='white').grid(row=0,column=2,padx=40)

    # >--- Menu Table ------------------------
        
        #> >-----styling tree-------------------------

        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview',
            background='silver',
            rowheight=30,
            font=('comic sansns',15)
        )

        my_menu=ttk.Treeview(menubox)
        my_menu['columns']=('Food_id','Food','Price')

        #-- Assiging width
        my_menu.column('#0',width=0,stretch=NO)
        my_menu.column('Food_id',width=100,anchor='c')
        my_menu.column('Food',width=150,anchor='c')
        my_menu.column('Price',width=100)
        
        #---- removing heading
        my_menu['show']='tree'

        #--- Adding data
        cursor=connect.cursor()
        cursor.execute('select meal_id,name,price from meals order by meal_id')

        for i in cursor:
            x=str(i[0])
            y=str(i[1])
            z=str(i[2])
            my_menu.insert(parent='',index='end',value=(x,y,'Rs. '+z))

        my_menu.pack(fill='both',expand=1)
    #Admin - board--------
        option=Frame(self,bg='green',width=150)
        option.pack_propagate(0)
        option.pack(fill='y',side=RIGHT)

        #Admin Button

        Button(option,text='GO TO ADMIN',command= lambda :self.controller.show(Admin_window)).pack()



    #---Order-board--------
        order=Frame(self)
        order.pack(expand=1,fill='both')
        
        #Frame
        EntryFrame1=Frame(order,bg='green',width=500,height=500)
        EntryFrame1.pack_propagate(0)
        EntryFrame1.pack(pady=100)
        
        #Order header
        Label(EntryFrame1,text='Order Menu',bg='#FC6646',fg='white',font=('comic sansns',15,'bold'),height=2).pack(fill=X)

        # Value for entry
        namevalue=StringVar()
        phonevalue=StringVar()
        cityvalue=StringVar()
        ordername=StringVar()
        
        #Entry

        Label(EntryFrame1,text='Name',bg='green',font=('comic sansns',15)).pack(pady=5)
        Entry(EntryFrame1,textvariable=namevalue,font=('comic sansns',10)).pack(pady=5)

        Label(EntryFrame1,text='Phone number',bg='green',font=('comic sansns',15)).pack(pady=5)
        Entry(EntryFrame1,textvariable=phonevalue,font=('comic sansns',10)).pack(pady=5)

        Label(EntryFrame1,text='City',bg='green',font=('comic sansns',15)).pack(pady=5)
        Entry(EntryFrame1,textvariable=cityvalue,font=('comic sansns',10)).pack(pady=5)

        Label(EntryFrame1,text='Order Name',bg='green',font=('comic sansns',15)).pack(pady=5)
        #combo box
        cursor.execute('select name from meals')
        food_list=[]
        for i in cursor:
            food_list+=[i[0]]
        
        box=ttk.Combobox(EntryFrame1,textvariable=ordername,state='readonly')
        box['values']=food_list
        box.current(1)
        box.pack(pady=5)

        Label(EntryFrame1,text='Quantity',font=('comic sansns',15),bg='green').pack(pady=10)
        quantityvalue=Scale(EntryFrame1,from_=0,to=100,orient=HORIZONTAL,length=200)
        quantityvalue.pack(pady=5)

        info=[namevalue,phonevalue,cityvalue,ordername,quantityvalue]
        Button(EntryFrame1,text='ORDER NOW',bg='red',fg='white',command=lambda :self.Place_Order(info)).pack(pady=20)

        
    

    def Place_Order(self,info):
        global connect
        cursor=connect.cursor()
        today = date.today()
        name=info[0].get()
        phone=info[1].get()
        city=info[2].get()
        ordername=info[3].get()
        quantity=info[4].get()
        d = today.strftime("%d-%b-%y")
        if(name==''):
            tmsg.showerror('Name','Please Enter Your Name !!!  ')
            return
        elif(len(phone) > 10):
            tmsg.showerror('Phone number','Length of Phone number is More than 10 Digit ')
            return
        elif(len(phone)<10):
            tmsg.showerror('Phone number','Length of Phone is Too small')
            return
        
        
        c_id=cursor.execute('select max(cust_id) from customers')
        c_id=list(c_id)[0][0]+1

        order_id=cursor.execute('select max(order_id) from orders')
        order_id=list(order_id)[0][0]+1

        meal_id=cursor.execute(f"select meal_id from meals where name='{ordername}'")
        meal_id=list(meal_id)[0][0]

        try:
            cursor.execute(f"insert into customers values({c_id},'{name}','{phone}','{city}',{order_id}) ")
        except cx_Oracle.Error as e:
            tmsg.showerror('Error has been occured','In customer table : '+e)
        
        try:
            cursor.execute(f"insert into orders values({order_id},'{d}','Pending',{quantity},{meal_id})")
            tmsg.showinfo('Order Done','Order has been placed !!!!! ')
            
        except cx_Oracle.Error as e:
            tmsg.showerror('Error has been occured','In order table : '+e)
        


        
class Admin_window(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()        

        #Tree Frame
        tree_frame=Frame(self,width=500,height=500,bg='red')
        tree_frame.pack_propagate(0)
        tree_frame.pack(side=LEFT,anchor=N,pady=60,padx=10)
        Label(tree_frame,text='Tables',height=1,bg='pink').pack(fill=X)
         
        #Tree scroll bar
        tree_scroll=Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT,fill=Y)

        #Creating Tree
        self.my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set)
        # self.my_tree['column']=('Worker id','Name','Post','Salary','Hire date')

        #Tree scroll bar configure
        tree_scroll.config(command=self.my_tree.yview)


        #Add Data
        # my_tree.insert('','end',value=(1,'Bharat','Bodss',2000,'28-1-2019'))
        
        self.my_tree.pack(fill=X,padx=10)

        # #Styling Tree
        # tree_style=ttk.Style()
        # tree_style.configure('Treeview',
        #     background='red'
        # )

        #Admin Frame
        admin_frame=Frame(self,borderwidth=2,relief=SUNKEN)
        admin_frame.pack(padx=10,pady=10)

        #Admin Header 
        Label(admin_frame,text='ADMIN BLOCK',bg='red',height=2).pack(fill=X)
       

        #Display Frame

        display_Frame=Frame(admin_frame,borderwidth=2,relief=SUNKEN)
        display_Frame.pack(pady=10)

        #-----------Display Items---------------

        #------Label-----
       
        
        Label(display_Frame,text='Select Table').grid(row=0,column=0)
        

        #------Option menu------
        Table=['Customers','Orders','Meals','Workers','Managers']
        Table_value=StringVar()
        Table_value.set(Table[0])

        Table_option=OptionMenu(display_Frame,Table_value,*Table)
        Table_option.grid(row=1,column=0)
        #------Button-------
        Button(display_Frame,text='Show',command=lambda : self.select_tab(Table_value.get())).grid(row=1,column=1)

        #Subframe
        sub_frame=Frame(admin_frame,borderwidth=2,relief=SUNKEN)
        sub_frame.pack()
        Label(sub_frame,text='Worker records',bg='red',height=1).pack(fill=X)

        # -> insertframe
        insert_frame=Frame(sub_frame)
        insert_frame.pack()

        # -> -> Columns Heading
        
        Label(insert_frame,text='Wid').grid(row=0,column=0,padx=20)
        Label(insert_frame,text='Name').grid(row=0,column=1,padx=20)
        Label(insert_frame,text='Post').grid(row=0,column=2,padx=20)
        Label(insert_frame,text='Salary').grid(row=0,column=3,padx=20)
        Label(insert_frame,text='Hire Date').grid(row=0,column=4,padx=20)

        # -> -> Entry Columns
        wid=IntVar()
        name=StringVar()
        post=StringVar()
        salary=IntVar()
        hiredate=StringVar()

        Entry(insert_frame,textvariable=wid).grid(row=1,column=0)
        Entry(insert_frame,textvariable=name).grid(row=1,column=1)
        Entry(insert_frame,textvariable=post).grid(row=1,column=2)
        Entry(insert_frame,textvariable=salary).grid(row=1,column=3)
        Entry(insert_frame,textvariable=hiredate).grid(row=1,column=4)

        # Insert Update
        Button(sub_frame,text='Insert').pack(pady=10)
        Label(sub_frame,text='To Update write id same').pack()
        Button(sub_frame,text='Update').pack()
        
        # Delete 
        Label(admin_frame,text="Delete Record",bg='red').pack(fill=X)

        Id=IntVar()
        Label(admin_frame,text='Select Table from you want to delete').pack()
        del_table=['Customers','Orders','Meals','Workers','Manager']
        del_value=StringVar()
        del_value.set(del_table[0])
        del_option=OptionMenu(admin_frame,del_value,*del_table)
        del_option.pack()
        Label(admin_frame,text="Enter Id for deleting").pack()
        Entry(admin_frame,textvariable=Id).pack(pady=10)
        Button(admin_frame,text='Delete').pack()
    
    #Clear ALL table
    def remove_all(self):
        for i in self.my_tree.get_children():
            self.my_tree.delete(i)


    #This will contain all select * statements or Display statements
    def select_tab(self,table):  
        global connect
        cursor=connect.cursor()
        if(table == 'Customers'):
            #Creating columns
            self.my_tree['column']=('Customer id','Name','Phone no','City','Order id')
            #Formating columns
            self.my_tree.column('#0',width=0,stretch=NO)
            self.my_tree.column('Customer id',width=50,anchor=CENTER)
            self.my_tree.column('Name',width=100,anchor=CENTER)
            self.my_tree.column('Phone no',width=100,anchor=CENTER)
            self.my_tree.column('City',width=100,anchor=CENTER)
            self.my_tree.column('Order id',width=100,anchor=CENTER)
            #creating headings
            self.my_tree.heading('Customer id',text='C_id')
            self.my_tree.heading('Name',text='Name')
            self.my_tree.heading('Phone no',text='Phoneno')
            self.my_tree.heading('City',text='City')
            self.my_tree.heading('Order id',text='O_id')
        elif table == 'Orders':
            #Creating columns
            self.my_tree['column']=('Order id','Time','Status','Quantity')
            #Formating columns
            self.my_tree.column('#0',width=0,stretch=NO)
            self.my_tree.column('Order id',width=50,anchor=CENTER)
            self.my_tree.column('Time',width=100,anchor=CENTER)
            self.my_tree.column('Status',width=100,anchor=CENTER)
            self.my_tree.column('Quantity',width=100,anchor=CENTER)
           
            #creating headings
            self.my_tree.heading('Order id',text='O_id')
            self.my_tree.heading('Time',text='Time')
            self.my_tree.heading('Status',text='Status')
            self.my_tree.heading('Quantity',text='Quantity')
            
        elif table == 'Meals':
            #Creating columns
            self.my_tree['column']=('Meal id','Name','Price','Order id')
            #Formating columns
            self.my_tree.column('#0',width=0,stretch=NO)
            self.my_tree.column('Meal id',width=50,anchor=CENTER)
            self.my_tree.column('Name',width=100,anchor=CENTER)
            self.my_tree.column('Price',width=100,anchor=CENTER)
            self.my_tree.column('Order id',width=100,anchor=CENTER)
            
            #creating headings
            self.my_tree.heading('Meal id',text='Meal id')
            self.my_tree.heading('Name',text='Name')
            self.my_tree.heading('Price',text='Price')
            self.my_tree.heading('Order id',text='Order id')
            
        elif table == 'Workers':
            #Creating columns
            self.my_tree['column']=('Worker id','Name','Post','Salary','Hire date')
            #Formating columns
            self.my_tree.column('#0',width=0,stretch=NO)
            self.my_tree.column('Worker id',width=50,anchor=CENTER)
            self.my_tree.column('Name',width=100,anchor=CENTER)
            self.my_tree.column('Post',width=100,anchor=CENTER)
            self.my_tree.column('Salary',width=100,anchor=CENTER)
            self.my_tree.column('Hire date',width=100,anchor=CENTER)
            #creating headings
            self.my_tree.heading('Worker id',text='WID')
            self.my_tree.heading('Name',text='Name')
            self.my_tree.heading('Post',text='Post')
            self.my_tree.heading('Salary',text='Salary')
            self.my_tree.heading('Hire date',text='Hire date')
            
        elif table == 'Managers':
            #Creating columns
            self.my_tree['column']=('Manager id','Department','NW')
            #Formating columns
            self.my_tree.column('#0',width=0,stretch=NO)
            self.my_tree.column('Manager id',width=100,anchor=CENTER)
            self.my_tree.column('Department',width=100,anchor=CENTER)
            self.my_tree.column('NW',width=100,anchor=CENTER)
           
            #creating headings
            self.my_tree.heading('Manager id',text='Manager id')
            self.my_tree.heading('Department',text='Department')
            self.my_tree.heading('NW',text='NW')
        
        self.remove_all()

        state=f'select * from {table}'
        record=cursor.execute(state)
        for i in record:
            self.my_tree.insert('','end',value=i)


            
        
    
    #This will contain all insert statements of workertable
    def insert_tab(self,arr):
        pass
        
    #This will contain all update statements of worker table
    def update_tab(self,arr):
        pass
    
    #This will delete all record related to given id of specific table
    def delete(self,id,table):
        pass




root=App()
root.mainloop()