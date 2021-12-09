from logging import NOTSET
import multiprocessing
from typing import MutableMapping

from pydub import AudioSegment
from pydub.playback import play
import fnmatch
import os
import time 

from threading import Thread
import multiprocessing as mp
import psutil

class Music:

    def __init__(self):
        self.Tracks = []
        self.Folders = []
        self.songsList = {}
        self.__time = 0
        self.MusicControl = None
        self.SongID = None
        self.songName = None

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
        
    def __timer(self):
        while self.SongID != psutil.STATUS_ZOMBIE:
            mins, secs = divmod(self.__time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            self.__time += 1



    def selectSong(self):
        val = 1
        print("Select the song among the songs from the List below ")
        print()
        for song in self.songsList.keys():
            print(val , ": ", song)
            val += 1
        Num = int(input("\nEnter the Song Number to play : "))
        print()
        songsName = list(self.songsList)
        
        self.songName = self.songsList[songsName[Num-1]]
        self.play(self.songsList[songsName[Num-1]])
        
    
    def play(self, song):
        sound = AudioSegment.from_file(song, format="mp3")
        
        p1 = mp.Process(target=play, args=(sound,))
        p1.start()
        self.SongID = p1.pid
        print("Currently Playing : ",os.path.basename(self.songName))
        print()
        #P2 = mp.Process(targest = self.__timer())
        #P2.start()
        #P3 = mp.Process(target = self.menu())
        #P3.start()
        self.menu()        


    def __pausePlay(self):
        process = psutil.Process(self.SongID)
        #process1 = psutil.Process(self.__timer())
        # while(process.status() != psutil.STATUS_ZOMBIE):
        if self.MusicControl == 1 and process.status() == psutil.STATUS_SLEEPING:
            """
            Halt the execution of play
            """
            #process1.suspend()
            process.suspend()
            # print(process.status())

        elif self.MusicControl == 1 and process.status() == psutil.STATUS_STOPPED:
            """
            Resume the execution of play
            """
            process.resume()
            #process1.resume()
            # print(process.status())


    def menu(self):
        while self.SongID != psutil.STATUS_ZOMBIE:
            #self.__timer()
            print("Enter command : ")
            self.MusicControl = int(
                input(" (1 : pause/play), (2 : loopSong), "
                      "(3 : loopPlaylist), (4 : loopAB), "
                      "(5 : seek), (6 : stop) : "))

            if 1 == self.MusicControl:
                self.__pausePlay()

            elif 2 == self.MusicControl:
                pass

            elif 3 == self.MusicControl:
                pass

            elif 4 == self.MusicControl:
                pass

            elif 5 == self.MusicControl:
                self.seek()

            elif 6 == self.MusicControl:
                self.stop()


    def seek(self):
        seekValue = int(input("\nEnter the starting position in seconds : "))
        psutil.Process(self.SongID).kill()
        sound = AudioSegment.from_file(self.songName, format="mp3", start_second=seekValue)
        
        p1 = mp.Process(target=play, args=(sound,))
        p1.start()
        self.SongID = p1.pid


    def stop(self):
        psutil.Process(self.SongID).kill()
        self.SongID = None
        self.songName = None
        self.selectSong()
            



if __name__ == "__main__":
    music = Music()
    music.selectSong()
