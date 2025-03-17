import os
import shutil
from addingapps import getPathdir

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Scripts": [".py", ".js", ".bat", ".sh"]
    }

    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(directory, folder, file))
                    break
    
    # Organize folders
    folder_category = "Folders"
    folder_category_path = os.path.join(directory, folder_category)
    if not os.path.exists(folder_category_path):
        os.makedirs(folder_category_path)

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path) and item not in file_types.keys() and item != folder_category:
            shutil.move(item_path, os.path.join(folder_category_path, item))

    print("Files and folders organized successfully!")


if __name__ == "__main__":
    path = getPathdir()
    organize_files(path)