from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.Expdate = StringVar()
        self.Dailydose = StringVar()
        self.Sideeffect = StringVar()
        self.FurtherInfo = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsnumber = StringVar()
        self.PatientName = StringVar()
        self.DOB = StringVar()
        self.PatientAddress = StringVar()
        
        
        lbltitle = Label(self.root ,bd = 20, relief= RIDGE, text = "HOSPITAL MANAGEMENT SYSTEM", fg = "dark blue" , bg = "white", font = ("times new roman",50,"bold")) 
        lbltitle.pack(side = TOP, fill = X)
        
        #========================Dataframe=====================
        
        Dataframe = Frame(self.root, bd = 20, relief = RIDGE)
        Dataframe.place(x=0, y=130, width = 1530, height=400)
        
        DataframeLeft = LabelFrame(Dataframe, bd = 10, relief = RIDGE, padx = 10, fg = "dark blue", font=("arial",15,"bold"), text ="Patient Information")
        DataframeLeft.place(x=0, y=5, width = 980, height = 350)
        
        DataframeRight = LabelFrame(Dataframe, bd = 10, relief = RIDGE, padx = 10, fg = "dark blue", font=("arial",15,"bold"), text ="Prescription")
        DataframeRight.place(x=990, y=5, width = 500, height = 350)
        
        #=====================Button frame===================
        
        Buttonframe = Frame(self.root, bd = 20, relief = RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)        
        
        #====================Details Frame===================
        
        Detailsframe = Frame(self.root, bd = 20, relief = RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190) 
        
        #=======================Data Frame Left=======================
        
        lblNameTablet = Label(DataframeLeft, text = "Names of Tablet", font = ("arial",12,"bold"),padx = 2, pady = 6)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        
        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets ,state="readonly",font = ("arial", 12,"bold"), width = 35)
        comNametablet["values"] = ("Amoxicillin", "Azithromycin", "Acetominophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0, column = 1)    
        
        lblref = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Reference No:", padx = 2)
        lblref.grid(row=1,column=0,sticky=W) 
        txtref = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable= self.ref, width = 35 )
        txtref.grid(row=1,column=1)   
        
        lblDost = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Dose:", padx = 2, pady = 4)
        lblDost.grid(row=2,column=0,sticky=W) 
        txtDost = Entry(DataframeLeft, font = ("arial", 12,"bold"), textvariable=self.Dose, width = 35 )
        txtDost.grid(row=2,column=1)   
        
        lblNoOftablets = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Number of Tablets:", padx = 2, pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W) 
        txtNoOftablets = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.NumberofTablets, width = 35 )
        txtNoOftablets.grid(row=3,column=1)   
        
        lblLot = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Lot:", padx = 2, pady=6)
        lblLot.grid(row=4,column=0,sticky=W) 
        txtLot = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.Lot, width = 35 )
        txtLot.grid(row=4,column=1)   
        
        lblissueDate = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Issue Date:", padx = 2, pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)  
        txtissueDate = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.Issuedate, width = 35 )
        txtissueDate.grid(row=5,column=1)  
        
        lblExpdate = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Exp Date:", padx = 2, pady=6)
        lblExpdate.grid(row=6,column=0,sticky=W) 
        txtExpdate = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.Expdate, width = 35 )
        txtExpdate.grid(row=6,column=1)   
        
        lblDailydose = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Daily Dose:", padx = 2, pady=6)
        lblDailydose.grid(row=7,column=0,sticky=W) 
        txtDailydose = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.Dailydose, width = 35 )
        txtDailydose.grid(row=7,column=1)   
        
        lblsideeffect = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Side Effect:", padx = 2, pady=6)
        lblsideeffect.grid(row=8,column=0,sticky=W) 
        txtsideeffect = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.Sideeffect, width = 35 )
        txtsideeffect.grid(row=8,column=1)   
        
        lblFurtherInfo = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Further Information:", padx = 2, pady=6)
        lblFurtherInfo.grid(row=0,column=2,sticky=W) 
        txtFurtherInfo = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.FurtherInfo, width = 35 )
        txtFurtherInfo.grid(row=0,column=3)   
        
        lblBloodPresuure = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Blood Pressure:", padx = 2, pady=6)
        lblBloodPresuure.grid(row=1,column=2,sticky=W) 
        txtBloodPressure = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.StorageAdvice, width = 35 )
        txtBloodPressure.grid(row=1,column=3)   
        
        lblStorage = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Storage Advice:", padx = 2, pady=6)
        lblStorage.grid(row=2,column=2,sticky=W) 
        txtStorage = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.DrivingUsingMachine, width = 35 )
        txtStorage.grid(row=2,column=3)   
                
        lblMedicine = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Medication:", padx = 2, pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W) 
        txtMedicine = Entry(DataframeLeft, font = ("arial", 12,"bold"), textvariable=self.HowToUseMedication, width = 35 )
        txtMedicine.grid(row=3,column=3)   
                
        lblPatientId = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Patient Id:", padx = 2, pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W) 
        txtPatientId = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.PatientId, width = 35 )
        txtPatientId.grid(row=4,column=3)   
                
        lblNHMnumber = Label(DataframeLeft, font = ("arial",12,"bold"), text = "NHS Number:", padx = 2, pady=6)
        lblNHMnumber.grid(row=5,column=2,sticky=W) 
        txtNHMnumber = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.nhsnumber, width = 35 )
        txtNHMnumber.grid(row=5,column=3)   
                
        lblPatientName = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Patient Name:", padx = 2, pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W) 
        txtPatientName = Entry(DataframeLeft, font = ("arial", 12,"bold"), textvariable=self.PatientName, width = 35 )
        txtPatientName.grid(row=6,column=3)   
        
        lblDOB = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Date Of Birth:", padx = 2, pady=6)
        lblDOB.grid(row=7,column=2,sticky=W) 
        txtDOB = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.DOB, width = 35 )
        txtDOB.grid(row=7,column=3) 
        
        lblPatientaddress = Label(DataframeLeft, font = ("arial",12,"bold"), text = "Patient Address:", padx = 2, pady=6)
        lblPatientaddress.grid(row=8,column=2,sticky=W) 
        txtPatientaddress = Entry(DataframeLeft, font = ("arial", 12,"bold"),textvariable=self.PatientAddress, width = 35 )
        txtPatientaddress.grid(row=8,column=3)  
        
        #========================Data Frame Right========================
        
        self.txtPrescription = Text(DataframeRight,font = ("arial",12,"bold"),width = 50,height = 16, padx = 2, pady = 6)
        self.txtPrescription.grid(row=0,column=0)
        
        #========================Buttons=============================
        
        btnPrescription = Button(Buttonframe,command=self.iPrescription, text = "Prescription", bg = "light blue", fg = "dark blue", font = ("arial",12,"bold"),width = 23, padx = 2, pady = 6)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData = Button(Buttonframe,command=self.iPrescriptionData, text = "Prescription Data", bg = "light blue", fg = "dark blue", font = ("arial",12,"bold"),width = 23, padx = 2, pady = 6)
        btnPrescriptionData.grid(row=0,column=1)
        
        btnupdate = Button(Buttonframe,command=self.update, text = "Update", bg = "light blue", fg = "dark blue", font = ("arial",12,"bold"),width = 23, padx = 2, pady = 6)
        btnupdate.grid(row=0,column=2)
        
        btndelete = Button(Buttonframe,command=self.idelete, text = "Delete", bg = "light blue", fg = "dark blue", font = ("arial",12,"bold"),width = 23, padx = 2, pady = 6)
        btndelete.grid(row=0,column=3)
        
        btnclear = Button(Buttonframe,command=self.clear, text = "Clear", bg = "light blue", fg = "dark blue", font = ("arial",12,"bold"),width = 23, padx = 2, pady = 6)
        btnclear.grid(row=0,column=4)
        
        btnExit = Button(Buttonframe,command=self.iExit, text = "Exit", bg = "light blue", fg = "dark blue", font = ("arial",12,"bold"),width = 23, padx = 2, pady = 6)
        btnExit.grid(row=0,column=5)
        
        #===================================Table==========================
        #==============================Scrollbar==========================
        
        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe,column=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack (side = BOTTOM, fill = X)
        scroll_y.pack (side = RIGHT, fill = Y)
        
        scroll_x = ttk.Scrollbar(command =self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command =self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftablets", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")
        
        self.hospital_table["show"] = "headings"
        
        self.hospital_table.column("nameoftablets",width = 100)
        self.hospital_table.column("ref",width = 100 )
        self.hospital_table.column("dose",width = 100 )
        self.hospital_table.column("nooftablets",width = 100 )
        self.hospital_table.column("lot",width = 100  )
        self.hospital_table.column("issuedate", width = 100 )
        self.hospital_table.column("expdate", width = 100 )
        self.hospital_table.column("dailydose", width = 100 )
        self.hospital_table.column("storage", width = 100 )
        self.hospital_table.column("nhsnumber", width = 100 )
        self.hospital_table.column("pname", width = 100 )
        self.hospital_table.column("dob",width = 100 )
        self.hospital_table.column("address", width = 100 )
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        #=========================Functionality Declaration======================
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error", "All blanks need to be filled")
        else:
            conn = mysql.connector.connect(host = "localhost", user = "root", password = "Dkp@1610", database = "mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftablets.get(),
                                                                                               self.ref.get(),
                                                                                               self.Dose.get(),
                                                                                               self.NumberofTablets.get(),
                                                                                               self.Lot.get(),
                                                                                               self.Issuedate.get(),
                                                                                               self.Expdate.get(),
                                                                                               self.Dailydose.get(),
                                                                                               self.StorageAdvice.get(),
                                                                                               self.nhsnumber.get(),
                                                                                               self.PatientName.get(),
                                                                                               self.DOB.get(),
                                                                                               self.PatientAddress.get()
                                                                                               
                                                                                               ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Successfully", "Record has been inserted")
            
    def update(self):
        conn = mysql.connector.connect(host = "localhost", user = "root", password = "Dkp@1610", database = "mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set Name_of_tablets=%s,Reference_No =%s,dose = %s,Numbersoftablets = %s,lot = %s, issuedate = %s,expdate = %s, dailydose = %s,storage = %s,nhsnumber = %s,patientname = %s,DOB = %s,patientaddress = %s",(self.Nameoftablets.get(),
                                                                                               self.ref.get(),
                                                                                               self.Dose.get(),
                                                                                               self.NumberofTablets.get(),
                                                                                               self.Lot.get(),
                                                                                               self.Issuedate.get(),
                                                                                               self.Expdate.get(),
                                                                                               self.Dailydose.get(),
                                                                                               self.StorageAdvice.get(),
                                                                                               self.nhsnumber.get(),
                                                                                               self.PatientName.get(),
                                                                                               self.DOB.get(),
                                                                                               self.PatientAddress.get()
                                                                                               ))
        
            
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", user = "root", password = "Dkp@1610", database = "mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.Expdate.set(row[6])
        self.Dailydose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsnumber.set(row[9])
        self.PatientName.set(row[10])
        self.DOB.set(row[11])
        self.PatientAddress.set(row[12])
        
    def iPrescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END,"No of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t" + self.Expdate.get() + "\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t" + self.Dailydose.get() + "\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t" + self.Sideeffect.get() + "\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t" + self.FurtherInfo.get() + "\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END,"Driving Using Machine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END,"Patient ID:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t" + self.nhsnumber.get() + "\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END,"Date Of Birth:\t\t\t" + self.DOB.get() + "\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")
        
        
    def idelete(self):
        conn = mysql.connector.connect(host = "localhost", user = "root", password = "Dkp@1610", database = "mydata")
        my_cursor = conn.cursor()
        query = "delete from hospital where Reference_No = %s"
        value = (self.ref.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","PatientInfo has been deleted successfully")
        
        
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.Dailydose.set("")
        self.Sideeffect.set("")
        self.FurtherInfo.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsnumber.set("")
        self.PatientName.set("")
        self.DOB.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)
        
        
    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System", "Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return
        
        
        
        
                
root = Tk()
object = Hospital(root)
root.mainloop()
