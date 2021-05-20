from tkinter import *
from tkinter.font import families
from PIL import Image,ImageTk
import cx_Oracle
import tkinter.messagebox as tmsg

connect=''
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
        
        frame=Login_window(container,self)
        frame.Login()
        frame.grid(row=0,column=0,sticky='nsew')
        
        # self.frames = {}
        # for F in ( Page1, Page2):

        #     frame = F(container, self)
        #     self.frames[F] = frame

        #     frame.grid(row = 0, column = 0, sticky ="nsew")

        




        
class Login_window(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.width=self.winfo_screenwidth()
        self.height=self.winfo_screenheight()


    def validation(self,user,password):
        self.user=user
        self.password=password
        try:
            global connect 
            connect=cx_Oracle.connect(f'{self.user}/{self.password}')
            tmsg.showinfo('Successfully connected',f'You been successfully connected to {self.user}\n')
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
    


root=App()
root.mainloop()