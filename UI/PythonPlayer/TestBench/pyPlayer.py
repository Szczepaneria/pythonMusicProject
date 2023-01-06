import pygame
from pygame import mixer as playerMusic
import os
import audioread as info
from PyQt5 import QtCore, QtGui, QtWidgets

dirList = []
fileList = []


def searchFiles():
    # C:\Users\7kube\Music\reszta\mp3
    f = open("directories.txt", "r")
    for x in f:
        if os.path.exists(x):
            dirList.append(x)
        else:
            print("Dir " + str(x) + " does not exist!\n")
    f.close()

    for musicDir in dirList:
        for root, dirs, files in os.walk(musicDir):
            for file in files:
                if file.endswith(".mp3"):  # or file.endswith(".m4a"):
                    print(os.path.join(root, file))
                    fileList.append(os.path.join(root, file))
    if fileList.__len__() == 0:
        exit("No directories found!")
    # check list of directories


def InitPlaylist(musicList, mode):
    if mode == "single":
        if len(list) > 1:
            return InitPlaylist(musicList, "auto")

        elif not os.path.exists(musicList):
            return False

    else:
        listChecked = []
        for i in musicList:
            if os.path.exists(i):
                listChecked.append(i)

        if len(musicList) < 1:
            return False
        else:
            return listChecked


class Player:
    def __init__(self, playlist, mode=1):
        self.playlist = InitPlaylist(playlist, "auto")
        self.currentIndex = 0
        self.maxIndex = len(self.playlist) - 1
        self.currentFile = playlist[self.currentIndex]
        self.currentFileName = os.path.basename(self.currentFile)
        self.currentPlaybackPos = 0.0
        pygame.mixer.init()

        with info.audio_open(self.currentFile) as f:
            self.fileDuration = f.duration
            f.close()

        if mode == 2:
            self.mode = "auto"
        elif mode == 3:
            self.mode = "one loop"
        else:
            self.mode = "loop"
        # auto --> play till the playlist ends
        # stop after 1 --> one stop

        playerMusic.music.set_endevent(pygame.USEREVENT)
        # write a goddamn userevent for this lil bullshit

    def updateBaseData(self) -> None:
        self.currentFile = self.playlist[self.currentIndex]
        self.currentFileName = os.path.basename(self.currentFile)
        with info.audio_open(self.currentFile) as f:
            self.fileDuration = f.duration
            f.close()
        return

    def endEvent(self) -> None:
        if self.mode == "auto":
            if self.currentIndex == self.maxIndex:
                self.currentIndex = 0
            else:
                self.currentIndex += 1

            self.updateBaseData()
            playerMusic.music.load(self.playlist[self.currentIndex])
            playerMusic.music.play()
            print("Playing")
            return

        elif self.mode == "one stop":
            playerMusic.music.pause()
            playerMusic.music.unload()
            playerMusic.music.load(self.currentFile)
            self.currentPlaybackPos = self.fileDuration
            # do nothing
            print("Player waiting for action")
            print("Paused")
            return

        elif self.mode == "loop":
            playerMusic.music.pause()
            playerMusic.music.unload()
            self.currentPlaybackPos = 0.0
            playerMusic.music.load(self.currentFile)
            playerMusic.music.play()
            print("Playing in loop")
            return

        else:
            playerMusic.music.unload()
            playerMusic.music.pause()
            print("Player is stopped, waiting")
            return

    def playNext(self) -> None:
        # for later check if music was playing
        wasBusy = False

        if playerMusic.music.get_busy():
            wasBusy = True
            playerMusic.music.pause()
        playerMusic.music.unload()

        if self.currentIndex == self.maxIndex:
            self.currentIndex = 0
        else:
            self.currentIndex += 1

        self.updateBaseData()
        # player.load(self.playlist[self.currentIndex])
        playerMusic.music.load(self.currentFile)

        if wasBusy:
            if self.mode == "one loop":
                playerMusic.music.play(-1)
            elif self.mode != "one loop":
                playerMusic.music.play()

    def playPrevious(self) -> None:
        # for later check if music was playing
        wasBusy = False

        if playerMusic.music.get_pos() >= 10000:
            # if more than 10s just jump to previous
            playerMusic.music.rewind()
            self.currentPlaybackPos = 0.0
            return

        elif playerMusic.music.get_busy():
            wasBusy = True
            playerMusic.music.pause()
        playerMusic.music.unload()

        if self.currentIndex == 0:
            self.currentIndex = self.maxIndex
        else:
            self.currentIndex -= 1

        self.updateBaseData()

        # player.load(self.playlist[self.currentIndex])
        playerMusic.music.load(self.currentFile)

        if wasBusy:
            playerMusic.music.play()
        self.currentPlaybackPos = 0
        return

    def playPause(self) -> None:
        playerMusic.music.pause()
        # change button UI to play
        return

    def playUnPause(self) -> None:
        playerMusic.music.unpause()
        # change button UI to pause
        return

    def changeVolume(self, amount) -> bool:
        checkedAmount = 0.0

        if amount > 1.0:
            checkedAmount = 1.0
        elif amount < 0.0:
            checkedAmount = 0.0
        try:
            playerMusic.music.set_volume(checkedAmount)
        except:
            return False
        else:
            return True

    def changePos(self, pos):
        playerWasBusy = False
        if playerMusic.music.get_busy():
            playerWasBusy = True
            playerMusic.music.pause()

        playerMusic.music.rewind()
        playerMusic.music.set_pos(pos)
        self.currentPlaybackPos = pos
        if playerWasBusy:
            playerMusic.music.play()
        return

    def updateCurrentPlaybackPos(self):
        self.currentPlaybackPos = playerMusic.music.get_pos()
        return
    def changeMode(self):
        if self.mode == "auto":
            self.mode = "one loop"
            # change button icon

        elif self.mode == "one loop":
            self.mode = "loop"
            # change button icon

        elif self.mode == "loop":
            self.mode = "auto"
            # change button icon
        return
