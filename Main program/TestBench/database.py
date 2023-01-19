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


# get all informations and store it in
def getAll(cursor, musicTab, dirTab, cleanUpdate):
    if cleanUpdate:
        musicTab = []
        dirTab = []

    tmp = cursor.execute("SELECT * from music").fetchall()
    for i in range(0, len(tmp)):
        musicTab.append(tmp[i][1])
        dirTab.append(tmp[i][0])


