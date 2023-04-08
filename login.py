from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import re
import mysql.connector
from student import Student
from train import Train
from face_rec import Face_Rec

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")

        self.bg=ImageTk.PhotoImage(file=r"Dark Green Modern Gradient Wave Linktree Background.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="#5a5192")
        frame.place(x=500,y=220,width=400,height=400)

        get_str=Label(frame,text="Get Started",font=("SF Pro Display",20,"bold"),fg="white",bg="#5a5192")
        get_str.place(x=160,y=20)

        #labels for username and password
        email=Label(frame,text="Mail ID ",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        email.place(x=90,y=80)

        self.txtusername=ttk.Entry(frame,font=("SF Pro Display",15))
        self.txtusername.place(x=90,y=120,width=320,height=40)

        username=Label(frame,text="Password ",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        username.place(x=90,y=170)

        self.txtpassword=ttk.Entry(frame,font=("SF Pro Display",15),show="*")
        self.txtpassword.place(x=90,y=210,width=320,height=40)

        #username and password icon images

        img1=Image.open(r"password.png")
        img1=img1.resize((40,40),Image.ANTIALIAS)   
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="#5a5192",borderwidth=0)    
        lblimg1.place(x=530,y=342,width=25,height=25)

        img2=Image.open(r"username.png")
        img2=img2.resize((50,50),Image.ANTIALIAS)   
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="#5a5192",borderwidth=0)    
        lblimg2.place(x=530,y=247,width=25,height=25)

        #LoginButton
        loginbtn=Button(frame,command=self.login,text="Login",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="cyan",activeforeground="white",activebackground="#5ebfd9")
        loginbtn.place(x=160,y=275,width=90,height=45)

        #RegisterButton

        registerbtn=Button(frame,text="Register",command=self.register_window,font=("SF Pro Display",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="cyan",activeforeground="white",activebackground="#5a5192")
        registerbtn.place(x=58,y=300,width=120,height=45)

        #forgotpassword

        forgotbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("SF Pro Display",12,"bold"),bd=3,relief=RIDGE,fg="white",bg="cyan",activeforeground="white",activebackground="#5a5192")
        forgotbtn.place(x=58,y=330,width=160,height=45)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def validateMail(self,email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return TRUE
        else:
            return FALSE

    def login(self):
        if self.txtusername.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.validateMail(self.txtusername.get())==FALSE:
            messagebox.showerror("Error","Invalid Email ID")
        else:
            conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
            my_cursor=conn.cursor()
            my_cursor.execute("Select* from register where email=%s and password=%s",(self.txtusername.get(),self.txtpassword.get()))
            row=my_cursor.fetchone()
            print(self.txtpassword.get())
            if row==None :
                messagebox.showerror("Error","Invalid username or password")
            else:
                self.new_window=Toplevel(self.root)
                self.app=Face_Recognition_System(self.new_window)
        conn.commit()
        conn.close()

    def reset_password(self):
        if self.combo_security_ques.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.select_sec_ans_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer to the security question",parent=self.root2)
        elif self.txt_new_pass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(user="root", password="",host="localhost",database="student_management_system",port="3306")
            my_cursor=conn.cursor() 
            query=("select * from register where email=%s and sec_q=%s and sec_a=%s")
            value=(self.txtusername.get().lower(),self.combo_security_ques.get(),self.select_sec_ans_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                vl=(self.txt_new_pass.get(),self.txtusername.get().lower())
                my_cursor.execute(query,vl) 
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been updated , please login again with your new password",parent=self.root2)
                self.root2.destroy()
        

    def return_login(self):
        self.root.destroy()  


    def forgot_password_window(self):
        if self.txtusername.get()=="":
            messagebox.showerror("Error","Username is required to reset password")
        else:   
            conn=mysql.connector.connect(user="root", password="",host="localhost",database="student_management_system",port="3306")
            my_cursor=conn.cursor()   
            query=("select * from register where email=%s")
            value=(self.txtusername.get(),)
            my_cursor.execute(query,value) 
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","User not found") 
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.resizable(0,0)
                self.root2.geometry("340x450+610+170")
                self.root2.configure(bg="#5a5192")

                l=Label(self.root2,text="Forgot password",font=("SF Pro Display",20,"bold"),fg="white",bg="#5a5192")
                l.place(x=0,y=10,relwidth=1)

                select_sec=Label(self.root2,text="Select Security Questions :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
                select_sec.place(x=50,y=80)

                self.combo_security_ques=ttk.Combobox(self.root2,font=("SF Pro Display",15),state="readonly")
                self.combo_security_ques["values"]=("Select","Your Birth Place","Your pet name","Your favorite fruit name","Your favorite animal name")
                self.combo_security_ques.current(0)
                self.combo_security_ques.place(x=50,y=110,width=250)

                select_sec_ans=Label(self.root2,text="Enter Security Answer :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
                select_sec_ans.place(x=50,y=150)

                self.select_sec_ans_entry=ttk.Entry(self.root2,font=("SF Pro Display",15))
                self.select_sec_ans_entry.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="Enter New Password :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
                new_password.place(x=50,y=220)
                
                self.txt_new_pass=ttk.Entry(self.root2,font=("SF Pro Display",15),show="*")
                self.txt_new_pass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
                btn.place(x=130,y=290,height=45)

        
class Register:
     def validateMail(self,email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return TRUE
        else:
            return FALSE

     def __init__(self,root):
        self.root = root
        self.root.resizable(0,0)
        self.root.title("Register")
        self.root.geometry("1500x1000+0+0")


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
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
      
        frame=Frame(self.root,bg="#5a5192")
        frame.place(x=250,y=255,width=965,height=530)

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

        select_sec_ans=Label(frame,text="Enter Security Answer :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        select_sec_ans.place(x=600,y=250)

        self.select_sec_ans_entry=ttk.Entry(frame,textvariable=self.var_sec_ans,font=("SF Pro Display",15))
        self.select_sec_ans_entry.place(x=600,y=300,width=320,height=40)
        
        password=Label(frame,text="Password :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        password.place(x=50,y=350)

        self.password_entry=ttk.Entry(frame,textvariable=self.var_password,font=("SF Pro Display",15),show="*")
        self.password_entry.place(x=50,y=400,width=320,height=40)

        lname=Label(frame,text="Last Name :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        lname.place(x=600,y=50)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("SF Pro Display",15))
        self.lname_entry.place(x=600,y=100,width=320,height=40)

        email=Label(frame,text="Email :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        email.place(x=600,y=150)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("SF Pro Display",15))
        self.email_entry.place(x=600,y=200,width=320,height=40)

        confirm_pass=Label(frame,text="Confirm Password :",font=("SF Pro Display",15,"bold"),fg="white",bg="#5a5192")
        confirm_pass.place(x=600,y=350)

        self.confirm_pass_entry=ttk.Entry(frame,textvariable=self.var_confpassword,font=("SF Pro Display",15),show="*")
        self.confirm_pass_entry.place(x=600,y=400,width=320,height=40)

        regbtn=Button(frame,text="Register now",command=self.register_data,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#c30e89",activeforeground="white",activebackground="#c30e89")
        regbtn.place(x=410,y=480,width=150,height=45)


    #set on action
     

     def register_data(self):
        def validateMail(email):
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if(re.fullmatch(regex, email)):
                return TRUE
            else:
                return FALSE

        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_sec_ques.get()=="Select":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_password.get()!=self.var_confpassword.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
        elif validateMail(self.var_email.get())==False:
            messagebox.showerror("Error","Invalid email address",parent=self.root)
        elif len(self.confirm_pass_entry.get())<7:
            messagebox.showerror("Error","Password must be at least 7 characters",parent=self.root)
        else:
            conn=mysql.connector.connect(user="root", password="",host="localhost",database="student_management_system",port="3306")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist , please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),self.var_lname.get(),str(self.var_contact.get()),self.var_sec_ques.get(),self.var_sec_ans.get(),self.var_password.get(),self.var_email.get().lower()
                                                            ))
            conn.commit()
            conn.close()
            self.root.destroy()
            messagebox.showinfo("Success","Register Successful")

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,0)
        self.root.geometry("1500x1000+0+0")
        self.root.title("Admin Functions")

        img=Image.open(r"Admin Functions.jpg")
        img=img.resize((1550,1000),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(img) 
        f_lbl=Label(self.root,image=self.bgimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        student_details_btn=Button(self.root,command=self.student_details,text="Add Student Details",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        student_details_btn.place(x=142,y=430,width=210,height=45)

        face_recognize_btn=Button(self.root,command=self.face_reco,text="Face Recognition",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        face_recognize_btn.place(x=647,y=430,width=210,height=45)

        attendance_btn=Button(self.root,text="Attendance",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        attendance_btn.place(x=1135,y=430,width=210,height=45)

        train_data_btn=Button(self.root,command=self.train_data,text="Train Data",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        train_data_btn.place(x=382,y=740,width=210,height=45)

        exit_btn=Button(self.root,text="Exit",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        exit_btn.place(x=915,y=740,width=210,height=45)


    #function buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_reco(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Rec(self.new_window)




        



if __name__ == "__main__":
   main()