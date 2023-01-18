import sqlite3
import os
from pathlib import Path

con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS directories(dir)")
cur.execute("CREATE TABLE IF NOT EXISTS music(dir, name)")


def checkInDatabase(cursor, dirIn):
    return cursor.execute("SELECT COUNT(*) from directories WHERE dir=?", [dirIn]).fetchone()[0] > 0


def checkInMusic(cursor, musIn):
    return cursor.execute("SELECT COUNT(*) from music WHERE dir=?", [musIn]).fetchone()[0] > 0


def addMusic(cursor, musIn):
    cursor.execute("INSERT INTO music(dir, name) VALUES (" + musIn + ", " + Path(musIn).stem)


def addDirectory(cursor, dirIn):
    cursor.execute("INSERT INTO directories(dir) VALUES (" + dirIn)

# def getSongs():


# def addDirectory():
#     directory = input("Please give a valid directory: ")
#     if os.path.exists(directory):

# if __name__ == "__main__":
# print("")
