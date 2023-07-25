import sqlite3
import os

debug = False
unstable = False
con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS directories(id INTEGER PRIMARY KEY, dir)")
cur.execute("CREATE TABLE IF NOT EXISTS music(id INTEGER PRIMARY KEY, path)")


# find in database functions
def checkInDatabase(cursor, dirIn):
    return cursor.execute("SELECT COUNT(*) from directories WHERE dir=?", [dirIn]).fetchone()[0] > 0


def checkInMusic(cursor, musIn):
    return cursor.execute("SELECT COUNT(*) from music WHERE path=?", [musIn]).fetchone()[0] > 0


# add elements to database
def addMusic(cursor, musIn):
    if not os.path.isfile(musIn) and debug:
        print("Path / music does not exist")
    elif checkInMusic(cursor, musIn) and debug:
        print("Already in music database: <" + str(musIn) + ">")
    else:
        cursor.execute("INSERT INTO music(path) VALUES (?)", [musIn])
        con.commit()


def addDirectory(cursor, dirIn):
    if not os.path.isdir(dirIn) and debug:
        print("Dir does not exist")
    elif checkInDatabase(cursor, dirIn) and debug:
        print("Already in database: " + str(dirIn))
    else:
        cursor.execute("INSERT INTO directories(dir) VALUES (?)", [dirIn])
        if debug:
            print(cursor.rowcount)
        con.commit()


# get all dirs
def getAllDirs(cursor):
    return cursor.execute("SELECT dir from directories").fetchall()


def updateDatabase(cursor):
    tmpDir = getAllDirs(cursor)
    dirs = []

    for i in tmpDir:
        newDir = i[0]
        if os.path.isdir(newDir):
            dirs.append(newDir)
    del tmpDir

    for musicDir in dirs:
        for root, dirs, files in os.walk(musicDir):
            for file in files:
                if file.endswith(".mp3"):  # or file.endswith(".m4a"):
                    # print(os.path.join(root, file))
                    # fileList.append(os.path.join(root, file))
                    addMusic(cursor, os.path.join(root, file))
    return


def getLastIndex(cursor) -> int:
    return cursor.execute("SELECT MAX(id) from music").fetchone()[0]


def getFileByIndex(cursor, index):
    return cursor.execute("SELECT path from music where id=?", [index]).fetchone()[0]


def firstRunCheck():
    if unstable:
        cur.execute("DELETE FROM music if exists")
        cur.execute("DELETE FROM directories if exists")
        con.commit()
    if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + r"\firstRun.txt"):
        if os.path.exists("firstRun.txt"):
            os.remove("firstRun.txt")
    else:
        return

    while True:
        a = input("First time running...\nPlease give a valid directory for music search:\n")
        if os.path.exists(a):
            addDirectory(cur, a)
            updateDatabase(cur)
            print("\nThank you, got it!")
            break
        else:
            print("Invalid path...\nTry again :)")
    return
