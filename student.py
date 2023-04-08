from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2 



class Student:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,0)
        self.root.geometry("1500x1000+0+0")
        self.root.title("Student details")

        #variables
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_course=StringVar()
        self.var_sem=StringVar()
        self.var_usn=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_mail=StringVar()
        self.var_tname=StringVar()
        self.var_combosearch=StringVar()
        self.var_search=StringVar()





        img=Image.open(r"student details bg.png")
        img=img.resize((1500,1000),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(img) 
        f_lbl=Label(self.root,image=self.bgimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        main_frame=Frame(self.root,bd=2,bg="#1e163b")
        main_frame.place(x=0,y=205,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bg="#1e163b",bd=3,relief=RIDGE,text="Student Details",font=("SF Pro Display",15,"bold"),fg="white")
        Left_frame.place(x=10,y=10,width=750,height=580)

        Course_frame=LabelFrame(Left_frame,bg="#1e163b",bd=2,relief=RIDGE,text="Current Course",font=("SF Pro Display",13,"bold"),fg="white")
        Course_frame.place(x=5,y=25,width=720,height=140)

        dep_label=Label(Course_frame,text="Department :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Course_frame,textvariable=self.var_dep,font=("SF Pro Display",12),width=15,state="readonly")
        dep_combo['values']=("Select Department","Computer Science","Information Science","Electronics and Communication","Electrical and Electronics","Mechanical","Civil","Chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        year_label=Label(Course_frame,text="Year :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        year_label.grid(row=0,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(Course_frame,textvariable=self.var_year,font=("SF Pro Display",12),width=15,state="readonly")
        year_combo['values']=("Select Year","First Year","Second Year","Third Year","Final year")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        Course_label=Label(Course_frame,text="Course Name :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        Course_label.grid(row=1,column=0,padx=10,sticky=W)

        Course_txt=ttk.Entry(Course_frame,textvariable=self.var_course,font=("SF Pro Display",12,"bold"))
        Course_txt.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        sem_label=Label(Course_frame,text="Semester :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(Course_frame,textvariable=self.var_sem,font=("SF Pro Display",12,"bold"),width=15,state="readonly")
        sem_combo['values']=("Select Semester","First Semester","Second Semester","Third Semester","Fourth Semester","Fifth Semester","Sixth Semester","Seventh Semester","Eighth Semester")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        Student_frame=LabelFrame(Left_frame,bg="#1e163b",bd=2,relief=RIDGE,text="Class Student Information",font=("SF Pro Display",13,"bold"),fg="white")
        Student_frame.place(x=5,y=175,width=740,height=600)

        usn_label=Label(Student_frame,text="Student USN :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        usn_label.grid(row=0,column=0,padx=10,sticky=W)

        usn_entry=ttk.Entry(Student_frame,textvariable=self.var_usn,width=20,font=("SF Pro Display",12,"bold"))
        usn_entry.grid(row=0,column=1,padx=10,sticky=W)

        name_label=Label(Student_frame,text="Student Name :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        name_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        name_entry=ttk.Entry(Student_frame,textvariable=self.var_name,width=20,font=("SF Pro Display",12,"bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        div_label=Label(Student_frame,text="Class Division :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        div_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        div_entry=ttk.Entry(Student_frame,textvariable=self.var_div,width=20,font=("SF Pro Display",12))
        div_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        gender_label=Label(Student_frame,text="Gender :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        gender_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        gen_combo=ttk.Combobox(Student_frame,textvariable=self.var_gender,font=("SF Pro Display",12),width=15,state="readonly")
        gen_combo['values']=("Select Gender","Male","Female")
        gen_combo.current(0)
        gen_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        dob_label=Label(Student_frame,text="Date Of Birth :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        dob_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        # dob_entry=ttk.DateEntry(Student_frame)
        dob_entry=ttk.Entry(Student_frame,textvariable=self.var_dob,width=20,font=("SF Pro Display",12))
        dob_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        mail_label=Label(Student_frame,text="Mail ID :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        mail_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        mail_entry=ttk.Entry(Student_frame,textvariable=self.var_mail,width=20,font=("SF Pro Display",12))
        mail_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        phone_label=Label(Student_frame,text="Phone No :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        phone_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        phone_entry=ttk.Entry(Student_frame,textvariable=self.var_phone,width=20,font=("SF Pro Display",12))
        phone_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        tname_label=Label(Student_frame,text="Teacher Name :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        tname_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        tname_entry=ttk.Entry(Student_frame,textvariable=self.var_tname,width=20,font=("SF Pro Display",12))
        tname_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        radiolbl1=Label(Student_frame,text="Take a Photo Sample :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        radiolbl1.grid(row=4,column=0)
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=1,pady=10)

        radiolbl2=Label(Student_frame,text="No Photo Sample :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        radiolbl2.grid(row=4,column=2)
        radiobtn2=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=4,column=3,pady=10)

        btn_frame = Frame(Student_frame, bd=2,relief=RIDGE,bg="#1e163b")
        btn_frame.place(x=0,y=240,width=720,height=50)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=14,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,command=self.update_data,text="Update",width=14,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,command=self.delete_data,text="Delete",width=14,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        delete_btn.grid(row=0,column=2)
        
        reset_btn = Button(btn_frame,command=self.reset_data,text="Reset",width=14,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(Student_frame, bd=2,relief=RIDGE,bg="#1e163b")
        btn_frame1.place(x=0,y=290,width=720,height=50)

        take_photosamp_btn = Button(btn_frame1,command=self.generate_dataset,text="Take photo sample",width=30,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        take_photosamp_btn.grid(row=0,column=0)

        update_photosamp_btn = Button(btn_frame1,command=self.generate_dataset,text="Update photo sample",width=30,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        update_photosamp_btn.grid(row=0,column=2)


        #right label frame
        Right_frame=LabelFrame(main_frame,bg="#1e163b",bd=3,relief=RIDGE,text="Student Details",font=("SF Pro Display",15,"bold"),fg="white")
        Right_frame.place(x=765,y=10,width=720,height=580)

        Search_frame=LabelFrame(Right_frame,bg="#1e163b",bd=2,relief=RIDGE,text="Search System",font=("SF Pro Display",13,"bold"),fg="white")
        Search_frame.place(x=5,y=25,width=710,height=75)

        search_label=Label(Search_frame,text="Search by :",font=("SF Pro Display",12,"bold"),fg="white",bg="#1e163b")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_combosearch,state="readonly",font=("SF Pro Display",12),width=15)
        search_combo['values']=("Select Search type","USN","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=15,font=("SF Pro Display",12))
        search_entry.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        search_btn = Button(Search_frame,command=self.search_data,text="Search",width=8,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn = Button(Search_frame,command=self.fetch_data,text="Show All",width=8,font=("SF Pro Display",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        showAll_btn.grid(row=0,column=4)

        #table frame
        Table_frame=Frame(Right_frame,bg="white",bd=2,relief=RIDGE)
        Table_frame.place(x=5,y=120,width=710,height=400)

        Scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(Table_frame,column=('Year','USN','Department','Course','Semester','Name','Division','Gender','Date Of Birth','Phone No','Mail ID','Teacher Name','Photo'),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Year",text="Year")
        self.student_table.heading("USN",text="USN")
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Teacher Name",text="Teacher Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Mail ID",text="Mail ID")
        self.student_table.heading("Date Of Birth",text="Date Of Birth")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=150)
        self.student_table.column("Name",width=150)
        self.student_table.column("Division",width=70)
        self.student_table.column("Teacher Name",width=150)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=70)
        self.student_table.column("Semester",width=150)
        self.student_table.column("USN",width=100)
        self.student_table.column("Phone No",width=100)
        self.student_table.column("Mail ID",width=200)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Date Of Birth",width=100)
        self.student_table.column("Photo",width=70)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



#function decraTION
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_usn.get()=="" or self.var_usn.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_year.get(),
                    self.var_usn.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone.get(),
                    self.var_mail.get(),
                    self.var_tname.get(),
                    self.var_radio1.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)


#fetch data to table
    def fetch_data(self):
        conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    #get cursor

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_year.set(data[0])
        self.var_usn.set(data[1])
        self.var_dep.set(data[2])
        self.var_course.set(data[3])
        self.var_sem.set(data[4])
        self.var_name.set(data[5])
        self.var_div.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_phone.set(data[9])
        self.var_mail.set(data[10])
        self.var_tname.set(data[11])
        self.var_radio1.set(data[12])

    #generate dataset foe training images for model to recognize face
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_usn.get()=="" or self.var_usn.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=self.var_usn.get()
                if(id==""):
                    messagebox.showerror("Error","USN Field are required",parent=self.root)
                else:
                    for x in myresult:
                        my_cursor.execute("Update student set Year=%s,Department=%s,Course=%s,Semester=%s,Name=%s,Division=%s,Gender=%s,DOB=%s,Phone=%s,Mail=%s,Teacher=%s,Photo=%s where USN=%s",(
                            self.var_year.get(),
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_sem.get(),
                            self.var_name.get(),
                            self.var_div.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_phone.get(),
                            self.var_mail.get(),
                            self.var_tname.get(),
                            self.var_radio1.get(),
                            self.var_usn.get()
                            ))
                        conn.commit()
                        self.fetch_data()
                        self.reset_data() 
                        conn.close()

                        #loading predifined data on face frontals from opencv

                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def face_cropped(img):
                            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            faces=face_classifier.detectMultiScale(gray,1.3,5)
                            #scaling factor=1.3 and minimum neighbors=5
                            for (x,y,w,h) in faces:
                                face_cropped=img[y:y+h,x:x+w]
                                return face_cropped
                        
                        cap=cv2.VideoCapture(0) #0 for inbuilt webcam open is other cam to open then 1
                        img_id=0
                        while True:
                            ret,my_frame=cap.read()
                            if face_cropped(my_frame) is not None:
                                img_id+=1
                                face=cv2.resize(face_cropped(my_frame),(450,450))
                                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                file_name_path="image_dataset/user."+str(id)+"."+str(img_id)+".jpg"
                                cv2.imwrite(file_name_path,face)
                                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                cv2.imshow("Cropped Face",face)

                            if cv2.waitKey(1) == 13 or int(img_id)==100:
                                break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Generating Dataset completed",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Error due to :{str(e)}",parent=self.root)      

                           


    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_usn.get()=="" or self.var_usn.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details ?",parent=self.root)
                if(Update>0):
                    conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
                    my_cursor=conn.cursor() 
                    my_cursor.execute("Update student set Year=%s,Department=%s,Course=%s,Semester=%s,Name=%s,Division=%s,Gender=%s,DOB=%s,Phone=%s,Mail=%s,Teacher=%s,Photo=%s where USN=%s",(
                    self.var_year.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_sem.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone.get(),
                    self.var_mail.get(),
                    self.var_tname.get(),
                    self.var_radio1.get(),
                    self.var_usn.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to :{str(e)}",parent=self.root)      

    #delete function
    def delete_data(self):
        if self.var_usn.get()=="":
            messagebox.showerror("Error","Student USN is required to delete student information",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Message","Do you want to delete information about this student ?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
                    my_cursor=conn.cursor()
                    query="delete from student where USN=%s"
                    val=(self.var_usn.get(),)
                    my_cursor.execute(query, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Error due to :{str(e)}",parent=self.root)      

        #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_course.set("")
        self.var_sem.set("Select Semester")
        self.var_usn.set("")
        self.var_name.set("")
        self.var_div.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_mail.set("")
        self.var_phone.set("")
        self.var_tname.set("")
        self.var_radio1.set("No")


    #search functions
    def search_data(self):
        if self.var_combosearch.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please enter search type and data")
        else:
            try:
                conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_combosearch.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data :
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to :{str(e)}",parent=self.root)      
            









        












        

if __name__ == "__main__":
    win=Tk()
    app=Student(win)
    win.mainloop()