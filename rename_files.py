from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import os

folder = "/Users/manvirsalh/Documents/Rename songs"  # <- replace with your actual folder

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    print(f"Checking: {file}")

    if not path.lower().endswith(".mp3"):
        print(f"Skipping (not mp3): {file}")
        continue

    try:
        audio = MP3(path, ID3=EasyID3)
        artist = audio.get("artist", [None])[0]
        title = audio.get("title", [None])[0]

        if artist and title:
            new_name = f"{artist} - {title}.mp3"
            new_path = os.path.join(folder, new_name)

            if os.path.exists(new_path):
                print(f"File already exists, skipping: {new_name}")
                continue

            print(f"Renaming to: {new_name}")
            os.rename(path, new_path)
        else:
            print(f"Missing tags: {file}")

    except Exception as e:
        print(f"Error reading {file}: {e}")