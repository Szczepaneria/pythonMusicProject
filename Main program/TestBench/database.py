import sqlite3
import os

con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS directories(dir)")
cur.execute("CREATE TABLE IF NOT EXISTS music(dir, name)")


# find in database functions
def checkInDatabase(cursor, dirIn):
    return cursor.execute("SELECT COUNT(*) from directories WHERE dir=?", [dirIn]).fetchone()[0] > 0


def checkInMusic(cursor, musIn):
    return cursor.execute("SELECT COUNT(*) from music WHERE dir=?", [musIn]).fetchone()[0] > 0


# add elements to database
def addMusic(cursor, musIn):
    if os.path.exists(musIn) and not checkInMusic(cursor, musIn):
        cursor.execute("INSERT INTO music(dir, name) VALUES (" + musIn + ", " + os.path.basename(musIn))
    else:
        print("Path does not exist")


def addDirectory(cursor, dirIn):
    if os.path.isdir(dirIn) and not checkInDatabase(cursor, dirIn):
        cursor.execute("INSERT INTO directories(dir) VALUES (" + dirIn)
    else:
        print("Dir does not exist")


# get all dirs
def getAllDirs(cursor):
    return cursor.execute("SELECT * from dirs").fetchall()


def updateDatabase(cursor):
    tmpDir = getAllDirs(cursor)
    dirs = []

    for i in range(0, len(tmpDir) - 1):
        newDir = tmpDir[i][0]
        if os.path.isdir(newDir):
            dirs.append(newDir)
    del tmpDir

    fileList = []
    for musicDir in dirs:
        for root, dirs, files in os.walk(musicDir):
            for file in files:
                if file.endswith(".mp3"):  # or file.endswith(".m4a"):
                    print(os.path.join(root, file))
                    fileList.append(os.path.join(root, file))
    if fileList.__len__() == 0:
        exit("No directories found!")
    else:
        return fileList


# get all informations and store it in
def getAll(cursor, musicTab, dirTab, cleanUpdate):
    if cleanUpdate:
        musicTab = []
        dirTab = []

    tmp = cursor.execute("SELECT * from music").fetchall()
    for i in range(0, len(tmp) - 1):
        musicTab.append(tmp[i][1])
        dirTab.append(tmp[i][0])
