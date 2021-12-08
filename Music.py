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
        for song in self.songsList.keys():
            print(val , ": ", song)
            val += 1
            
        Num = int(input("Enter the Song Number to play : "))
        songsName = list(self.songsList)
        
        self.play(self.songsList[songsName[Num-1]])
        
    
    def play(self, song):
        sound = AudioSegment.from_file(song, format="mp3")
        
        p1 = mp.Process(target=play, args=(sound,))
        p1.start()
        self.SongID = p1.pid
        self.pause()        


    def pause(self):
        process = psutil.Process(self.SongID)
        
        while(process.status() != psutil.STATUS_ZOMBIE):
            
            self.MusicControl = int(input("\nEnter 1 to pause playback "))
            if(self.MusicControl == 1):
                """
                Halt the execution of play
                """
                process.suspend()
                # print(process.status())

            self.MusicControl = int(input("\nEnter 1 to resume playback "))
            if(self.MusicControl == 1):
                """
                Resume the execution of play
                """
                process.resume()
                # print(process.status())
            
        


music = Music()
music.selectSong()
