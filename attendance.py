from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2 



class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,0)
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance details")

        img=Image.open(r"attendance information bg.png")
        img=img.resize((1500,1000),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(img) 
        f_lbl=Label(self.root,image=self.bgimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        main_frame=Frame(self.root,bd=2,bg="#1e163b")
        main_frame.place(x=0,y=155,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bg="#1e163b",bd=3,relief=RIDGE,text="Student Attendance Details",font=("SF Pro Display",15,"bold"),fg="white")
        Left_frame.place(x=10,y=10,width=750,height=580)

        Right_frame=LabelFrame(main_frame,bg="#1e163b",bd=3,relief=RIDGE,text="Attendance Details",font=("SF Pro Display",15,"bold"),fg="white")
        Right_frame.place(x=765,y=10,width=720,height=580)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="#1e163b")
        left_inside_frame.place(x=5,y=25,width=720,height=300)

        #attendance id
        attendanceid_label=Label(left_inside_frame,text="Attendance ID :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceid_entry=ttk.Entry(left_inside_frame,width=20,font=("SF Pro Display",12,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


if __name__ == "__main__":
    win=Tk()
    app=Attendance(win)
    win.mainloop()