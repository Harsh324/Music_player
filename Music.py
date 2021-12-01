from pydub import AudioSegment
from pydub.playback import play
import fnmatch
import os
import shutil
from pygame import mixer
import dbus


class Music:

    def __init__(self):
        self.Tracks = []
        self.Folders = []


    def __getsongs__(self):

        Current = os.getcwd()
        New = os.path.join(Current , r'Songs')
        if not os.path.exists(New):
            os.makedirs(New)

        Path , Format = '/' , '*.mp3'
        #Tracks , Folders = [],[]
        for root, dirs, files in os.walk(Path):
            for filename in fnmatch.filter(files, Format):
                self.Folders.append(os.path.join(root))
                self.Tracks.append(os.path.join(filename))
                Source = os.path.join(root , filename)
                try:
                    shutil.copy(Source , New)
                except shutil.SameFileError:
                    continue

        #print(os.path.join(root, filename))
        #return self.Tracks , self.Folders
    

    def __play__(self):
        Val = 1
        song = os.listdir(r'Songs')
        for file in song:
            print(Val , ": ",file)
            Val +=1
        Num = int(input("Enter the Song Number to play : "))
        Song = os.path.join(r'Songs' , song[Num-1])
        #print(Song)
        sound = AudioSegment.from_file(Song, format="mp3")
        play(sound)
    




music = Music()
#music.__getsongs__()
music.__play__()
music.__pause__()
'''
#for i in range(len(Tracks)):
#    print(i+1 , ": " , Tracks[i])
Root = '/'
Format = '*.mp3'
Tracks , Folders = [],[]
for root, dirs, files in os.walk(Root):
    for filename in fnmatch.filter(files, Format):
        #folder = os.path.join(root)
        #track = os.path.join(root, filename)
        Folders.append(os.path.join(root))
        Tracks.append(os.path.join(filename))'
for i in range(len(Song)):
    print(i+1 , ": " , Song[i])
#sound = AudioSegment.from_file("07 Channa Mereya - Arijit Singh 320Kbps.mp3", format="mp3")
#play(sound)'''
