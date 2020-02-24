import tkinter as tk
import random

HEIGHT = 500
WIDTH = 600

random_number = random.randint(1, 100)


def restart():
    global random_number
    random_number = random.randint(1, 100)
    label["text"] = "Good Luck!!"
    clear_text()
    entry.focus()


def clear_text():
    entry.delete(0, 'end')


def guess_function(entry):
    try:
        entry_int = int(entry)
        if(entry_int < random_number):
            label["text"] = "Too Low"
            clear_text()
        elif(entry_int > random_number):
            label["text"] = "Too High"
            clear_text()
        elif(entry_int == random_number):
            label["text"] = "You Win!!"
            clear_text()
        else:
            label["text"] = "Please enter a number 1-100"
            clear_text()
    except ValueError:
        label["text"] = "Please enter a number 1-100"
        clear_text()


root = tk.Tk()
root.title("Guessing Game")
root.bind('<Return>', lambda event: guess_function(entry.get()))

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg='#80c1ff', bd=5)
upper_frame.place(relx=0.5, rely=0.05, relwidth=0.75,
                  relheight=0.1, anchor='n')

upper_label = tk.Label(upper_frame, bg='#80c1ff',
                       text='Guess a number between 1 and 100', font=(None, 25), height=50, width=50)
upper_label.config(width=500)
upper_label.place(relx=0.5, relheight=1, anchor='n')

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=(None, 35))
entry.place(relwidth=.65, relheight=1)

button = tk.Button(frame, text="Guess", font=40,
                   command=lambda: guess_function(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75,
                  relheight=0.4, anchor='n')

label = tk.Label(lower_frame, text="Good Luck!!", font=(None, 30))
label.place(relwidth=1, relheight=1)

restart_button = tk.Button(root, text="Restart", font=40, command=restart)
restart_button.place(relx=0.45, rely=0.85, height=40,
                     width=60, anchor='n')

quit_button = tk.Button(root, text="Quit", font=40, command=quit)
quit_button.place(relx=0.55, rely=0.85, height=40, width=60, anchor='n')

entry.focus()
root.mainloop()
