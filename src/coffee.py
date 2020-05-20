import sys
import pyperclip
import requests
from time import sleep
import glob
import os

base = "https://file.coffee/"

def set_clipboard(url):
    pyperclip.copy(url)


def post(file):
    # @file: File name
    response = requests.post(
        url=f"{endpoint}api/v1/upload",
        files={
            "file": open(file, "rb")
        }
    ).json()

    if response["success"]:
        return endpoint + response["filename"]
    return None


def main():
    os.system("")
    # External argument
    ext_dir = sys.argv[1]
    while True:
        files_in_dir = glob.glob(f"{ext_dir}*.png")

        if files_in_dir:
            for file in files_in_dir:
                url = post(file)
                if url:
                    set_clipboard(url)
                    os.remove(file)
        sleep(2)


if __name__ == '__main__':
    main()