import pyautogui
import random
import time

# Define time delay between switching apps and scrolling
switch_delay = 4  # Increased delay between app switches to make it more noticeable
scroll_delay = 2  # Adjust the delay time between scroll actions

# Screen dimensions (pyautogui.size() will give you the screen width and height)
screen_width, screen_height = pyautogui.size()

def random_app_switch():
    # Randomly choose how many apps to cycle through, up to a reasonable limit (e.g., 1 to 7)
    app_jumps = random.randint(1, 7)
    
    # Hold down Alt (or Command on macOS) and press Tab multiple times to switch apps
    pyautogui.keyDown('alt')  # Use 'command' for macOS
    for _ in range(app_jumps):
        pyautogui.press('tab')
        time.sleep(0.3)  # Small delay between each tab press to make it noticeable
    pyautogui.keyUp('alt')

def random_scroll():
    # Randomly decide to scroll up or down with a bigger, more noticeable scroll
    scroll_direction = random.choice(['up', 'down'])
    scroll_amount = random.randint(50, 200)  # Increase the scroll amount for more noticeable movement
    
    if scroll_direction == 'down':
        pyautogui.scroll(-scroll_amount)  # Scroll down
    else:
        pyautogui.scroll(scroll_amount)  # Scroll up

def random_mouse_move():
    # Move the mouse a small random amount in a random direction
    move_x = random.randint(-50, 50)  # Random x-axis movement
    move_y = random.randint(-50, 50)  # Random y-axis movement
    
    # Get current mouse position
    current_x, current_y = pyautogui.position()
    
    # Make sure the mouse stays within the screen boundaries
    new_x = max(0, min(screen_width, current_x + move_x))
    new_y = max(0, min(screen_height, current_y + move_y))
    
    # Move the mouse to the new position
    pyautogui.moveTo(new_x, new_y, duration=0.5)  # Smooth movement over 0.5 seconds

def main():
    while True:
        # Random app switching
        random_app_switch()
        time.sleep(switch_delay)  # Wait for a random time before switching again

        # Random scrolling
        random_scroll()
        time.sleep(scroll_delay)  # Wait for a random time before scrolling again

        # Random mouse movement
        random_mouse_move()
        time.sleep(1)  # Short delay before the next action

if __name__ == "__main__":
    main()
