from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.resizable(1920,1080)
        self.root.geometry("1500x1000+0+0")
        self.root.title("Admin Functions")

        img=Image.open(r"Admin Functions.jpg")
        img=img.resize((1550,1000),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(img) 
        f_lbl=Label(self.root,image=self.bgimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        student_details_btn=Button(self.root,text="Add Student Details",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        student_details_btn.place(x=142,y=430,width=210,height=45)

        face_recognize_btn=Button(self.root,text="Face Recognition",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        face_recognize_btn.place(x=647,y=430,width=210,height=45)

        attendance_btn=Button(self.root,text="Attendance",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        attendance_btn.place(x=1135,y=430,width=210,height=45)

        train_data_btn=Button(self.root,text="Train Data",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        train_data_btn.place(x=382,y=740,width=210,height=45)

        exit_btn=Button(self.root,text="Exit",font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        exit_btn.place(x=915,y=740,width=210,height=45)
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()