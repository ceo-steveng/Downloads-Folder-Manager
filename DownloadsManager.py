import os

source_dir = "/Users/StevenGarcia 1/Downloads/"

with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)