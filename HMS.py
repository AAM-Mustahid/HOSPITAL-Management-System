# hospital management system with Tkinter GUI and MySQL database
from tkinter import*
from tkinter import ttk
import random
import time
import datetime 
from tkinter import messagebox



class Hospital():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background="gainsboro")
# ========================Main Frame===============================================================================
        MainFrame = Frame(self.root, bd=10, width = 1350, height = 700, relief=RIDGE)
        MainFrame.grid()
        UFrame = Frame(MainFrame, bd=10, width = 1340, height = 600, relief=RIDGE)
        UFrame.grid(row = 0, column = 0) 
        ULFrame = Frame(UFrame, bd=5, width = 600, height = 500, bg = 'cadet blue', relief=RIDGE)
        ULFrame.grid(row = 0, column = 0)       
        URFrame = Frame(UFrame, bd=5, width = 800, height = 500, bg = 'cadet blue', relief=RIDGE)
        URFrame.grid(row = 0, column = 1, sticky = N)
        LowerFrame = Frame(MainFrame, bd=7, width = 1340, height = 300, bg = 'cadet blue', relief=RIDGE)
        LowerFrame.grid(row = 2, column = 0, sticky=W, padx =5)        
# ========================Upper Right Frame===============================================================================
        PatientListFrame = Frame(URFrame, bd=5, width = 800, height =300, relief = RIDGE)
        PatientListFrame.grid()  
        PatientInfoFrame = Frame(ULFrame, bd=4, width = 600, height=300, relief=RIDGE)
        PatientInfoFrame.grid()

        Subject_Frame_Left = Frame(LowerFrame, bd=5, width = 600, height=300, relief=RIDGE)
        Subject_Frame_Left.grid(row=0, column=0, sticky = NW)
        Subject_Frame_Right = Frame(LowerFrame, bd=5, width = 700, height=300, bg='cadet blue', relief=RIDGE)
        Subject_Frame_Right.grid(row=0, column=1)
        SubjectFrame1 = Frame(Subject_Frame_Left, bd=5, width = 300, height = 250, padx=2, relief=RIDGE)
        SubjectFrame1.grid(row=0, column=0, sticky=W)
        SubjectFrame2 = Frame(Subject_Frame_Left, bd=5, width = 400, height = 250, padx=2, relief=RIDGE)
        SubjectFrame2.grid(row=0, column=1, sticky = NW)
        DoctorFrame = Frame(Subject_Frame_Right, bd=5, width = 400, height=250, padx=4, pady=4, relief=RIDGE)
        DoctorFrame.grid(row=0, column=0, sticky = N)
        ButtonsFrame = Frame(Subject_Frame_Right, bd=5, width = 200, height=250, padx=4, pady=4, relief=RIDGE)
        ButtonsFrame.grid(row=0, column=1)

# --------------------------Variables--------------------------------------------------------------------------------

        self.PatientID = StringVar()
        self.FirstName = StringVar()
        self.LastName = StringVar()
        self.Age = StringVar()
        self.Gender = StringVar()
        self.BloodGroup = StringVar()
        self.Address = StringVar()
        self.Mobile = StringVar()
        self.Email = StringVar()
        self.RoomNumber = StringVar()
        self.DoctorID = StringVar()
        self.ApptID = StringVar()
        self.Diagnosis = StringVar()
        self.Date = StringVar()
        self.DoctorAge = StringVar()
        self.DoctorName = StringVar()


        #--------------------------Patient Details--------------------------------------------------------------------------------
        self.lblPatientInfo = Label(PatientInfoFrame, font=('arial', 12, 'bold'), text="Patient Information", bd=7)
        self.lblPatientInfo.grid(row=0, column=0, padx=5, pady=5,sticky='w')

        self.lblPatientID = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Patient ID", bd=7)
        self.lblPatientID.grid(row=1, column=0, sticky = W, padx=5, pady= 5)

        self.txtPatientID = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19, textvariable=self.PatientID)
        self.txtPatientID.grid(row=1, column=1, padx=5, pady= 5)

        self.lblFirstName = Label(PatientInfoFrame, font=('arial',12,'bold'), text="First Name", bd=7)
        self.lblFirstName.grid(row=2, column=0, sticky = W, padx=5, pady= 5)

        self.txtFirstName = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19,textvariable=self.FirstName)
        self.txtFirstName.grid(row=2, column=1, padx=5, pady= 5)

        self.lblLastName = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Last Name", bd=7)
        self.lblLastName.grid(row=3, column=0, sticky = W, padx=5, pady= 5)

        self.txtLastName = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19,textvariable=self.LastName)
        self.txtLastName.grid(row=3, column=1, padx=5, pady= 5)

        self.lblAge = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Age", bd=7)
        self.lblAge.grid(row=4, column=0, sticky = W, padx=5, pady= 5)

        self.txtAge = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19,textvariable=self.Age)
        self.txtAge.grid(row=4, column=1, padx=5, pady= 5)
        
        self.lblGender= Label(PatientInfoFrame, font=('arial',12,'bold'), text="Gender", bd=7)
        self.lblGender.grid(row=5, column=0, sticky = W, padx=5, pady= 5)
        self.cboGender = ttk.Combobox(PatientInfoFrame, width=19, font=('arial', 12,'bold'), state='readonly',textvariable=self.Gender)
        self.cboGender['values'] = ('Select','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5,column=1)

# Create a label for blood group
        self.lblBloodGroup = Label(PatientInfoFrame, font=('arial', 12, 'bold'), text="Blood Group", bd=7)
        self.lblBloodGroup.grid(row=6, column=0, sticky=W, padx=5, pady=5)
 


# Create a ComboBox for blood groups
        self.cboBloodGroup = ttk.Combobox(PatientInfoFrame, width=19, font=('arial', 12, 'bold'), state='readonly', textvariable=self.BloodGroup)
        self.cboBloodGroup['values'] = ['Select', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']  # Set the values for the ComboBox
        self.cboBloodGroup.current(0)
        self.cboBloodGroup.grid(row=6, column=1, padx=5, pady=5)  # Grid placement for the ComboBox

       
        self.lblAddress = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=7, column=0, sticky = W, padx=5, pady= 5)
        self.txtAddress = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19,textvariable=self.Address)
        self.txtAddress.grid(row=7, column=1, padx=5, pady= 5)
        
        self.lblMobile = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=8, column=0, sticky = W, padx=5, pady= 5)
        self.txtMobile = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19, textvariable=self.Mobile)
        self.txtMobile.grid(row=8, column=1, padx=5, pady= 5)
        self.lblEmail = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=9, column=0, sticky = W, padx=5, pady= 5)
        self.txtEmail = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19, textvariable= self.Email)
        self.txtEmail.grid(row=9, column=1, padx=5, pady= 5)

        self.lblRoomNumber = Label(PatientInfoFrame, font=('arial',12,'bold'), text="Room Number", bd=7)
        self.lblRoomNumber.grid(row=10, column=0, sticky = W, padx=5, pady= 5)
        self.txtRoomNumber = Entry(PatientInfoFrame, font=('arial',12,'bold'), bd=5,width=19, textvariable= self.RoomNumber)
        self.txtRoomNumber.grid(row=10, column=1, padx=5, pady= 5)
       
#Patient Records
        scroll_x = Scrollbar(PatientListFrame, orient = HORIZONTAL)
        scroll_y = Scrollbar(PatientListFrame, orient = VERTICAL)
        columns = ("PatientID","First Name","Last Name","Age","Gender","Blood Group","Address","Mobile","Email","Room Number")
        self.student_records = ttk.Treeview(PatientListFrame, height = 13, columns=columns, xscrollcommand=scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side= BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT, fill=Y) 
                




if __name__ == '__main__':
    root = Tk()
    application = Hospital(root)
    root.mainloop()