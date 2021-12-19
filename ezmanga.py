import click
from manga_down import mangareader
import platform
import getpass
import os

# import random shit

@click.group()
def CLI():
    pass # OwO

operatingSystem = platform.system()
user = getpass.getuser()

if operatingSystem == "Linux":
    defaultSave = r"/home/" + user + "/Downloads"
if operatingSystem == "Windows":
    ezMangaDirCheck = os.path.isdir(r"c:\\users\\{}\\AppData\Local\ezManga").format(os.getenv("username"))
    if ezMangaDirCheck == False:
        os.mkdir(r"c:\\users\\{}\\AppData\Local\ezManga")
        defaultSave = r"c:\\users\\{}\\AppData\Local\ezManga".format(os.getenv("username"))
    if ezMangaDirCheck == True:
            efaultSave = r"c:\\users\\{}\\AppData\Local\ezManga".format(os.getenv("username"))
if operatingSystem == "Darwin": # Darwin = OSX
        defaultSave = r"/home/" + user + "/Downloads"

@click.command()
@click.option("--manga", help="Input name of the manga you want to download.")
@click.option("--chapterlist", help="Returns the amount of chapters available for the manga you want to download.")
@click.option("--chaptertodownload", help="The chapter number of the manga you want to download")
@click.option("--saveto", help="Input location to download manga to.", default=defaultSave)

def ezManga():
    pass


if __name__ == '__main__':
    CLI()