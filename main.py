from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "jpeg"
                                       or extension[1].lower() == "png"):
                file = folder_track + "/" + filename
                new_path = folder_dest_photo + "/" + filename
                os.rename(file, new_path)
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "mp3" or extension[1].lower() == "aac"
                                       or extension[1].lower() == "flac"):
                file = folder_track + "/" + filename
                new_path = folder_dest_music + "/" + filename
                os.rename(file, new_path)
        for filename in os.listdir(folder_track):
            extension = filename.split(".")
            if len(extension) > 1 and (extension[1].lower() == "txt" or extension[1].lower() == "doc"
                                       or extension[1].lower() == "docx" or extension[1].lower() == "pdf"):
                file = folder_track + "/" + filename
                new_path = folder_dest_document + "/" + filename
                os.rename(file, new_path)


folder_track = 'C:/Users/ilya/Downloads'
folder_dest_photo = 'C:/Users/ilya/Pictures'
folder_dest_music = 'C:/Users/ilya/Music'
folder_dest_document = 'C:/Users/ilya/Documents'
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)

observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
