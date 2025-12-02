import sys
import shutil
from pathlib import Path


def parse_arguments():
    """Parse command line arguments"""

    # Check that at least source directory is provided
    if len(sys.argv) < 2:
        print("No source directory provided.")
        return None

    src_path = Path(sys.argv[1])

    # Create default directory if destination is not provided
    if len(sys.argv) >= 3:
        dest_path = Path(sys.argv[2])
    else:
        dest_path = Path("dist")

    # Check that source directory exists
    if not src_path.exists():
        print("Source directory does not exist.")
        return None

    # Check that source directory is directory
    if not src_path.is_dir():
        print("Source directory is not a directory.")
        return None

    # Check that destination directory is directory
    if dest_path.exists() and not dest_path.is_dir():
        print("Destination directory is not a directory.")
        return None

    # Check difference between source and destination directories
    if src_path.resolve() == dest_path.resolve():
        print("Source and destination directories must be different.")
        return None

    return src_path, dest_path


def copy_files(src_path, dest_path):
    """Copy files from source directory to destination directory"""
    try:
        # Get file extension
        extension = src_path.suffix.lower()

        # Use file extension as directory name
        directory = extension[1:] if extension else "no_extension"
        dest_dir_path = dest_path / directory

        # Create destination directory
        dest_dir_path.mkdir(parents=True, exist_ok=True)

        target_path = dest_dir_path / src_path.name

        # Copy files
        shutil.copy2(src_path, target_path)

    except Exception as e:
        print("Problem with copying")


def iterate_folder(src_dir, dest_root):
    """Iterate through source directory and copy files to destination directory"""
    try:
        for item in src_dir.iterdir():
            if item.is_dir():
                iterate_folder(item, dest_root)
            else:
                copy_files(item, dest_root)
    except PermissionError:
        print("Access denied.")
    except Exception as e:
        print("Error reading directory")


def main():
    """Main function: parse command line arguments, iterate through source directory and copy files to destination directory"""

    arguments = parse_arguments()
    if arguments is None:
        return

    src_path, dest_path = arguments

    try:
        dest_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print("Cannot create destination directory")
        return

    iterate_folder(src_path, dest_path)

    print("Done!")


if __name__ == "__main__":
    main()
