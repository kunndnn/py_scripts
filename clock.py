import tkinter as tk
from time import strftime


def update_time():
    current_time = strftime("%I:%M:%S %p")
    label.config(text=current_time)
    label.after(1000, update_time)


# create the main window
root = tk.Tk()
root.title("Digital Click")

label = tk.Label(
    root, font=("Calibri", 40, "bold"), background="blue", foreground="white"
)
label.pack(anchor="center")

# start the clock
update_time()
# run the application
root.mainloop()
