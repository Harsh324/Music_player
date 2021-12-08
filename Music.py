from logging import NOTSET
import multiprocessing
from typing import MutableMapping

from pydub import AudioSegment
from pydub.playback import play
import fnmatch
import os

from threading import Thread
import multiprocessing as mp
import psutil

class Music:

    def __init__(self):
        self.Tracks = []
        self.Folders = []
        self.songsList = {}

        self.MusicControl = None
        self.SongID = None
        self.songName = None

        self.songLoop = False
        self.playlistLoopFlag = False

        self.__get_songs()
        self.__setList()
        

    def __get_songs(self, Path = '/', Format = '*.mp3'):
        
        try :
            cacheFile = open("Cache.txt", 'x')
        except : 
            return
        
        for root, dirs, files in os.walk(Path):
            for filename in fnmatch.filter(files, Format):
                self.Folders.append(os.path.join(root))
                self.Tracks.append(os.path.join(filename))
                Source = os.path.join(root , filename)
               
                cacheFile.write(filename + ":*:")
                cacheFile.write(Source)
                cacheFile.write('\n')     
        cacheFile.close()

    
    def __setList(self):
        self.__get_songs()
        cacheFile = open("Cache.txt", 'r')
        
        for line in cacheFile:
            name, path = line.split(":*:")
            self.songsList[name] = path[:-1]
        
    
    def selectSong(self):
        val = 1
        print("Select the song among the songs from the List below ")
        print()
        for song in self.songsList.keys():
            print(val , ": ", song)
            val += 1
        Num = int(input("Enter the Song Number to play : "))
        songsName = list(self.songsList)
        
        self.songName = self.songsList[songsName[Num-1]]
        self.play()
        
    
    def play(self):
        sound = AudioSegment.from_file(self.songName, format="mp3")
        
        p1 = mp.Process(target=play, args=(sound,))
        p1.start()
        self.SongID = p1.pid    
        
        if False == self.songLoop:
            self.menu()
 

    def __pausePlay(self):
        process = psutil.Process(self.SongID)

        # while(process.status() != psutil.STATUS_ZOMBIE):
        if self.MusicControl == 1 and process.status() == psutil.STATUS_SLEEPING:
            """
            Halt the execution of play
            """
            process.suspend()
            # print(process.status())

        elif self.MusicControl == 1 and process.status() == psutil.STATUS_STOPPED:
            """
            Resume the execution of play
            """
            process.resume()
            # print(process.status())


    def menu(self):
        while self.SongID != psutil.STATUS_ZOMBIE:
            self.MusicControl = int(
                input("  (1 : pause/play)\n  (2 : loopSong)\n  "
                      "(3 : loopPlaylist)\n  (4 : loopAB)\n  "
                      "(5 : seek)\n  (6 : stop)\n"))

            if 1 == self.MusicControl:
                self.__pausePlay()

            elif 2 == self.MusicControl:
                self.songLoop = True
                
                while True == self.songLoop:
                    self.play()

            elif 3 == self.MusicControl:
                pass

            elif 4 == self.MusicControl:
                pass

            elif 5 == self.MusicControl:
                self.seek()

            elif 6 == self.MusicControl:
                self.stop()


    def seek(self):
        psutil.Process(self.SongID).kill()
        seekValue = int(input("\nEnter the starting position in seconds : "))

        sound = AudioSegment.from_file(self.songName, format="mp3", start_second=seekValue)
        
        p1 = mp.Process(target=play, args=(sound,))
        p1.start()
        self.SongID = p1.pid


    def stop(self):
        psutil.Process(self.SongID).kill()
        self.SongID = None
        self.songName = None
        self.selectSong()
            

    def loopSong(self):
        p1 = psutil.Process(self.SongID)
        
        


if __name__ == "__main__":
    music = Music()
    music.selectSong()
