#!/usr/bin/env python3

import vtt
import sys
from tkinter import ttk
import tkinter as tk
from playsound import playsound

semester = None

if(len(sys.argv) < 3):
    print("usecase: class_track.py [semester] [year] [crn]")
    exit(0)

# input to command line (semester) (year) (crn)
# as an example:
# python3 class_track.py  spring 2024 13267

if(sys.argv[1] == "fall"):
  semester = vtt.Semester.FALL

if(sys.argv[1] == "summer"):
  semester = vtt.Semester.SUMMER

if(sys.argv[1] == "spring"):
  semester = vtt.Semester.SPRING
# print(sys.argv[1], sys.argv[2], sys.argv[3])

course = vtt.get_crn(sys.argv[2], semester, sys.argv[3])

while(course.has_open_spots() == False):
    continue



root = tk.Tk()
root.title('Ding!')

window_width = 300
window_height = 200
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

message = tk.Label(root, 
               text="Ding! {crn} is open!".format(crn=sys.argv[3]),
               font=("Helvetica", 20))

message.pack(side=tk.TOP, expand=True)

photo = tk.PhotoImage(file='./image.png')
image_label = ttk.Label(
root,
image=photo,
padding=1
)
image_label.pack()

def ding():
    playsound("./sound-6.mp3")
    root.after(500,ding)

root.after(100, ding)

root.mainloop()
