from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2 
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,0)
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance details")

        #text variables
        self.var_usn=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_dept=StringVar()
        self.var_sem=StringVar()
        self.var_div=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_att=StringVar()

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

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="#1e163b")
        left_inside_frame.place(x=5,y=25,width=740,height=300)

        #attendance id
        usn_label=Label(left_inside_frame,text="USN :", font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        usn_label.grid(row=0,column=0,padx=10,pady=5)

        usn_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_usn,font=("SF Pro Display",12,"bold"))
        usn_entry.grid(row=0,column=1,pady=8,sticky=W)

        student_label=Label(left_inside_frame,text="Name :", font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        student_label.grid(row=0,column=2,padx=10,pady=5)

        student_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_name,font=("SF Pro Display",12,"bold"))
        student_entry.grid(row=0,column=3,pady=8,sticky=W)

        dep_label=Label(left_inside_frame,text="Department :", font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        dep_label.grid(row=1,column=0,padx=10,pady=5)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_dept,font=("SF Pro Display",12,"bold"))
        dep_entry.grid(row=1,column=1,pady=8,sticky=W)

        course_label=Label(left_inside_frame,text="Course :", font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        course_label.grid(row=1,column=2,padx=10,pady=5)

        course_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_course,font=("SF Pro Display",12,"bold"))
        course_entry.grid(row=1,column=3,pady=8,sticky=W)

        semester_label=Label(left_inside_frame,text="Semester :", font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        semester_label.grid(row=2,column=0,padx=10,pady=5)

        semester_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_sem,font=("SF Pro Display",12,"bold"))
        semester_entry.grid(row=2,column=1,pady=8,sticky=W)

        div_label=Label(left_inside_frame,text="Division :", font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        div_label.grid(row=2,column=2,padx=10,pady=5)

        div_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_div,font=("SF Pro Display",12,"bold"))
        div_entry.grid(row=2,column=3,pady=8,sticky=W)

        time_label=Label(left_inside_frame,text="Time :", font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        time_label.grid(row=3,column=0,padx=10,pady=5)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_time,font=("SF Pro Display",12,"bold"))
        time_entry.grid(row=3,column=1,pady=8,sticky=W)

        date_label=Label(left_inside_frame,text="Date :", font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        date_label.grid(row=3,column=2,padx=10,pady=5)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_date,font=("SF Pro Display",12,"bold"))
        date_entry.grid(row=3,column=3,pady=8,sticky=W)

        attendanceLabel=Label(left_inside_frame,text="Attendance Status :", font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        attendanceLabel.grid(row=4,column=0,pady=10,padx=10)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_att,font=("SF Pro Display",12,"bold"), state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=4,column=1,pady=8,sticky=W)
        self.atten_status.current(0)

        btn_frame = Frame(left_inside_frame, bd=2,relief=RIDGE,bg="#1e163b")
        btn_frame.place(x=0,y=245,width=735,height=40)

        import_btn = Button(btn_frame,text="Import csv",command=self.importcsv,width=14,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame,text="Export csv",command=self.exportcsv,width=14,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        export_btn.grid(row=0,column=1)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=14,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        update_btn.grid(row=0,column=2)
        
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        reset_btn.grid(row=0,column=3)

        #right frame
        Right_frame=LabelFrame(main_frame,bg="#1e163b",bd=3,relief=RIDGE,text="Attendance Details",font=("SF Pro Display",15,"bold"),fg="white")
        Right_frame.place(x=765,y=10,width=650,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=640,height=455)

        #scrollbar

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("usn","name","course","department","semester","division","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("usn",text="USN")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("course",text="Course")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("semester",text="Semester")
        self.AttendanceReportTable.heading("division",text="Division")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("usn",width=150)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("course",width=150)
        self.AttendanceReportTable.column("department",width=150)
        self.AttendanceReportTable.column("semester",width=150)
        self.AttendanceReportTable.column("division",width=50)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=150)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    #fetch data

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV File",filetypes=(("CSV File",".csv"),("ALL File",".")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return FALSE
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV File",filetypes=(("CSV File",".csv"),("ALL File",".")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data is exported to "+os.path.basename(fln)+" successfully")  
        except Exception as e:
                messagebox.showerror("Error",f"Error due to :{str(e)}",parent=self.root)         

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_usn.set(rows[0])
        self.var_name.set(rows[1])
        self.var_course.set(rows[2])
        self.var_dept.set(rows[3])
        self.var_sem.set(rows[4])
        self.var_div.set(rows[5])
        self.var_time.set(rows[6])
        self.var_date.set(rows[7])
        self.var_att.set(rows[8])

    def reset_data(self):
        self.var_usn.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_dept.set("")
        self.var_sem.set("")
        self.var_div.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_att.set("")

    def update_data(self):
        if self.var_usn.get()=="" or self.var_name.get()=="" or self.var_course.get()=="" or self.var_dept.get()=="" or self.var_sem.get()=="" or self.var_div.get()=="" or self.var_time.get()=="" or self.var_att.get()=="Status" or self.var_date.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details ?",parent=self.root)
                if(Update>0):
                    with open('attendance.csv', mode='r') as file:
                        reader = csv.reader(file)
                        rows = list(reader)

                    # Find the index of the row containing the desired entry
                    for i, row in enumerate(rows):
                        if self.var_usn.get() in row:
                            index_to_update = i
                            break

                    # Update the entire row
                    new_row = [self.var_usn.get(),self.var_name.get(),self.var_course.get(),self.var_dept.get(),self.var_sem.get(),self.var_div.get(),self.var_time.get(),self.var_date.get(),self.var_att.get()]
                    rows[index_to_update] = new_row

                    # Write the updated rows back to the CSV file
                    with open('attendance.csv', mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(rows)
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Attendance details successfully updated",parent=self.root)
                self.fetchData(rows)
                
            except Exception as e:
                messagebox.showerror("Error",f"Error due to :{str(e)}",parent=self.root)
        
        
        








        



if __name__ == "__main__":
    win=Tk()
    app=Attendance(win)
    win.mainloop()