from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#a10f18"
RED = "#e7305b"
GREEN = "#69942e"
YELLOW = "#ffde59"
FONT_NAME = "Montserrat"
ICON = ""
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER")
    checks_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break...", fg=PINK)
        countdown(short_break_sec)
    else:
        countdown(work_sec)
        title_label.config(text="WORKING", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_mins = count // 60
    count_secs = count % 60
    canvas.itemconfig(timer_text, text=f"{count_mins:02d}:{count_secs:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        checks_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.grid(column=1, row=0)

checks_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checks_label.grid(column=1, row=3)

start_button = Button(text="Start", font=("Montserrat", 10, "bold"),
                activebackground="black",
                activeforeground="white",
                command=start_timer)
start_button.grid(column=0, row=2)
start_button.config(padx=10, pady=2)
reset_button = Button(text="Reset", font=("Montserrat", 10, "bold"),
                      activebackground="black",
                      activeforeground="white",
                      command=reset)
reset_button.grid(column=2, row=2)
reset_button.config(padx=10, pady=2)

canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125,125, image=tomato_img)
timer_text = canvas.create_text(120, 180, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
check_img = PhotoImage(file="checkmark.png")



window.mainloop()