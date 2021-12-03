from pydub import AudioSegment
from pydub.playback import play
import fnmatch
import os


class Music:

    def __init__(self):
        self.Tracks = []
        self.Folders = []
        self.songsList = {}
        
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
        
    

    def play(self):
    
        val = 1
        for song in self.songsList.keys():
            print(val , ": ", song)
            val += 1
            
        Num = int(input("Enter the Song Number to play : "))
        songsName = list(self.songsList)
        
        sound = AudioSegment.from_file(self.songsList[songsName[Num-1]], format="mp3")
        play(sound)
    




music = Music()
music.play()
