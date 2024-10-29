"""
EXERCISE 3 Student Manager by Val Kyrvey Latoja
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image
import pygame

#  initialize pygame mixer
pygame.mixer.init()

# function to play music 
def playmusic():
    pygame.mixer.music.load("20190826.mp3")
    pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()
    
# showing grade
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

# showing all students
def viewstudentrecord():
    studentlist = "studentMarks.txt"
    studentcount = 0
    totalpercentage = 0
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
            studentcount += 1
            totalpercentage += percentage

        textbox.insert(tk.END, f"Total number of students: {studentcount}\n")

        if studentcount > 0:
            avgpercentage = totalpercentage / studentcount
            textbox.insert(tk.END, f"Average Percentage: {avgpercentage:.2f}%")

        return content

# showing highest student
def highestresult():
    studentlist = "studentMarks.txt"
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
                percentageresult = calculatepercentage(percentage)
                top_student = f"Name: {values[1].strip()}\nStudent No.: {values[0].strip()}\nCoursework Total: {total}\nExam Mark: {values[5].strip()}\nOverall Percentage: {percentage:.2f}%\nGrade: {percentageresult}"
    
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, f"{top_student}")

# showing lowest student
def lowestresult():
    studentlist = "studentMarks.txt"
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
                percentageresult = calculatepercentage(percentage)
                bottom_student = f"Name: {values[1].strip()}\nStudent No.: {values[0].strip()}\nCoursework Total: {total}\nExam Mark: {values[5].strip()}\nOverall Percentage: {percentage:.2f}%\nGrade: {percentageresult}"
    
    textbox.delete("1.0", tk.END)
    textbox.insert(tk.END, f"{bottom_student}")

# showing each individual student in the option menu
def load_students():
    studentlist = "studentMarks.txt"
    student_names = []
    with open(studentlist, 'r') as file:
        content = file.readlines()
        for line in content:
            values = line.strip().split(',')
            if values[0].lower() != "name":
                student_names.append(values[1].strip())
    return student_names

# showing the selected student's results from the option menu
def view_student_record():
    selected_student = selected_option.get()
    studentlist = "studentMarks.txt"
    textbox.delete("1.0", tk.END)
    with open(studentlist, 'r') as file:
        content = file.readlines()
        for line in content:
            values = line.strip().split(',')
            if values[1].strip() == selected_student:
                total = int(values[2].strip()) + int(values[3].strip()) + int(values[4].strip())
                percentage = ((total + int(values[5].strip())) / 160) * 100
                percentageresult = calculatepercentage(percentage)
                textbox.insert(tk.END, f"Name: {values[1].strip()}\nStudent No.: {values[0].strip()}\nCoursework Total: {total}\nExam Mark: {values[5].strip()}\nOverall Percentage: {percentage:.2f}%\nGrade: {percentageresult}\n\n")

def on_closing():
    stop_music()
    root.destroy()
    
root = tk.Tk()
root.title("Student Manager")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#ff5c92")

# PLays background music
playmusic()

img = Image.open("C:\\Users\\Val Kyrvey Latoja\\Documents\\Coding shit\\Python\\ASSESSMENT 1\\heart.png")
resized_image = img.resize((100, 100))  # resize to 100x100 pixels
new_image = ImageTk.PhotoImage(resized_image) # setting a new variable for the resized new image
root.iconphoto(False, new_image) # setting the window icon

# Define font settings
font_settings1 = ("Helvetica", 24, "bold")
font_settings2 = ("Helvetica", 11)
font_settings3 = ("Helvetica", 13, "bold")

# Create header
header = tk.Label(root, text="Student Manager", font=font_settings1, bg="#ff5c92")
header.grid(row=0, column=0, columnspan=3, pady=20, sticky="ew")

# Create buttons
button1 = tk.Button(root, text="View All Student Records", font=font_settings2, width=20, height=3, relief="flat", bg="#ffa6d2", activebackground="#ff2b75", command=viewstudentrecord)
button2 = tk.Button(root, text="Show Highest Score", font=font_settings2, width=20, height=3, relief="flat", bg="#ffa6d2", activebackground="#ff2b75", command=highestresult)
button3 = tk.Button(root, text="Show Lowest Score", font=font_settings2, width=20, height=3, relief="flat", bg="#ffa6d2", activebackground="#ff2b75", command=lowestresult)

button1.grid(row=1, column=0, padx=10, pady=10)
button2.grid(row=1, column=1, padx=10, pady=10)
button3.grid(row=1, column=2, padx=10, pady=10)

# Configure column weights for even spacing
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# Ensure the first row remains fixed
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)

# Subtext and OptionMenu in the second row
subtext = tk.Label(root, text="View Individual Student Record: ", font=font_settings3, bg="#ff5c92", anchor="w")
subtext.grid(row=2, column=0, columnspan=2, padx=(2,1), pady=0, sticky="w")

studentnames=load_students()
selected_option = tk.StringVar()
selected_option.set(studentnames[0])
option = ttk.Combobox(root, textvariable=selected_option, values=studentnames, font=("Helvetica",10))
option.config(width=15)
option.grid(row=2, column=1, padx=(1, 2), pady=0, sticky="e")

button4 = tk.Button(root, text="View Record", font=font_settings2, width=10, height=2, relief="flat", bg="#ffa6d2", activebackground="#ff2b75", command=view_student_record)
button4.grid(row=2, column=2, padx=0, pady=0)

# Make the second row flexible
root.rowconfigure(2, weight=0)

# Text box with fixed size and padding
textbox = tk.Text(root, width=70, height=15)
textbox.grid(row=3, column=0, columnspan=3, padx=30, pady=20, sticky="nsew")

# Configure the row with the text box to be flexible as well
root.rowconfigure(3, weight=1)

# Bind the close event to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()