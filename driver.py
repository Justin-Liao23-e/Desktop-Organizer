import os #operating system interaction
import shutil #file operations
import time 

# Watchdog Library
from watchdog.observers import Observer #monitor file system events
from watchdog.events import FileSystemEventHandler #handle file system events

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads") #concatenate the user's home directory with the Downloads folder
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop") #concatenate the user's home directory with the Desktop folder

# Dictionary Mapping File Extensions to Folder Names
file_extensions = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Others': []  #for all other file types
}

# Function: move a file to a specified category folder
def move_file(item_path, category): #item_path: full path to the file in Downloads; category: category folder on the Desktop

    category_path = os.path.join(desktop_path, category) #catergory folder path
    
    # If the Category Folder NOT Exists
    if not os.path.exists(category_path):
        os.makedirs(category_path) #create the folder with name of the category passed: when organize_files() is called
        print(f"Created folder: {category}") 
    
    destination = os.path.join(category_path, os.path.basename(item_path)) #file destination path to the category folder
    
    # If the File Already Exists
    if os.path.exists(destination):
        name, ext = os.path.splitext(os.path.basename(item_path)) #split the file name and extension
        new_name = f"{name}_{int(time.time())}{ext}" #add a timestamp to the file name
        destination = os.path.join(category_path, new_name) #update the destination path
    
    # Move File Operation
    try:
        shutil.move(item_path, destination) #file to the destination path
        print(f"Moved {os.path.basename(item_path)} to {category}")
    except Exception as e: 
        print(f"Error moving {os.path.basename(item_path)}: {e}")

# Function: scans and organize files in the Downloads folder
def organize_files():

    # Iterate through Each Item (File/Folder) within Downloads
    for item in os.listdir(downloads_path):
        
        item_path = os.path.join(downloads_path, item) #full path to the item in Downloads
        if os.path.isdir(item_path): #skip directories
            continue
        
        extension = os.path.splitext(item)[1].lower() #obtain the file extension and convert to lowercase
        check = False #check if the file belong to a category
        
        # Iterate through Each Category and its Extensions from file_extensions (above)
        for category, extensions in file_extensions.items():
            
            if extension in extensions: #file extension matches the category
                move_file(item_path, category) #call move_file()
                check = True
                break
        
        # Unmatched File Extensions
        if not check:
            move_file(item_path, 'Others') #moves to Others category

# Class: DownloadHandler
class DownloadHandler(FileSystemEventHandler):
    
    # Function: called when a file is created in the Downloads folder
    def on_created(self, event):
        if not event.is_directory: #skip directories
            time.sleep(1)  #wait for 1 sec
            organize_files()

# Main Function
if __name__ == "__main__":
    event_handler = DownloadHandler() #create DownloadHandler object
    observer = Observer() #create Observer object
    observer.schedule(event_handler, path=downloads_path, recursive=False)
    observer.start() 
    print("Session Begins...")

    try:
        while True: #run the program until interrupted
            time.sleep(1) 
    except KeyboardInterrupt:
        observer.stop()
    observer.join() #wait for the observer to finish