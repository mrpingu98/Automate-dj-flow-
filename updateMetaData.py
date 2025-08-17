from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
import os

folder = "/Users/manvirsalh/Documents/Rename songs" 

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    print(f"\nChecking: {file}")

    if not path.lower().endswith(".mp3"):
        print(f"Skipping (not mp3): {file}")
        continue

    try:
        try:
            audio = MP3(path, ID3=EasyID3)
        except ID3NoHeaderError:
            print("ID3 header missing, initializing...")
            audio = MP3(path)
            audio.add_tags(ID3=EasyID3)
            audio.save()
            audio = MP3(path, ID3=EasyID3)

        # Get current metadata or fallback values
        artist = audio.get("artist", ["Unknown Artist"])[0]
        title = audio.get("title", ["Unknown Title"])[0]

        # Update title to 'artist - title'
        new_title = f"{artist} - {title}"
        audio["title"] = new_title
        audio.save()

        print(f"Updated title to: {new_title}")

    except Exception as e:
        print(f"Error processing {file}: {e}")