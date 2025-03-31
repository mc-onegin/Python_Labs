import os
import argparse

def check_files_in_directory(dirpath, filenames):
    present_files = []
    absent_files = []

    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        if os.path.isfile(file_path):
            present_files.append(filename)
        else:
            absent_files.append(filename)

    return present_files, absent_files

def folder_info(dirpath):
    total_files = 0
    total_size = 0

    for _, _, files in os.walk(dirpath):
        total_files += len(files)
        total_size += sum(os.path.getsize(os.path.join(dirpath, f)) for f in files)

    return total_files, total_size

def main(dirpath, filenames):
    if filenames:
        present_files, absent_files = check_files_in_directory(dirpath, filenames)

        print("files:")
        for file in present_files:
            print(file)

        print("\nnot found files:")
        for file in absent_files:
            print(file)

        with open("present_files.txt", "w") as present_file:
            for file in present_files:
                present_file.write(file + "\n")

        with open("absent_files.txt", "w") as absent_file:
            for file in absent_files:
                absent_file.write(file + "\n")

    else:
        total_files, total_size = folder_info(dirpath)
        print(f"In '{dirpath}' count of files: {total_files}")
        print(f"size: {total_size} bytes")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="check files in directory")
    parser.add_argument("--dirpath", type=str, default=os.getcwd(), help="path to folder")
    parser.add_argument("--files", nargs='*', help="list names")
    args = parser.parse_args()
    main(args.dirpath, args.files)