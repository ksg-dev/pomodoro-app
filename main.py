from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BUTTON_FONT = ("Calibri", 12, "normal")
reps = 0
checks = ""

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    print(reps)

    if reps == 8:
        countdown(LONG_BREAK_MIN)
        # countdown(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN)
        # countdown(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        countdown(WORK_MIN)
        # countdown(work_sec)
        timer_label.config(text="Work!")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    # format timer
    minute = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minute:=02}:{seconds:=02}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start()
        global checks
        if reps % 2 == 0:
            checks += "✔"
            checkmarks.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
# Window set up
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas set up
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# x, y required, to center image half canvas size - adjusted x to center

# Use PhotoImage to read image from file location
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)

# Add timer and set to grid
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24, "bold"))
timer_label.grid(column=1, row=0)

# Create checkmarks
checkmarks = Label(text=checks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"))
checkmarks.grid(column=1, row=3)

# create start button
start_button = Button(text="Start", command=start, font=BUTTON_FONT)
start_button.grid(column=0, row=2)

# create reset button
reset_button = Button(text="Reset", command=reset, font=BUTTON_FONT)
reset_button.grid(column=2, row=2)



window.mainloop()
