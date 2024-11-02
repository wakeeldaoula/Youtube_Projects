import os
import shutil

def organize_files(source_dir):
    # Define the file type categories
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Archives': ['.zip', '.rar', '.tar'],
    }

    # Create subdirectories for each file type
    for folder in file_types.keys():
        folder_path = os.path.join(source_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Move files to their respective folders
    for filename in os.listdir(source_dir):
        file_extension = os.path.splitext(filename)[1].lower()
        source_file = os.path.join(source_dir, filename)

        if os.path.isfile(source_file):  # Check if it is a file
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(source_file, os.path.join(source_dir, folder, filename))
                    print(f'Moved: {filename} to {folder}/')
                    break

if __name__ == "__main__":
    directory_to_organize = input("Enter the path of the directory to organize: ")
    organize_files(directory_to_organize)
    print("File organization complete.")