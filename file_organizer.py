import os
import shutil

def setup_organizer():
    print("Welcome to the File Organizer Setup!")
    print("Let's set up the directories and file types.\n")

    source_dir = input("Enter the source directory path: ").strip()
    if not os.path.isdir(source_dir):
        raise ValueError("Source directory does not exist or is invalid.")
    
    file_types = {}
    print("\nEnter file types to organize (e.g., Images -> .jpg, .jpeg, .png):")
    while True:
        category = input("Category name (or 'done' to finish): ").strip()
        if category.lower() == 'done':
            break
        extensions = input("File extensions (comma-separated): ").strip().split(',')
        file_types[category] = [ext.strip() for ext in extensions if ext.strip()]
    
    for category in file_types:
        dest_dir = os.path.join(source_dir, category)
        os.makedirs(dest_dir, exist_ok=True)
        print(f"Created directory: {dest_dir}")
    
    return source_dir, file_types

def organize_files(source_dir, file_types):
    for file_name in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, file_name)):
            file_ext = os.path.splitext(file_name)[1].lower()
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    src_path = os.path.join(source_dir, file_name)
                    dest_path = os.path.join(source_dir, category, file_name)
                    shutil.move(src_path, dest_path)
                    print(f"Moved {file_name} to {category}")

if __name__ == "__main__":
    try:
        source_directory, file_types = setup_organizer()
        organize_files(source_directory, file_types)
        print("\nFile organization complete!")
    except Exception as e:
        print(f"Error occurred: {str(e)}")