from os.path import exists, join, splitext
import os
import shutil
import time
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

downloadsFolder = "/Users/paulostos/Downloads" 
document_files = "/Users/paulostos/Desktop/Documents" 
pp_files = "/Users/paulostos/Desktop/PowerPoints" 
image_files = "/Users/paulostos/Desktop/Images"
lucas_music = "/Users/paulostos/Desktop/LucaMusic" 


image_extensions = [".jpeg", ".jpg", ".png"]
audio_extensions = [".mp3", ".mp4", "wma"]
pp_extensions = [".pptx", ".ppt"]
document_extensions = [".docx", ".txt", ".pdf", ".doc", ".xls"] 

## method to make unique file names, prevents overriding files 
def makeUnique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # if file exists add number to the end of the file name
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1 
    return name 
    
# method to move file from downloads folder to the appropriate folder 
def moveFile(dest, entry, name):
    try: 
        if exists(f"{dest}/{name}"):
            name = makeUnique(dest, name)
        shutil.move(entry.path, join(dest, name))
    except Exception as e:
        logging.error(f"Failed to move file {name}: {e}")


class FileOrganizer(FileSystemEventHandler):
    def on_modified(self, event): 
        with os.scandir(downloadsFolder) as files: 
            for file in files: 
                name = file.name.lower()
                self.check_audio_files(file, name)
                self.check_pp_files(file, name)
                self.check_image_files(file, name)
                self.check_doc_files(file, name)   
        

    def check_audio_files(self, entry, name): 
        for audio_extension in audio_extensions: 
            if name.lower().endswith(audio_extension):
                dest = lucas_music
                moveFile(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_pp_files(self, entry, name): 
        for pp_extension in pp_extensions:
            if name.lower().endswith(pp_extension):
                dest = pp_files
                moveFile(dest, entry, name)
                logging.info(f"Moved PowerPoint file: {name}")

    def check_image_files(self, entry, name): 
        for image_extension in image_extensions: 
            if name.lower().endswith(image_extension): 
                dest = image_files
                moveFile(dest, entry, name)
                logging.info(f"Moved image file: {name}")
    
    def check_doc_files(self, entry, name): 
        for document_extension in document_extensions: 
            if name.lower().endswith(document_extension): 
                dest = document_files
                moveFile(dest, entry, name)
                logging.info(f"Moved document file: {name}")



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = downloadsFolder
    event_handler = FileOrganizer()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()