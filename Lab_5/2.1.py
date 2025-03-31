import os
import shutil
import sys

def find_small_files(folder):
    small_files = []
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.getsize(file_path) < 2048:
                small_files.append(file_path)
    return small_files

def main(folder):
    small_files = find_small_files(folder)
    if small_files:
        print("find:")
        for file in small_files:
            print(file)
        small_folder = os.path.join(folder, "small")
        os.makedirs(small_folder, exist_ok=True)
        for file in small_files:
            shutil.copy(file, small_folder)
        print(f"all copy to: {small_folder}")
    else:
        print("not find.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = os.getcwd()
    main(folder_path)
