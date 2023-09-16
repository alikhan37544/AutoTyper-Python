import pyautogui
import time
from tqdm import tqdm

delay = 5  # Initial Delay in Seconds
time.sleep(delay)

name = r"typedstuff.txt"   # File Name in Windows
# name = r"/home/bob/Desktop/file.txt"   # File Name in Linux
interval = 0   # In Seconds

# Determine the total number of characters to be written
with open(name) as f:
    data = f.read()
total_characters = len(data)

# Initialize the progress bar
# with tqdm(total=total_characters, desc="Writing Text") as pbar:
for char in data:
    pyautogui.write(char, interval=interval)
        # pbar.update(1)
