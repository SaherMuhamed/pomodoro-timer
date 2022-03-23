from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break :)", fg=RED, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break :)", fg=PINK, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="Work!", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > 0:
        global timer
        canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
            checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# TODO: Creating a window.

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=70, bg=YELLOW)

# TODO: Creating a canvas.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# TODO: Creating labels.
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
checkmark_label.grid(column=1, row=3)

# TODO: Creating buttons.
start_button = Button(text="Start", width=7, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=7, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
