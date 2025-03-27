import os
import subprocess
import shutil
import re

REGEX = r'([a-zA-Z]:[\\\/](?:[a-zA-Z0-9]+[^WINDOWS][\\\/])+.+\.dll\b)'

if __name__ == "__main__":
    # Run ntldd process
    executable_path = input("Executable Path: ")
    output = subprocess.check_output(f"ntldd {executable_path}", shell=True).decode("utf-8")

    # Match REGEX
    file_paths = re.findall(REGEX, output)
    
    # Create required_libraries
    if not os.path.exists("required_libraries"):
        os.mkdir("required_libraries")
    build_path = os.getcwd() + "\\required_libraries"

    # Copy .dll files to build_path
    for filepath in file_paths:
        print("Retrieving " + filepath)
        try:
            shutil.copy2(filepath, build_path)
        except PermissionError:
            print("File already exists at build path")
