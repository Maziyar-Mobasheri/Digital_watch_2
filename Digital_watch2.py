from tkinter import *
import time

window = Tk()
window.title('Digital clock')
window.geometry('600x400')

# Default settings
font_family = 'Arial'
font_size = 72
text_color = 'white'
bg_color = 'gray'
time_format = 12  # Default to 12-hour format

def update_clock():
    hour = time.strftime('%I' if time_format == 12 else '%H')
    minute = time.strftime("%M")
    second = time.strftime('%S')
    am_pm = time.strftime('%p')
    day = time.strftime("%A")
    zone = time.strftime("%Z")

    myText = hour + ":" + minute + ":" + second + " " + am_pm
    myText2 = day + ", " + zone

    mylabel.config(text=myText)
    mylabel2.config(text=myText2)
    mylabel.after(1000, update_clock)

def change_font_size(size):
    global font_size
    font_size = size
    mylabel.config(font=(font_family, font_size))

def change_text_color(color):
    global text_color
    text_color = color
    mylabel.config(fg=text_color)

def change_bg_color(color):
    global bg_color
    bg_color = color
    mylabel.config(bg=bg_color)

def change_time_format(format):
    global time_format
    time_format = format

mylabel = Label(window, text="", font=(font_family, font_size), fg=text_color, bg=bg_color)
mylabel.pack()
mylabel2 = Label(window, text="", font=("Arial", 24))
mylabel2.pack()

update_clock()

# Settings panel
settings_frame = Frame(window)
settings_frame.pack()

font_size_label = Label(settings_frame, text="Font Size:")
font_size_label.grid(row=0, column=0)
font_size_scale = Scale(settings_frame, from_=12, to=100, orient=HORIZONTAL, command=change_font_size)
font_size_scale.set(font_size)
font_size_scale.grid(row=0, column=1)

text_color_label = Label(settings_frame, text="Text Color:")
text_color_label.grid(row=1, column=0)
text_color_entry = Entry(settings_frame, textvariable=StringVar(value=text_color), width=10)
text_color_entry.grid(row=1, column=1)

bg_color_label = Label(settings_frame, text="Background Color:")
bg_color_label.grid(row=2, column=0)
bg_color_entry = Entry(settings_frame, textvariable=StringVar(value=bg_color), width=10)
bg_color_entry.grid(row=2, column=1)

time_format_label = Label(settings_frame, text="Time Format:")
time_format_label.grid(row=3, column=0)
time_format_radio_12 = Radiobutton(settings_frame, text="12-Hour", variable=IntVar(value=time_format), value=12, command=lambda: change_time_format(12))
time_format_radio_24 = Radiobutton(settings_frame, text="24-Hour", variable=IntVar(value=time_format), value=24, command=lambda: change_time_format(24))
time_format_radio_12.grid(row=3, column=1)
time_format_radio_24.grid(row=3, column=2)

window.mainloop()