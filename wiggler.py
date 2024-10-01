import tkinter as tk
from threading import Thread
import pyautogui
import time
import keyboard  # To detect 'q' and 'r' key press to stop or restart the script
import random  # To generate random movement values
from PIL import Image, ImageDraw  # To create tray icon
import pystray  # For system tray icon

# Global variables to control the loop and tray icon
running = False
tray_icon = None  # Declare tray_icon globally
q_press_count = 0  # Counter for 'q' key presses
r_press_count = 0  # Counter for 'r' key presses
q_press_threshold = 5  # Number of 'q' presses to stop the script
r_press_threshold = 5  # Number of 'r' presses to restart the script

# Total number of tabs you want to consider (change this according to your needs)
total_tabs = (
    10  # Adjust this value to match the number of tabs you want to cycle through
)


# Function to switch to a random tab
def switch_tabs():
    random_tab = random.randint(0, total_tabs - 1)  # Select a random tab index
    for _ in range(random_tab):
        pyautogui.hotkey("ctrl", "tab")  # Switch to the next tab
        time.sleep(0.1)  # Short delay to ensure the tab switch occurs
    time.sleep(1)  # Delay after switching


# Function to scroll down randomly
def scroll_down():
    scroll_amount = random.randint(100, 1000)  # Generate a random scroll amount
    pyautogui.scroll(-scroll_amount)  # Scroll down
    time.sleep(2)  # Increased delay to slow down scrolling


# Function to scroll up randomly
def scroll_up():
    scroll_amount = random.randint(100, 1000)  # Generate a random scroll amount
    pyautogui.scroll(scroll_amount)  # Scroll up
    time.sleep(2)  # Increased delay to slow down scrolling


# Function to move the mouse slightly
def move_mouse():
    # Generate random movement in the range of -5 to 5 pixels for both x and y
    move_x = random.randint(-5, 5)
    move_y = random.randint(-5, 5)
    pyautogui.move(
        move_x, move_y, duration=0.3
    )  # Increased duration for smoother movement
    time.sleep(0.5)  # Increased delay after mouse movement


# Function to run the tab switching and scrolling process
def start_scrolling():
    global running
    running = True
    while running:
        move_mouse()  # Move the mouse slightly
        switch_tabs()  # Switch tabs randomly
        scroll_down()  # Scroll down randomly
        scroll_up()  # Scroll up randomly


# Function to stop the scrolling process
def stop_scrolling():
    global running
    running = False
    # print("Quit")  # Print confirmation to terminal when quitting


# Function to restart the scrolling process
def restart_scrolling():
    global running, thread, r_press_count
    stop_scrolling()  # Stop current scrolling process
    # # print("Restart")  # Print confirmation to terminal when restarting
    r_press_count = 0  # Reset the 'r' key press count
    run_in_thread()  # Restart the process


# Threaded function to avoid blocking the GUI
def run_in_thread():
    global thread
    thread = Thread(target=start_scrolling)
    thread.start()


# Function to create tray icon image
def create_image(width, height, color1, color2):
    image = Image.new("RGB", (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
    dc.rectangle((0, height // 2, width // 2, height), fill=color2)
    return image


# System Tray Menu
def setup_tray_icon():
    global tray_icon
    icon_image = create_image(64, 64, "black", "blue")
    tray_icon = pystray.Icon(
        "Tab Switcher",
        icon_image,
        menu=pystray.Menu(
            pystray.MenuItem("Start", lambda: run_in_thread()),
            pystray.MenuItem("Stop", lambda: stop_scrolling()),
            pystray.MenuItem("Quit", lambda: quit_app()),
        ),
    )
    tray_icon.run()


# Quit application
def quit_app():
    stop_scrolling()  # Stop the scrolling
    if tray_icon is not None:
        tray_icon.stop()  # Stop the tray icon
    # # print("Quit")  # Print confirmation to terminal when quitting


# Function to handle keypress events and implement counter logic
def handle_keypress(e):
    global q_press_count, r_press_count, running

    if e.name == "q":
        q_press_count += 1
        # print(f"'q' pressed: {q_press_count} times")
        if q_press_count >= q_press_threshold:
            stop_scrolling()  # Stop the script if 'q' is pressed 5 times
    elif e.name == "r":
        r_press_count += 1
        # print(f"'r' pressed: {r_press_count} times")
        if r_press_count >= r_press_threshold:
            restart_scrolling()  # Restart the script if 'r' is pressed 5 times
    else:
        # Reset counters if any other key is pressed
        # print(f"Other key '{e.name}' pressed. Resetting counters.")
        q_press_count = 0
        r_press_count = 0


# Start listening to keypresses using the keyboard module
keyboard.on_press(handle_keypress)

if __name__ == "__main__":

    tray_icon_thread = Thread(target=setup_tray_icon)
    tray_icon_thread.start()
    keyboard.wait()  # Keep the script running to listen for keypresses

# to generate executable file # and get the file from dest directory
# pyinstaller --onefile --windowed main.py
