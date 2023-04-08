from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import re
import numpy as np
import cv2


class Train:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,0)
        self.root.geometry("1500x1000+0+0")
        self.root.title("Train Data")

        img=Image.open(r"Train data.png")
        img=img.resize((1500,1000),Image.ANTIALIAS)
        self.bgimg=ImageTk.PhotoImage(img) 
        f_lbl=Label(self.root,image=self.bgimg)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        train_btn=Button(self.root,command=self.train_classifier,text="Click Here to Train Data",font=("SF Pro Display",25,"bold"),bd=3,relief=RIDGE,fg="white",bg="#5ebfd9",activeforeground="white",activebackground="#5ebfd9")
        train_btn.place(x=355,y=400,width=810,height=65)


    def train_classifier(self):
        data_dir=("image_dataset")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        usns=[]

        for image in path:
            img=Image.open(image).convert('L') #img converted to grayscale image
            imageNp=np.array(img,'uint8')
            usnpre=str(os.path.split(image)[1].split('.')[1])
            numbers=re.findall(r'\d+', usnpre)
            string_numbers = [str(x) for x in numbers]
            result = ''.join(string_numbers)
            usn=int(result)
            faces.append(imageNp)
            usns.append(usn)
            cv2.imshow("Training",imageNp)
            
            cv2.waitKey(1)==13
        usns=np.array(usns) #conversting array takes much time thus we are using numpy where coverstion to array is 88% faster

        #training part
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,usns)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed",parent=self.root)


if __name__ == "__main__":
    win=Tk()
    app=Train(win)
    win.mainloop()