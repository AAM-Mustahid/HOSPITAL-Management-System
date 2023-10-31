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
        PatientInfoFrame = Frame(ULFrame, bd=4, width = 600, height=400, relief=RIDGE)
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




if __name__ == '__main__':
    root = Tk()
    application = Hospital(root)
    root.mainloop()