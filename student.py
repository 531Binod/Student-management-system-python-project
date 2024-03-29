from tkinter import*
from tkinter import ttk

from PIL import Image,ImageTk   #pip install pillow
import mysql.connector
from tkinter import messagebox


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_stdid=StringVar()
        self.var_stdname=StringVar()
        self.var_regid=StringVar()
        self.var_roll=StringVar()
        self.var_dob=StringVar()
        self.var_section=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_phn=StringVar()
        self.var_adhr=StringVar()



        #firstimage of student group
        img=Image.open(r"images\images.jpg")
        img=img.resize((460,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=460,height=120)

        #2nd_image of university 
        img_2=Image.open(r"images\image2.webp")
        img_2=img_2.resize((460,160),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        self.btn_2=Button(self.root,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=460,y=0,width=460,height=120)

        #3rd_image of student group
        img_3=Image.open(r"images\2019-08-23.jpg")
        img_3=img_3.resize((460,160),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)
        self.btn_3=Button(self.root,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=920,y=0,width=460,height=120)

        #Background image
        img_4=Image.open(r"images\mdu.jpg")
        img_4=img_4.resize((1500,700),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)
        bg_lb1=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lb1.place(x=0,y=120,width=1500,height=700)

        lb_title=Label(bg_lb1,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",36,"bold"),fg="blue",bg="white")
        lb_title.place(x=0,y=0,width=1500,height=40)

        #Main Frame design , not labelframe
        bigger_frame=Frame(bg_lb1,bd=3,relief=RIDGE,bg="white")
        bigger_frame.place(x=20,y=45,width=1300,height=500)

        #Left labelframe
        leftLbframe=LabelFrame(bigger_frame,bd=2,relief=RIDGE,padx=2,text="Student information",font=("times new roman",12,"bold"),fg="red",bg="white")
        leftLbframe.place(x=10,y=8,width=550,height=485)

        #image_inside_leftframe
        img_5=Image.open(r"images\6th.jpg")
        img_5=img_5.resize((540,100),Image.ANTIALIAS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)
        my_image=Label(leftLbframe,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_image.place(x=0,y=0,width=540,height=100)

        

        #current course labelframe
        currentLeftLbframe=LabelFrame(leftLbframe,bd=2,relief=RIDGE,padx=2,text="Your current course detail",font=("times new roman",12,"bold"),fg="red",bg="white")
        currentLeftLbframe.place(x=2,y=100,width=540,height=110)

       
        #CourseLabel
        course_lb1=Label(currentLeftLbframe,text="Course",font=("arial",11,"bold"),bg="white")
        course_lb1.grid(row=0,column=0,padx=2,sticky=W)
        #Course_comboBox
        combo_course=ttk.Combobox(currentLeftLbframe,textvariable=self.var_course,font=("arial",11,"bold"),width=17,state="readonly")
        combo_course["value"]=("Select Course","B-Tech","M-Tech","Bsc","M.Sc","BCA","MCA")
        combo_course.current(0)
        combo_course.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #DeparmentLabel
        dep_lb1=Label(currentLeftLbframe,text="Depatment",font=("arial",11,"bold"),bg="white")
        dep_lb1.grid(row=0,column=2,padx=20,sticky=W)
        #Department_comboBox
        combo_dep=ttk.Combobox(currentLeftLbframe,textvariable=self.var_dep,font=("arial",11,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","CSE","ME","civil","Biotech","ECE","Mathematics","Physics")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #YearLabel
        year_lb1=Label(currentLeftLbframe,text="Year",font=("arial",11,"bold"),bg="white")
        year_lb1.grid(row=1,column=0,padx=2,sticky=W)
        #year_comboBox
        combo_year=ttk.Combobox(currentLeftLbframe,textvariable=self.var_year,font=("arial",11,"bold"),width=17,state="readonly")
        combo_year["value"]=("Select Year ","2015-2016","2016-2017","2017-2018","2018-2019","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025")
        combo_year.current(0)
        combo_year.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #SemesterLabel
        sem_lb1=Label(currentLeftLbframe,text="Semester",font=("arial",11,"bold"),bg="white")
        sem_lb1.grid(row=1,column=2,padx=20,sticky=W)
        #Semester_comboBox
        combo_sem=ttk.Combobox(currentLeftLbframe,textvariable=self.var_sem,font=("arial",11,"bold"),width=17,state="readonly")
        combo_sem["value"]=("Select Semester ","sem-1","sem-2","sem-3","sem-4","sem-5","sem-6","sem-7","sem-8")
        combo_sem.current(0)
        combo_sem.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #StudentInformationLabelframe
        StudentClassInformationLbframe=LabelFrame(leftLbframe,bd=2,relief=RIDGE,padx=2,text="Student class Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        StudentClassInformationLbframe.place(x=2,y=215,width=540,height=220)

        #IdLabel
        id_lb1=Label(StudentClassInformationLbframe,text="Student_ID:",font=("arial",11,"bold"),bg="white")
        id_lb1.grid(row=0,column=0,padx=2,pady=8,sticky=W)
        #IdEntry
        id_entry=ttk.Entry(StudentClassInformationLbframe,textvariable=self.var_stdid,font=("arial",11,"bold"),width=17)
        id_entry.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        #NameLabel
        name_lb1=Label(StudentClassInformationLbframe,text="Student Name:",font=("arial",11,"bold"),bg="white")
        name_lb1.grid(row=0,column=2,padx=2,pady=8,sticky=W)
        #NameEntry
        name_entry=ttk.Entry(StudentClassInformationLbframe,textvariable=self.var_stdname,font=("arial",11,"bold"),width=17)
        name_entry.grid(row=0,column=3,padx=2,pady=8,sticky=W)

        #Reg_idLabel
        reg_lb1=Label(StudentClassInformationLbframe,text="Regitration_ID:",font=("arial",11,"bold"),bg="white")
        reg_lb1.grid(row=1,column=0,padx=2,pady=8,sticky=W)
        #Reg_IdEntry
        reg_entry=ttk.Entry(StudentClassInformationLbframe,textvariable=self.var_regid,font=("arial",11,"bold"),width=17)
        reg_entry.grid(row=1,column=1,padx=2,pady=8,sticky=W)

        #ROllLabel
        roll_lb1=Label(StudentClassInformationLbframe,text="Class Roll no:",font=("arial",11,"bold"),bg="white")
        roll_lb1.grid(row=1,column=2,padx=2,pady=8,sticky=W)
        #RollEntry
        id_entry=ttk.Entry(StudentClassInformationLbframe,textvariable=self.var_roll,font=("arial",11,"bold"),width=17)
        id_entry.grid(row=1,column=3,padx=2,pady=8,sticky=W)

        #SectionLabel
        section_lb1=Label(StudentClassInformationLbframe,text="Section:",font=("arial",11,"bold"),bg="white")
        section_lb1.grid(row=2,column=2,padx=2,pady=8,sticky=W)
        #section_combo
        sec_combo=ttk.Combobox(StudentClassInformationLbframe,textvariable=self.var_section,state="readonly",font=("arial",11,"bold"),width=15)
        sec_combo["value"]=("Select Section","A","B","C","D")
        sec_combo.current(0)
        sec_combo.grid(row=2,column=3,padx=2,pady=8,sticky=W)

        #GenderLabel
        gend_lb1=Label(StudentClassInformationLbframe,text="Gender:",font=("arial",11,"bold"),bg="white")
        gend_lb1.grid(row=3,column=2,padx=2,pady=8,sticky=W)
        #Gender_combo
        gend_combo=ttk.Combobox(StudentClassInformationLbframe,textvariable=self.var_gender,font=("arial",11,"bold"),width=15)
        gend_combo["value"]=("Select Gender","Male","Female","Other")
        gend_combo.current(0)
        gend_combo.grid(row=3,column=3,padx=2,pady=8,sticky=W)

        #DOBLabel
        dob_lb1=Label(StudentClassInformationLbframe,text="D.O.B:",font=("arial",11,"bold"),bg="white")
        dob_lb1.grid(row=2,column=0,padx=2,pady=8,sticky=W)
        #DOBEntry
        dob_entry=ttk.Entry(StudentClassInformationLbframe,textvariable=self.var_dob,font=("arial",11,"bold"),width=17)
        dob_entry.grid(row=2,column=1,padx=2,pady=8,sticky=W)

        #MailLabel
        ml_lb1=Label(StudentClassInformationLbframe,text="Email:",font=("arial",11,"bold"),bg="white")
        ml_lb1.grid(row=3,column=0,padx=2,pady=8,sticky=W)
        #MailEntry
        ml_entry=ttk.Entry(StudentClassInformationLbframe,textvariable=self.var_email,font=("arial",11,"bold"),width=17)
        ml_entry.grid(row=3,column=1,padx=2,pady=8,sticky=W)

        #PhoneLabel
        phn_lb1=Label(StudentClassInformationLbframe,text="Phone Number:",font=("arial",11,"bold"),bg="white")
        phn_lb1.grid(row=4,column=0,padx=2,pady=8,sticky=W)
        #PhoneEntry
        phn_entry=ttk.Entry(StudentClassInformationLbframe,textvariable=self.var_phn,font=("arial",11,"bold"),width=17)
        phn_entry.grid(row=4,column=1,padx=2,pady=8,sticky=W)

        #AadharLabel
        adh_lb1=Label(StudentClassInformationLbframe,text="Aadhar number:",font=("arial",11,"bold"),bg="white")
        adh_lb1.grid(row=4,column=2,padx=2,pady=8,sticky=W)
        #AadharEntry
        adh_entry=ttk.Entry(StudentClassInformationLbframe,textvariable=self.var_adhr,font=("arial",11,"bold"),width=17)
        adh_entry.grid(row=4,column=3,padx=2,pady=8,sticky=W)

        #ButtonFrame
        btn_frame=Frame(leftLbframe,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=435,width=540,height=25)

        #add Button
        btn1=Button(btn_frame,text="Save",command=self.add_data,font=("arial",10,"bold"),width=15,bg="blue",fg="white")
        btn1.grid(row=0,column=0,padx=1)

        btn2=Button(btn_frame,text="Update",command=self.update_data,font=("arial",10,"bold"),width=15,bg="blue",fg="white")
        btn2.grid(row=0,column=1,padx=1)

        btn3=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",10,"bold"),width=16,bg="blue",fg="white")
        btn3.grid(row=0,column=2,padx=1)

        btn4=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",10,"bold"),width=15,bg="blue",fg="white")
        btn4.grid(row=0,column=3,padx=1)

        #Right labelframe
        rightLbframe=LabelFrame(bigger_frame,bd=2,relief=RIDGE,padx=2,text="Information about all Student",font=("times new roman",12,"bold"),fg="red",bg="white")
        rightLbframe.place(x=580,y=8,width=700,height=485)

        #image_inside_rightLbframe
        img_6=Image.open(r"images\images (1).jpg")
        img_6=img_6.resize((690,100),Image.ANTIALIAS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)
        my_image1=Label(rightLbframe,image=self.photoimg_6,bd=2,relief=RIDGE)
        my_image1.place(x=0,y=0,width=690,height=100)

        lb_title2=Label(rightLbframe,text="MAHARSHI DAYANAND UNIVERSITY , Rohtak",font=("times new roman",18,"bold"),fg="black",bg="white")
        lb_title2.place(x=10,y=110,width=680,height=20)

        #search labelFrame
        srchLbframe=LabelFrame(rightLbframe,bd=2,relief=RIDGE,padx=2,text="Search student information",font=("times new roman",12,"bold"),fg="red",bg="white")
        srchLbframe.place(x=10,y=130,width=680,height=70)

        #srchlabel
        srch_lb=Label(srchLbframe,text="Search By:",font=("arial",11,"bold"),bg="white")
        srch_lb.grid(row=0,column=0,padx=2,sticky=W)
        #Search by_comboBox
        self.var_combo_search=StringVar()        #variable for combobox
        
        combo_srch=ttk.Combobox(srchLbframe,textvariable=self.var_combo_search,font=("arial",11,"bold"),width=15,state="readonly")
        combo_srch["value"]=("Select Option ","Student_ID","Registration_ID")
        combo_srch.current(0)
        combo_srch.grid(row=0,column=1,padx=2,sticky=W)
        #search_entry
        self.var_search=StringVar()    #variable for entry field

        srch_entry=ttk.Entry(srchLbframe,textvariable=self.var_search,font=("arial",11,"bold"),width=20)
        srch_entry.grid(row=0,column=2,padx=2,sticky="w")
        #search_Button
        srch_btn1=Button(srchLbframe,command=self.search_data,text="Search",font=("arial",10,"bold"),width=15,bg="blue",fg="white")
        srch_btn1.grid(row=0,column=3,padx=1)
        #show_all Button
        srch_btn2=Button(srchLbframe,command=self.fetch_data,text="Show All",font=("arial",10,"bold"),width=15,bg="blue",fg="white")
        srch_btn2.grid(row=0,column=4,padx=1)

        #============Student Table and scroll bar============
        #table Frame
        tbl_frame=Frame(rightLbframe,bd=5,relief=RIDGE)
        tbl_frame.place(x=10,y=210,width=680,height=250)

        #Scrollbar
        scroll_x=ttk.Scrollbar(tbl_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frame,orient=VERTICAL)
        #Treeview(heading of table(it can be dummy ))
        self.student_table=ttk.Treeview(tbl_frame,columns=("dep","course","reg_id","std_id","name","year","sem","roll_no","section","dob","Gender","Email","phone","Aadhar"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #PACK
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        #config
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        #Heading
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("reg_id",text="Registration_ID")
        self.student_table.heading("std_id",text="Student_ID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("roll_no",text="Class Roll no")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("phone",text="Phone number")
        self.student_table.heading("Aadhar",text="Aadhar number")
        
        self.student_table["show"]="headings" #to start from x=0
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("reg_id",width=100)
        self.student_table.column("std_id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("Aadhar",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (self.var_dep.get()=="" or self.var_regid.get()=="" or self.var_stdid.get()=="" or self.var_roll.get()=="" or self.var_phn.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Binod@1234',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                        self.var_dep.get(),
                                                        self.var_course.get(),
                                                        self.var_regid.get(),
                                                        self.var_stdid.get(),
                                                        self.var_stdname.get(),
                                                        self.var_year.get(),
                                                        self.var_sem.get(),
                                                        self.var_roll.get(),
                                                        self.var_section.get(),
                                                        self.var_dob.get(),
                                                        self.var_gender.get(),
                                                        self.var_email.get(),
                                                        self.var_phn.get(),
                                                        self.var_adhr.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Fetch function
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Binod@1234',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # function  to show all data by clicking the row of table with the help of cursor
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_regid.set(data[2])
        self.var_stdid.set(data[3])
        self.var_stdname.set(data[4])
        self.var_year.set(data[5])
        self.var_sem.set(data[6])
        self.var_roll.set(data[7])
        self.var_section.set(data[8])
        self.var_dob.set(data[9])
        self.var_gender.set(data[10])
        self.var_email.set(data[11])
        self.var_phn.set(data[12])
        self.var_adhr.set(data[13])

    #update
    def update_data(self):
        if (self.var_dep.get()=="" or self.var_regid.get()=="" or self.var_stdid.get()=="" or self.var_roll.get()=="" or self.var_phn.get()==""):
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are You sure to update this content",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Binod@1234',database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Registration_Id=%s,Student_Name=%s,Year=%s,Semester=%s,Roll_No=%s,Section=%s,dob=%s,Gender=%s,Email=%s,Phone_no=%s,Aadhar_no=%s where Student_Id=%s",(
                                                      self.var_dep.get(),
                                                      self.var_course.get(),
                                                      self.var_regid.get(),
                                                      self.var_stdname.get(),
                                                      self.var_year.get(),
                                                      self.var_sem.get(),
                                                      self.var_roll.get(),
                                                      self.var_section.get(),
                                                      self.var_dob.get(),
                                                      self.var_gender.get(),
                                                      self.var_email.get(),
                                                      self.var_phn.get(),
                                                      self.var_adhr.get(),
                                                      self.var_stdid.get()
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Delete
    def delete_data(self):
        if (self.var_dep.get()=="" or self.var_regid.get()=="" or self.var_stdid.get()=="" or self.var_roll.get()=="" or self.var_phn.get()==""):
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are You sure to delete this content",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Binod@1234',database='mydata')
                    my_cursor=conn.cursor()
                    sql="delete from student where student_Id=%s"
                    Value=(self.var_stdid.get(),)
                    my_cursor.execute(sql,Value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your Student has been deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_regid.set("")
        self.var_stdid.set("")
        self.var_stdname.set("")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_roll.set("")
        self.var_section.set("Select Section")
        self.var_dob.set("")
        self.var_gender.set("Select Gender")
        self.var_email.set("")
        self.var_phn.set("")
        self.var_adhr.set("")

    #Search
    def search_data(self):
        if self.var_combo_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Binod@1234',database='mydata')
                my_cursor=conn.cursor()
        
                my_cursor.execute("select * from student where "+str(self.var_combo_search.get())+" LIKE '"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        
     
if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()


