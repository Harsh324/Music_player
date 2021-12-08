import audioplayer
from pydub import AudioSegment
from pydub.playback import play
import fnmatch
import os
from audioplayer import AudioPlayer

class Music:

    def __init__(self):
        self.Tracks = []
        self.Folders = []
        self.songsList = {}
        self.__Audio = None
        self.__filename = None
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
        
    def __get_filename(self):
        val = 1
        print("Select the song among the songs from the List below ")
        print()
        for song in self.songsList.keys():
            print(val , ": ", song)
            val += 1
        Num = int(input("Enter the Song Number to play : "))
        songsName = list(self.songsList)
        self.__filename = self.songsList[songsName[Num-1]]
        return self.__filename


    def __play(self):
        
        #sound = AudioSegment.from_file(self.songsList[songsName[Num-1]], format="mp3")
        #play(sound)
        self.__Audio = AudioPlayer(self.__get_filename())
        self.__Audio.play()
        #return self.__Audio


    def __Pause(self):
        self.__Audio.pause()
        print("Audio is paused")
        #return self.__Audio


    def __Resume(self):
        self.__Audio.resume()
        print("Audio is resumed")
        #return self.__Audio
    

    def __Stop(self):
        self.__Audio.stop()
        print("Audio is stopped")
        #return self.__Audio


    def __Close(self):
        self.__Audio.close()
        print("Audio player is closed , Thank you")
    

    def Drive(self):
        self.__play()
        Num = int(input("Enter 1 to pause Audio : "))
        if(Num == 1):
            self.__Pause()
        Num = int(input("Enter 2 to resume Audio : "))
        if(Num == 2):
            self.__Resume()
        Num = int(input("Enter 3 to stop Audio : "))
        if(Num == 3):
            self.__Stop()
        Num = int(input("Enter 4 to close the Audio player : "))
        if(Num == 4):
            self.__Close()




music = Music()
music.Drive()
