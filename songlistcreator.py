import os
import json
import random
import sys
import time

import os
import json
import random

def process_song_folder(song_folder):
    song_name = os.path.basename(song_folder)
    # Replace '-' with ' : ' for the id
    song_id = song_name.replace('-', ':')
    # Example: random year and timestamp (customize as needed)
    year = random.choice([1993, 1997])
    timestamp = 1673742039  # Or use random.randint(...) or int(time.time())
    return {
        "id": song_id,
        "l": "en",
        "y": year,
        "t": timestamp
    }

def generate_music_json(root_dir):
    output = {}
    # Only process first-level folders in root_dir
    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)
        if os.path.isdir(folder_path):
            songs = []
            for song_folder in os.listdir(folder_path):
                song_path = os.path.join(folder_path, song_folder)
                if os.path.isdir(song_path):
                    songs.append(process_song_folder(song_path))
            output[folder_name] = songs
    return output

if __name__ == "__main__":
    root_folder ="/Users/marko/Music/UltraStar Deluxe"  # Change to your music root directory
    output_file = "songlist.json"  # Default output file

    # Optionally allow command-line arguments for folder and output file
    if len(sys.argv) > 1:
        root_folder = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    data = generate_music_json(root_folder)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"JSON data saved to {output_file}")

# if __name__ == "__main__":
#     root_folder = "/Users/marko/Music/UltraStar Deluxe"  # Change this to your target directory
#     data = generate_music_json(root_folder)
#     print(json.dumps(data, indent=2))

