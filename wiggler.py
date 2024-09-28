import pyautogui
import random
import time
import threading
import tkinter as tk

# Global flag to control when to exit the script
running = False
start_time = 0

# Define time delay between switching apps and scrolling
switch_delay = 4  # Increased delay between app switches to make it more noticeable
scroll_delay = 2  # Adjust the delay time between scroll actions

# Screen dimensions (pyautogui.size() will give you the screen width and height)
screen_width, screen_height = pyautogui.size()


def random_app_switch():
    app_jumps = random.randint(1, 7)
    pyautogui.keyDown('alt')  # Use 'command' for macOS
    for _ in range(app_jumps):
        pyautogui.press('tab')
        time.sleep(0.3)  # Small delay between each tab press to make it noticeable
    pyautogui.keyUp('alt')


def random_scroll():
    scroll_direction = random.choice(['up', 'down'])
    scroll_amount = random.randint(50, 200)  # Increase the scroll amount for more noticeable movement

    if scroll_direction == 'down':
        pyautogui.scroll(-scroll_amount)  # Scroll down
    else:
        pyautogui.scroll(scroll_amount)  # Scroll up


def random_mouse_move():
    move_x = random.randint(-50, 50)  # Random x-axis movement
    move_y = random.randint(-50, 50)  # Random y-axis movement

    current_x, current_y = pyautogui.position()

    new_x = max(0, min(screen_width, current_x + move_x))
    new_y = max(0, min(screen_height, current_y + move_y))

    pyautogui.moveTo(new_x, new_y, duration=0.5)  # Smooth movement over 0.5 seconds


def run_script():
    global running, start_time
    start_time = time.time()
    running = True
    while running:
        random_app_switch()
        time.sleep(switch_delay)
        random_scroll()
        time.sleep(scroll_delay)
        random_mouse_move()
        time.sleep(1)


def start_script():
    threading.Thread(target=run_script, daemon=True).start()
    update_timer()  # Start updating the timer display


def stop_script():
    global running
    running = False
    timer_label.config(text="Timer: 00:00:00")  # Reset timer display


def update_timer():
    if running:
        elapsed_time = int(time.time() - start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        timer_label.config(text=f"Timer: {hours:02}:{minutes:02}:{seconds:02}")
        timer_label.after(1000, update_timer)  # Update timer every second


# GUI setup
root = tk.Tk()
root.title("Random App Switcher")
root.configure(bg="#282c34")  # Background color

# Timer label
timer_label = tk.Label(
    root, text="Timer: 00:00:00", font=("Helvetica", 14), bg="#282c34", fg="#61dafb"
)
timer_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

# Start button
start_button = tk.Button(
    root,
    text="Start",
    command=start_script,
    width=10,
    bg="#61dafb",
    fg="white",
    font=("Helvetica", 12),
)
start_button.grid(row=1, column=0, padx=10, pady=10)

# Stop button
stop_button = tk.Button(
    root,
    text="Stop",
    command=stop_script,
    width=10,
    bg="#ff5733",
    fg="white",
    font=("Helvetica", 12),
)
stop_button.grid(row=1, column=1, padx=10, pady=10)

root.geometry("300x150")  # Set the window size
root.resizable(False, False)  # Make the window size fixed
root.mainloop()
