from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
     def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")


        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=IntVar()
        self.var_email=StringVar()
        self.var_sec_ques=StringVar()
        self.var_sec_ans=StringVar()
        self.var_password=StringVar()
        self.var_confpassword=StringVar()
        

        self.bg=ImageTk.PhotoImage(file=r"Registerbackground.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0)

        
        frame=Frame(self.root,bg="#5a5192")
        frame.place(x=255,y=255,width=965,height=525)

        register_lbl=Label(frame,text="REGISTER HERE",font=("SF Pro Display",20,"bold"),fg="white",bg="#5a5192")
        register_lbl.place(x=380,y=0)


        fname=Label(frame,text="First Name :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        fname.place(x=50,y=50)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("SF Pro Display",15))
        self.fname_entry.place(x=50,y=100,width=320,height=40)

        contact=Label(frame,text="Contact No :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        contact.place(x=50,y=150)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("SF Pro Display",15))
        self.contact_entry.place(x=50,y=200,width=320,height=40)

        select_sec=Label(frame,text="Select Security Questions :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        select_sec.place(x=50,y=250)

        self.combo_security_ques=ttk.Combobox(frame,textvariable=self.var_sec_ques,font=("SF Pro Display",15),state="readonly")
        self.combo_security_ques["values"]=("Select","Your Birth Place","Your email ID","Your pet name","Your favorite fruit name","Your favorite animal name")
        self.combo_security_ques.current(0)
        self.combo_security_ques.place(x=50,y=300,width=320,height=40)
        

        password=Label(frame,text="Password :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        password.place(x=50,y=350)

        self.password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("SF Pro Display",15))
        self.password_entry.place(x=50,y=400,width=320,height=40)


        lname=Label(frame,text="Last Name :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        lname.place(x=600,y=50)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("SF Pro Display",15))
        self.lname_entry.place(x=600,y=100,width=320,height=40)

        email=Label(frame,text="Email :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        email.place(x=600,y=150)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("SF Pro Display",15))
        self.email_entry.place(x=600,y=200,width=320,height=40)

        select_sec_ans=Label(frame,text="Enter Security Answer :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        select_sec_ans.place(x=600,y=250)

        self.select_sec_ans_entry=ttk.Entry(frame,textvariable=self.var_sec_ans,font=("SF Pro Display",15))
        self.select_sec_ans_entry.place(x=600,y=300,width=320,height=40)

        confirm_pass=Label(frame,text="Confirm Password :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        confirm_pass.place(x=600,y=350)

        self.confirm_pass_entry=ttk.Entry(frame,textvariable=self.var_confpassword,font=("SF Pro Display",15))
        self.confirm_pass_entry.place(x=600,y=400,width=320,height=40)

        regbtn=Button(frame,text="Register now",command=self.register_data,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#c30e89",activeforeground="white",activebackground="#c30e89")
        regbtn.place(x=270,y=480,width=150,height=45)

        logbtn=Button(frame,text="Login now",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#c30e89",activeforeground="white",activebackground="#c30e89")
        logbtn.place(x=550,y=480,width=150,height=45)


    #set on action

     def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_sec_ques.get()=="Select":
            messagebox.showerror("Error","All fields are required")

        elif self.var_password.get()!=self.var_confpassword.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        else:
            conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist , please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),self.var_lname.get(),str(self.var_contact.get()),self.var_sec_ques.get(),self.var_sec_ans.get(),self.var_password.get(),self.var_email.get()
                                                            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successful")
                                                        
                       

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
