import pyautogui
import random
import time
from datetime import datetime

# Prevent pyautogui from raising exceptions when mouse hits screen edges
pyautogui.FAILSAFE = False

def move_mouse():
    print(f"Mouse mover started at {datetime.now().strftime('%H:%M:%S')}")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            # Get current screen size
            screen_width, screen_height = pyautogui.size()
            
            # Get current mouse position
            current_x, current_y = pyautogui.position()
            
            # Generate small random movement (-10 to +10 pixels)
            move_x = random.randint(-10, 80)
            move_y = random.randint(-10, 50)
            
            # Calculate new position
            new_x = max(0, min(current_x + move_x, screen_width))
            new_y = max(0, min(current_y + move_y, screen_height))
            
            # Move mouse smoothly to new position
            pyautogui.moveTo(new_x, new_y, duration=0.5)
            
            # Wait for 30 seconds before next movement
            time.sleep(30)
            
    except KeyboardInterrupt:
        print(f"\nMouse mover stopped at {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    move_mouse()
