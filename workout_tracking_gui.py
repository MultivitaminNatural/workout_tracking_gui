import csv,datetime,pprint,tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys

file="workout_gui_file.csv"
workout_csv_header = ['exercise', 'set', 'reps_1','reps_2','reps_3', 'date', "weight", "variation","rpe","rest time"]
def check_if_header_present():
    header_flag = 0
    try:
        with open(file, 'r+') as read_obj:
        # pass the file object to reader() to get the reader object
            csv_reader = csv.reader(read_obj)
        # Iterate over each row in the csv using reader object
            for row in csv_reader:
            # row variable is a list that represents a row in csv
                if row == workout_csv_header:
                    header_flag=header_flag+1
                    break

    except FileNotFoundError:
        open(file,"a")
        with open(file, 'r+') as read_obj:
        # pass the file object to reader() to get the reader object
            csv_reader = csv.reader(read_obj)
        # Iterate over each row in the csv using reader object
            for row in csv_reader:
            # row variable is a list that represents a row in csv
                if row == workout_csv_header:
                    header_flag = header_flag + 1
                    break
    if header_flag != 0:
        messagebox.showinfo("error!","header already present!")
    else:
        write_header()

def write_header():
    with open(file, 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(workout_csv_header)
        messagebox.showinfo('success!!', "you added the header! ")

exercise_dictionary = {1: "bench press",
                       2: "overhead press",
                       3: "barbell row",
                       4: "barbell squat",
                       5: "pistol squat",
                       6: "romanian deadlift",
                       7: "deadlift",
                       8: "pullup",
                       9: "weighted pullup",
                       10: "weighted dip",
                       11: "dip",
                       12: "bicep curl",
                       13: "triceps isolation work",
                       14: "planche pushup",
                       15: "front lever row",
                       16: "handstand pushup",
                       17: "dumbbell press",
                       18: "calf raises",
                       19: "nordic curl",
                       20: "hamstring curl",
                        21: "lat_pulldown",
                       22: "cable row",
                       23: "face pull"}
#a dictionary that contains all the exercises available
pretty_dictionary = pprint.pformat(exercise_dictionary)
#makes the dictionary look more presentable


#  designs the look of the gui
gui_window = tk.Tk()
gui_window.title('Workout tracking app 1.3')
gui_window.config(bg="#EE4540")#background colour
window_width = 600
window_height = 500 # get the screen dimension

screen_width = gui_window.winfo_screenwidth()
screen_height = gui_window.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2) # set the position of the window to the center of the screen
gui_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') #puts window in the centre of the screen
try:
    gui_window.iconbitmap('cat_2.ico')#changes the icon on the top left, only works if the picture is in the folder, otherwise uses the basic icon
except:
    pass

input_1 = tk.StringVar()
input_2 = tk.StringVar()
input_3 = tk.StringVar()
input_4 = tk.StringVar()
input_5 = tk.StringVar()
input_6 = tk.StringVar()
input_7 = tk.StringVar()
input_8 = tk.StringVar()
input_9 = tk.StringVar()
input_10 = tk.StringVar()
#declares all the variables for the input of th data

def submit():
    exercise = input_1.get()
    set = input_2.get()
    reps_1 = input_3.get()
    reps_2 = input_4.get()
    reps_3 = input_5.get()
    date = input_6.get()
    weight = input_7.get()
    variation = input_8.get()
    rpe = input_9.get()
    rest = input_10.get()
    error_counter = 0
    for input in [set,reps_1,reps_2,reps_3,weight,rpe,rest]:
        try:
            int(input)
        except ValueError as ep:
            messagebox.showinfo('error!', "input integer values!")
            error_counter = error_counter +1
    try:
        exercise_input = exercise_dictionary[exercise]
    except:
        error_counter = error_counter +1
        messagebox.showinfo('error!', "choose an exercise from the list and enter the assigned abbreviation")
    try:
        converted_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError as ep:
        error_counter = error_counter+1
        messagebox.showinfo('error!', "wrong date format, should be yyyy-mm-dd")
    if int(rpe) not in range(1,11):
        error_counter=error_counter+1
        messagebox.showinfo('error!', "rpe (rate of perceived exertion) must be in range 1-10")
    else:
        pass
    if error_counter==0:
        with open(file, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            input_into_csv = writer.writerow([exercise_dictionary[exercise], set, reps_1,reps_2,reps_3, date, weight, variation, rpe, rest])
            print("Adding")
            print(exercise_dictionary[exercise] + " with " + set + " sets," + reps_1 +" "+reps_2+" "+reps_3+" "+ " reps, done on " + date + " with " + weight + "kg, variation:" + variation + ", done at " + rpe + " rpe " + "with " + rest + "s rest time.")
            messagebox.showinfo('success!!', "you successfully entered the data")
        for entry_value in [exercise_entry,set_entry,reps_1_entry,reps_2_entry,reps_3_entry,date_entry,weight_entry,variation_entry,rpe_entry,rest_entry]:
            entry_value.delete(0, 'end')
    # used for input of the inputted workout data into the csv file.
    else:
        messagebox.showinfo('error!!', "general error message 101")

#creates label and entry for each variable necessary for writing into csv.
exercise_label = tk.Label(gui_window,width=8, fg="#FFFFFF",background="#801336", text='exercise', font=('times new roman', 15, 'bold'))
exercise_entry = tk.Entry(gui_window,fg="#FFFFFF", background="#801336",textvariable=input_1, font=('times new roman', 15, 'italic'))

set_label = tk.Label(gui_window,width=8,fg="#FFFFFF",background="#801336", text='sets', font=('times new roman', 15, 'bold'))
set_entry = tk.Entry(gui_window, fg="#FFFFFF",background="#801336",textvariable=input_2, font=('times new roman', 15, 'italic'))

reps_1_label = tk.Label(gui_window,width=8,fg="#FFFFFF",background="#801336", text='reps set 1', font=('times new roman', 15, 'bold'))
reps_1_entry = tk.Entry(gui_window,fg="#FFFFFF",background="#801336", textvariable=input_3, font=('times new roman', 15, 'italic'))

reps_2_label = tk.Label(gui_window,width=8,fg="#FFFFFF",background="#801336", text='reps set 2', font=('times new roman', 15, 'bold'))
reps_2_entry = tk.Entry(gui_window,fg="#FFFFFF",background="#801336", textvariable=input_4, font=('times new roman', 15, 'italic'))

reps_3_label = tk.Label(gui_window,width=8,fg="#FFFFFF",background="#801336", text='reps set 3', font=('times new roman', 15, 'bold'))
reps_3_entry = tk.Entry(gui_window,fg="#FFFFFF",background="#801336", textvariable=input_5, font=('times new roman', 15, 'italic'))

date_label = tk.Label(gui_window,width=8,fg="#FFFFFF",background="#801336", text='date', font=('times new roman', 15, 'bold'))
date_entry = tk.Entry(gui_window,fg="#FFFFFF",background="#801336",textvariable=input_6, font=('times new roman', 15, 'italic'))

weight_label = tk.Label(gui_window,width=8,fg="#FFFFFF",background="#801336", text='weight', font=('times new roman', 15, 'bold'))
weight_entry = tk.Entry(gui_window,fg="#FFFFFF",background="#801336", textvariable=input_7, font=('times new roman', 15, 'italic'))

variation_label = tk.Label(gui_window,width=8,fg="#FFFFFF",background="#801336", text='variation', font=('times new roman', 15, 'bold'))
variation_entry = tk.Entry(gui_window,fg="#FFFFFF",background="#801336", textvariable=input_8, font=('times new roman', 15, 'italic'))

rpe_label = tk.Label(gui_window,width=8,fg="#FFFFFF",background="#801336", text='rpe', font=('times new roman', 15, 'bold'))
rpe_entry = tk.Entry(gui_window, fg="#FFFFFF",background="#801336",textvariable=input_9, font=('times new roman', 15, 'italic'))

rest_label = tk.Label(gui_window,width=8,fg="#FFFFFF",background="#801336", text='rest', font=('times new roman', 15, 'bold'))
rest_entry = tk.Entry(gui_window,fg="#FFFFFF", background="#801336",textvariable=input_10, font=('times new roman', 15, 'italic'))




sub_btn = tk.Button(gui_window, text='Submit', command=submit,fg="#FFFFFF",background="#2D142C",font=('times new roman', 20, 'bold'))#submit button
header_btn = tk.Button(gui_window, text='Add header', command=check_if_header_present,fg="#FFFFFF",background="#2D142C",font=('times new roman', 12, 'bold'))#header button
exit_button = Button(gui_window, text="Exit", command=gui_window.destroy,fg="#FFFFFF",background="#2D142C",activebackground="red",activeforeground="black",font=('times new roman', 12, 'bold'))#exit button

def change_on_hovering_sub_button(event):
    global sub_btn
    sub_btn['bg'] = 'white'
    sub_btn["fg"] = "black"
def return_to_normal_state_sub_button(event):
   global sub_btn
   sub_btn['bg'] = "#2D142C"
   sub_btn["fg"] = "white"
sub_btn.bind('<Enter>', change_on_hovering_sub_button)
sub_btn.bind('<Leave>', return_to_normal_state_sub_button)

def change_on_hovering_header(event):
    global header_btn
    header_btn['bg'] = 'white'
    header_btn["fg"] = "black"
def return_to_normal_state_header(event):
   global header_btn
   header_btn['bg'] = "#2D142C"
   header_btn["fg"] = "white"
header_btn.bind('<Enter>', change_on_hovering_header)
header_btn.bind('<Leave>', return_to_normal_state_header)

def change_on_hovering_exit(event):
    global exit_button
    exit_button['bg'] = 'white'
    exit_button["fg"] = "black"
def return_to_normal_state_exit(event):
   global exit_button
   exit_button['bg'] = "#2D142C"
   exit_button["fg"] = "white"
exit_button.bind('<Enter>', change_on_hovering_exit)
exit_button.bind('<Leave>', return_to_normal_state_exit)
#makes the colours of the button change on hovering


# placing the label and entry in the required position using .place()
exercise_label.place(x = 0, y = 10)
exercise_entry.place(x = 110, y = 10)
set_label.place(x = 0, y = 45)
set_entry.place(x = 110, y = 45)
reps_1_label.place(x = 0, y = 90)
reps_1_entry.place(x = 110, y = 90)

reps_2_label.place(x = 0, y = 135)
reps_2_entry.place(x = 110, y = 135)

reps_3_label.place(x = 0, y = 180)
reps_3_entry.place(x = 110, y = 180)

date_label.place(x = 0, y = 225)
date_entry.place(x = 110, y = 225)
weight_label.place(x = 0, y = 270)
weight_entry.place(x = 110, y = 270)
variation_label.place(x = 0, y = 315)
variation_entry.place(x = 110, y = 315)
rpe_label.place(x = 0, y = 360)
rpe_entry.place(x = 110, y = 360)
rest_label.place(x = 0, y = 405)
rest_entry.place(x = 110, y = 405)
sub_btn.place(x = 110, y = 440)
exit_button.place(x = 265, y = 460)
header_btn.place(x=0,y=460)

#textbox with keys and values for exercises
text_box = Text(
    gui_window,
    height=27,
    width=31,
    font=('times new roman', 13, 'bold italic'),
background="#C72C41",fg="#FFFFFF")
text_box.place(relx=0.8
               , rely=0.54, anchor='center')
text_box.insert('end',pretty_dictionary)
text_box.config(state='disabled')#no readjusting the window for you!
gui_window.mainloop() #included every time to actually display the window