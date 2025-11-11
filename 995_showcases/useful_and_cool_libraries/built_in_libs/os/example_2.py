
import os
import shutil

def organize_files(directory):
    """
    Organize files in a directory by creating folders for each file type
    and moving files into their respective folders.
    """
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist!")
        return

    # Change to the target directory
    os.chdir(directory)
    print(f"Organizing files in: {os.getcwd()}\n")

    # Define file type categories
    file_categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.java', '.cpp', '.js', '.html', '.css']
    }

    # Get all files in the directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    if not files:
        print("No files to organize!")
        return

    organized_count = 0

    # Process each file
    for filename in files:
        # Skip this script itself
        if filename == os.path.basename(__file__):
            continue

        # Get file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Find the appropriate category
        category = 'Others'
        for cat, extensions in file_categories.items():
            if extension in extensions:
                category = cat
                break

        # Create category folder if it doesn't exist
        if not os.path.exists(category):
            os.makedirs(category)
            print(f"Created folder: {category}")

        # Move file to category folder
        destination = os.path.join(category, filename)
        if not os.path.exists(destination):
            shutil.move(filename, destination)
            print(f"Moved: {filename} -> {category}/")
            organized_count += 1

    print(f"\nOrganization complete! {organized_count} files organized.")

# Example usage
if __name__ == "__main__":
    # Demo: Create a test directory structure
    test_dir = "test_organize"

    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
        print(f"Created test directory: {test_dir}\n")

        # Create some dummy files for demonstration
        test_files = [
            'photo1.jpg', 'document.pdf', 'video.mp4',
            'song.mp3', 'archive.zip', 'script.py',
            'report.docx', 'image2.png'
        ]

        for file in test_files:
            filepath = os.path.join(test_dir, file)
            with open(filepath, 'w') as f:
                f.write('dummy content')

        print("Created test files for demonstration\n")

    # Organize the test directory
    organize_files(test_dir)

    print("\n" + "="*50)
    print("TIP: Modify the directory path to organize your own files!")
    print("="*50)