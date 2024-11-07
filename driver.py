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

