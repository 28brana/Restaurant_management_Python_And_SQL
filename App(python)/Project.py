from tkinter import *
from tkinter.font import families
import cx_Oracle
from tkinter import ttk
import tkinter.messagebox as tmsg

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
        
        # frame=Database_window(container,self)
        # frame.Structure()
        # frame.grid(row=0,column=0,sticky='nsew')
        
        self.frames = {}
        for F in (Menu_window,Login_window ):

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
        self.Structure()
    
    def Structure(self):
   
    #-- Order-MENU------------------------------------
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

    #--- Menu Table ------------------------
        
        #-----styling tree-------------------------

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
        global connect
        cursor=connect.cursor()
        cursor.execute('select meal_id,name,price from meals order by meal_id')

        for i in cursor:
            x=str(i[0])
            y=str(i[1])
            z=str(i[2])
            my_menu.insert(parent='',index='end',value=(x,y,'Rs. '+z))

        my_menu.pack(fill='both',expand=1)





        





root=App()
root.mainloop()