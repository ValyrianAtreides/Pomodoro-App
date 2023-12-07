from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas1.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps % 8==0:
        label.config(text="Break",fg=RED)
        count_down(long_break_sec)

    if reps % 2==0:
        winsound.Beep(1000, 500)
        label.config(text="Break", fg=PINK)
        count_down(break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min= math.floor(count/60)
    count_sec=count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas1.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)

    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)   #yani tekrar 2'deyse 1 tane tik ekleyecek
        for _ in range(work_sessions):
            mark +="✓"
        check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro App")
window.config(padx=100,pady=50,bg=YELLOW)

window.after(1000,)

back_ground = PhotoImage(file="tomato.png")
canvas1 = Canvas(width=200,
                 height=224,bg=YELLOW)

canvas1.create_image(103,112, image = back_ground)
timer_text=canvas1.create_text(103,130,text="00:00",fill="White",font=(FONT_NAME,35,"bold"))
canvas1.grid(column=1,row=1)

label=Label(text="TIMER",font=(FONT_NAME,25,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

start_button=Button(text="Start",font=(FONT_NAME,10,"bold"),command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",font=(FONT_NAME,10,"bold"),command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks=Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)


window.mainloop()