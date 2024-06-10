from tkinter import *
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

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    countdown(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    # format timer
    minute = int(count / 60)
    print(minute)
    seconds = count % 60
    print(seconds)
    canvas.itemconfig(timer_text, text=f"{minute:=02}:{seconds:=02}")
    if count > 0:
        window.after(1000, countdown, count - 1)



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
checkmarks = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"))
checkmarks.grid(column=1, row=3)

# create start button
start_button = Button(text="Start", command=start, font=BUTTON_FONT)
start_button.grid(column=0, row=2)

# create reset button
reset_button = Button(text="Reset", command=reset, font=BUTTON_FONT)
reset_button.grid(column=2, row=2)



window.mainloop()