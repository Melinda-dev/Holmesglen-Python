import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog


def printHeadings():

    print("-- HOLMESGLEN INSTITUTE --")
    print("ID    NAME    COURSE    FEE \n")


def inputStudentDetails():
    application_window = tk.Tk()
    application_window.geometry("60x40")
    application_window.title("Student Details")
    student_ID = simpledialog.askstring("Student Details","Input student ID", parent=application_window)
    student_NAME = simpledialog.askstring("Student Details", "Input student name",parent=application_window)
    student_COURSE = simpledialog.askstring("Student Details", "Input the enrolled course", parent=application_window)
    student_FEE = simpledialog.askstring("Student Details", "Input the course fees", parent=application_window)

    student_dict['ID'] = student_ID
    student_dict['NAME'] = student_NAME
    student_dict['COURSE'] = student_COURSE
    student_dict['FEE'] = float(student_FEE)
    return student_dict, student_FEE

def outputTotalFee(total_fees):

    print("\n Total Fee: ${}".format(total_fees))



printHeadings() # for testing
student_dict = {}
totalFees = 0.0

for i in range(1, 4):
    student, student_FEE = inputStudentDetails()
    #print(student_FEE)
    totalFees += float(student_FEE)
    print("{}    {}    {}    {}".format(student['ID'],student['NAME'], student['COURSE'], student['FEE']))
    #student_detail.append()
#print(student_detail)

outputTotalFee(totalFees)



