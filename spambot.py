import time
import pyautogui

time.sleep(3)                      # Delayes the starting

message = "spam message"           # Message to be delivered
repeat = 10                        # Number of time to be repeated

for i in range(repeat):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
