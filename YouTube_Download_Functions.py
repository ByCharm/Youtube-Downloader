# Press Umschalt + F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pafy
# https://pythonhosted.org/pafy/
import os


def create_pafy_object(link):
    return pafy.new(link)


def create_download_folder():
    # desktop stores the direction to desktop on windows
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE'], "Desktop"))
    desktop = desktop + "\\" + "YT_Download_Folder"
    if not os.access(desktop, os.F_OK):
        os.mkdir(desktop + "\\" + "YT_Download_Folder")

    return desktop


def run_engine(url):
    download_folder = create_download_folder()
    try:
        my_vid = create_pafy_object(url)
        stream = my_vid.getbest()
        stream.download(download_folder)
    except ValueError:
        print("Invalid URL")
