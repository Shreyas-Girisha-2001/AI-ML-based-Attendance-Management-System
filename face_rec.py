from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
from time import strftime

from datetime import datetime
import cv2

def convert_to_string(data):
    # Convert the data to a string
    string_data = str(data)
    
    # Remove the specified characters
    string_data = string_data.replace(",", "")
    string_data = string_data.replace("'", "")
    string_data = string_data.replace('"', '')
    string_data = string_data.replace("(", "")
    string_data = string_data.replace(")", "")
    
    # Return the resulting string
    return string_data


class Face_Rec:
    def __init__(self,root):
        self.root=root
        self.root.resizable(1920,1080)
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognizer")

        img=Image.open(r"Recognize Face.png")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(img) 
        f_lbl=Label(self.root,image=self.bgimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        
        exrec_btn=Button(self.root,command=self.face_recognition_externalcam,text="Click Here to Recognize Faces using external camera",font=("SF Pro Display",25,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        exrec_btn.place(x=355,y=400,width=810,height=65)

        inrec_btn=Button(self.root,command=self.face_recognition_internalcam,text="Click Here to Recognize Faces using default camera",font=("SF Pro Display",25,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        inrec_btn.place(x=355,y=500,width=810,height=65)


    def mark_attendance(self,usn,name,course,sem,div,dept):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
                #to avoid duplicates
            if((usn not in name_list) and (name not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstr=now.strftime("%H:%M:%S")
                f.writelines(f"{usn},{name},{course},{dept},{sem},{div},{dtstr},{d1},Present\n")


    #face recognition function

    def face_recognition_externalcam(self):
        def draw_boundary(img,classifier,scalefactor,minneighbor,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minneighbor)
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                ids,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                number_array = list(str(ids))
                getusn=str(number_array[0])+"SD"+str(number_array[1])+""+str(number_array[2])+"CS"+str(number_array[3])+""+str(number_array[4])+""+str(number_array[5])
                conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
                my_cursor=conn.cursor()
                namequery="select Name from student where USN=%s"
                subjectquery="select Course from student where USN=%s"
                deptquery="select Department from student where USN=%s"
                semquery="select Semester from student where USN=%s"
                divquery="select Division from student where USN=%s"

                my_cursor.execute(namequery,(getusn,))
                name=my_cursor.fetchone()

                my_cursor.execute(subjectquery,(getusn,))
                course=my_cursor.fetchone()

                my_cursor.execute(deptquery,(getusn,))
                dept=my_cursor.fetchone()

                my_cursor.execute(semquery,(getusn,))
                sem=my_cursor.fetchone()
           
                my_cursor.execute(divquery,(getusn,))
                div=my_cursor.fetchone()
                
                print(confidence)

                if confidence>88:
                    cv2.putText(img,'Present',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(getusn,convert_to_string(name),convert_to_string(course),convert_to_string(sem),convert_to_string(div),convert_to_string(dept))
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            try:
                coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            except Exception as e:
                 error_message = "Error occurred while recognizing faces:\n" + str(e)
                 messagebox.showerror("Error", error_message)
                 coord = [] 
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(1)
        video_cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        video_cap.set(cv2.CAP_PROP_FRAME_WIDTH,720)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    def face_recognition_internalcam(self):
        def draw_boundary(img,classifier,scalefactor,minneighbor,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minneighbor)
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                ids,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                number_array = list(str(ids))
                getusn=str(number_array[0])+"SD"+str(number_array[1])+""+str(number_array[2])+"CS"+str(number_array[3])+""+str(number_array[4])+""+str(number_array[5])
                conn=mysql.connector.connect(user="root", password="root",host="localhost",database="student_management_system",port="8889")
                my_cursor=conn.cursor()
                namequery="select Name from student where USN=%s"
                subjectquery="select Course from student where USN=%s"
                semquery="select Semester from student where USN=%s"
                divquery="select Division from student where USN=%s"
                my_cursor.execute(namequery,(getusn,))
                name=my_cursor.fetchone()


                my_cursor.execute(subjectquery,(getusn,))
                course=my_cursor.fetchone()


                my_cursor.execute(semquery,(getusn,))
                sem=my_cursor.fetchone()


                my_cursor.execute(divquery,(getusn,))
                div=my_cursor.fetchone()

                print(confidence)

                if confidence>80:
                    cv2.putText(img,f'Present',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(getusn,convert_to_string(name),convert_to_string(course),convert_to_string(sem),convert_to_string(div),"Computer Science")
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,y]
            return coord
        
        def recognize(img,clf,faceCascade):
            try:
                coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            except Exception as e:
                 error_message = "Error occurred while recognizing faces:\n" + str(e)
                 messagebox.showerror("Error", error_message)
                 coord = []
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    




if __name__ == "__main__":
    win=Tk()
    app=Face_Rec(win)
    win.mainloop()