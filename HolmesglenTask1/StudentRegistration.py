import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog


def printHeadings():

    print("-- HOLMESGLEN INSTITUTE --\n")
    print("ID    NAME    COURSE    FEE \n")
printHeadings()

student_dict = {'ID', 'NAME', 'COURSE', 'FEE'}
def inputStudentDetails():

    application_window = tk.Tk()
    application_window.geometry("30x20")
    application_window.title("Student Details")
    student_ID = simpledialog.askstring("Student Details","Input student ID", parent=application_window)
    student_NAME = simpledialog.askstring("Student Details", "Input student name",parent=application_window)
    student_COURSE = simpledialog.askstring("Student Details", "Input the enrolled course", parent=application_window)
    student_FEE = simpledialog.askstring("Student Details", "Input the course fees", parent=application_window)

    student_dict['ID'] = student_ID
    student_dict['NAME'] = student_NAME
    student_dict['COURSE'] = student_COURSE
    student_dict['FEE'] = student_FEE
    print(student_dict)

    student_detail = []
    for i in range(1,4):
        student_detail.append()
    print(student_detail)



'''


def outputTotalFee()
'''


