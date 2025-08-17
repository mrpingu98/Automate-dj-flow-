import pyautogui
import time

# Coordinates of the Soulseek search bar — update these!
SEARCH_BAR_COORDS = (418, 179)  # ← YOU MUST UPDATE THIS BASED ON YOUR SCREEN

# Load song list
with open("songs.txt", "r") as file:
    songs = [line.strip() for line in file if line.strip()]

print(f"Loaded {len(songs)} songs to search.")

# Countdown so you can switch to Soulseek
print("You have 5 seconds to switch to Soulseek window...")
time.sleep(5)

for i, song in enumerate(songs, start=1):
    print(f"({i}/{len(songs)}) Searching for: {song}")

    # Click the search bar to ensure it's focused
    pyautogui.click(*SEARCH_BAR_COORDS)
    time.sleep(5)

    # Clear and enter new search
    pyautogui.write(song, interval=0.05)
    pyautogui.press("enter")

    print(f"Searched: {song}")
    time.sleep(5)  # Adjust time to manually review/download

print("✅ All searches complete.")