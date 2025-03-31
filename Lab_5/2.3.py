import os
import argparse
def create_missing_files(dirpath, missing_files):
    created_files = []
    for filename in missing_files:
        file_path = os.path.join(dirpath, filename)
        if not os.path.isfile(file_path):
            with open(file_path, 'w') as f:
                f.write(f'This is a placeholder for {filename}\n')
            created_files.append(filename)
    return created_files
def main(dirpath, missing_files_file):
    if not os.path.isfile(missing_files_file):
        print(f'no files: {missing_files_file}')
        return
    with open(missing_files_file, 'r') as f:
        missing_files = [line.strip() for line in f if line.strip()]
    if not missing_files:
        print('No files')
        return
    created_files = create_missing_files(dirpath, missing_files)
    if created_files:
        print(f'New files: "{dirpath}":')
        for file in created_files:
            print(file)
    else:
        print('No files for creation')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="New files:")
    parser.add_argument("--dirpath", type=str, required=True, help="Path")
    parser.add_argument("--missing_files_file", type=str, required=True, help="path to new files")
    args = parser.parse_args()
    main(args.dirpath, args.missing_files_file)