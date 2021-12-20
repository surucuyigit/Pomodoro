import os
from tkinter import *
import math
#-------------------------------------#
# Used this block of code for pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#---------------------------------------#

# CONSTANTS  #
YELLOW = "#F7F5DD"
GREEN = "#519259"
PEACH = "#FF9292"
PINK = "#FFCCD2"
MAROON = "#DD4A48"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
screen_timer = None

# RESET #

def reset_timer():
    global reps
    window.after_cancel(screen_timer)
    tick.config(text='')
    timer_label.config(text='Timer', fg=PEACH)
    canvas.itemconfig(pomodoro_timer, text='00:00')
    reps = 0


# TIMER #

def start_timer():
    global reps
    reps += 1

    working_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        window.deiconify()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        timer_label.config(text='Long Break')
        count = long_break_sec
    elif reps % 2 == 0 and reps != 0:
        window.deiconify()  # If window minimized, it forces program to bring on screen
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        timer_label.config(text='Short Break', fg=MAROON)
        count = short_break_sec
    else:
        window.deiconify()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        timer_label.config(text='Work Time', fg=GREEN)
        count = working_sec

    timer(count)

# COUNTDOWN #
def timer(count):
    global screen_timer
    minutes = math.floor(count / 60)
    seconds = count % 60  # We can get the remaining seconds with modulo
    if seconds <= 9:
        seconds = f'0{seconds}'

    canvas.itemconfig(pomodoro_timer, text=f'{minutes}:{seconds}')
    if count > 0:
        screen_timer = window.after(1000, timer, count - 1)
    else:
        start_timer()
        empty_string = ''
        number_of_ticks = math.floor(reps/2)
        for _ in range(number_of_ticks):
            empty_string += '✓'
        tick.config(text=empty_string)

# UI #

# Window & Canvas
window = Tk()
window.title('Pomodoro')
window.config(padx=50, pady=30, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file=resource_path('tomato.png'))
canvas.create_image(100, 112, image=tomato) # x ve y vermek zorundayiz
pomodoro_timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 28, 'bold'))
canvas.grid(column=1, row=1)

#Label
timer_label = Label(text='Timer', font=(FONT_NAME, 36, 'bold'))
timer_label.config(bg=YELLOW, fg=PEACH)
timer_label.grid(column=1, row=0)

tick = Label(bg=YELLOW, fg=PINK)
tick.config(font=(FONT_NAME, 8, 'bold'), pady=20)
# tick.place(x=170, y=295)
tick.grid(column=1, row=2)

#Button
start_button = Button(text='Start', command=start_timer)
start_button.config(width=10, fg=YELLOW, bg=PEACH)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.config(width=10, fg=YELLOW, bg=PEACH)
reset_button.grid(column=2, row=2)


window.mainloop()
