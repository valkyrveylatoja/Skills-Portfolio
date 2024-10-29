import tkinter as tk
from tkinter import ttk
import pygame

pygame.mixer.init()

def playmusic():
    pygame.mixer.music.load("C:\\Users\Val Kyrvey Latoja\\Documents\\Coding shit\\Python\\ASSESSMENT 1\\20190826.mp3")
    pygame.mixer.music.play(-1)
    
def calculatepercentage(percentage):
    if percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

def openstudentfile():
    studentlist = "C:\\Users\\Val Kyrvey Latoja\\Documents\\Coding shit\\Python\\ASSESSMENT 1\\studentMarks.txt"
    student_names = []
    with open(studentlist, 'r') as file:
        content = file.readlines()
        for line in content:
            values = line.strip().split(',')
            if values[0].lower() == "name":
                continue
            student_names.append(values[1].strip())
    return student_names

def viewallstudents():
    studentlist = "C:\\Users\\Val Kyrvey Latoja\\Documents\\Coding shit\\Python\\ASSESSMENT 1\\studentMarks.txt"
    student_count = 0
    total_percentage = 0
    with open(studentlist, 'r') as file:
        content = file.readlines()
        textbox.delete("1.0", tk.END)
        for line in content:
            values = line.strip().split(',')
            if values[0].lower() == "name":
                textbox.insert(tk.END, f"{values[0].strip()} - {values[1].strip()}\n")
                continue
            total = int(values[2].strip()) + int(values[3].strip()) + int(values[4].strip())
            percentage = ((total + int(values[5].strip())) / 160) * 100
            percentageresult = calculatepercentage(percentage)
            textbox.insert(tk.END, f"Name: {values[1].strip()}\nStudent No.: {values[0].strip()}\nCoursework Total: {total}\nExam Mark: {values[5].strip()}\nOverall Percentage: {percentage:.2f}%\nGrade: {percentageresult}\n\n")
            student_count += 1
            total_percentage += percentage
        
        if student_count > 0:
            avg_percentage = total_percentage / student_count
            textbox.insert(tk.END, f"\nAverage Percentage: {avg_percentage:.2f}%\n")
        
        textbox.insert(tk.END, f"Total number of students: {student_count}\n")

def viewstudentrecord():
    selected_student = selected_option.get()
    textbox.delete("1.0", tk.END)
    with open("C:\\Users\\Val Kyrvey Latoja\\Documents\\Coding shit\\Python\\ASSESSMENT 1\\studentMarks.txt", 'r') as file:
        content = file.readlines()
        for line in content:
            values = line.strip().split(',')
            if values[1].strip() == selected_student:
                total = int(values[2].strip()) + int(values[3].strip()) + int(values[4].strip())
                percentage = ((total + int(values[5].strip())) / 160) * 100
                percentageresult = calculatepercentage(percentage)
                textbox.insert(tk.END, f"Name: {values[1].strip()}\nStudent No.: {values[0].strip()}\nCoursework Total: {total}\nExam Mark: {values[5].strip()}\nOverall Percentage: {percentage:.2f}%\nGrade: {percentageresult}\n")

def highestresult():
    studentlist = "C:\\Users\\Val Kyrvey Latoja\\Documents\\Coding shit\\Python\\ASSESSMENT 1\\studentMarks.txt"
    highest_percentage = -1
    top_student = ""
    with open(studentlist, 'r') as file:
        content = file.readlines()
        for line in content:
            values = line.strip().split(',')
            if values[0].lower() == "name":
                continue
            total = int(values[2].strip()) + int(values[3].strip()) + int(values[4].strip())
            percentage = ((total + int(values[5].strip())) / 160) * 100
            if percentage > highest_percentage:
                highest_percentage = percentage
                top_student = f"Name: {values[1].strip()}\nStudent No.: {values[0].strip()}\nCoursework Total: {total}\nExam Mark: {values[5].strip()}\nOverall Percentage: {percentage:.2f}%\n"
    
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, f"Top Student:\n{top_student}")

def lowestresult():
    studentlist = "C:\\Users\\Val Kyrvey Latoja\\Documents\\Coding shit\\Python\\ASSESSMENT 1\\studentMarks.txt"
    lowest_percentage = 101
    bottom_student = ""
    with open(studentlist, 'r') as file:
        content = file.readlines()
        for line in content:
            values = line.strip().split(',')
            if values[0].lower() == "name":
                continue
            total = int(values[2].strip()) + int(values[3].strip()) + int(values[4].strip())
            percentage = ((total + int(values[5].strip())) / 160) * 100
            if percentage < lowest_percentage:
                lowest_percentage = percentage
                bottom_student = f"Name: {values[1].strip()}\nStudent No.: {values[0].strip()}\nCoursework Total: {total}\nExam Mark: {values[5].strip()}\nOverall Percentage: {percentage:.2f}%\n"
    
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, f"Lowest Student:\n{bottom_student}")

# Example Tkinter setup
root = tk.Tk()
root.title("Student Manager")
root.geometry("600x500")

# Start playing music in the background
playmusic()

textbox = tk.Text(root, wrap='word', width=70, height=20)
textbox.pack(pady=20)

# Load student names into OptionMenu
student_names = openstudentfile()
selected_option = tk.StringVar()
selected_option.set(student_names[0])
option_menu = ttk.Combobox(root, textvariable=selected_option, values=student_names, font=("Helvetica", 12))
option_menu.pack()

# Button to view all student records
button_all = tk.Button(root, text="View All Students", command=viewallstudents)
button_all.pack()

# Button to view selected student record
button_view = tk.Button(root, text="View Student Record", command=viewstudentrecord)
button_view.pack()

# Button to view highest result
button_highest = tk.Button(root, text="View Highest Result", command=highestresult)
button_highest.pack()

# Button to view lowest result
button_lowest = tk.Button(root, text="View Lowest Result", command=lowestresult)
button_lowest.pack()

root.mainloop()

