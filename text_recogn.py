import os
import speech_recognition as sr
from pydub import AudioSegment
import pydub

# Getting the current work directory (cwd)
thisdir = os.getcwd()

pydub.AudioSegment.converter = "c:\\work\\python\\video_dir\\ffmpeg-20200623-ce297b4-win64-static\\bin\\ffmpeg.exe"

def textRecogn(file):
    r = sr.Recognizer()
    AudioSegment.ffmpeg = "c:\\work\\python\\video_dir\\ffmpeg-20200623-ce297b4-win64-static\\bin\\ffmpeg.exee"
    with sr.AudioFile(file) as source:
        audio = r.record(source)
    command = r.recognize_google(audio, language= "Ru")
    print (command)
    return command

def mp3_transform():
    # files
    src = "c:\\work\\python\\video_dir\\audio.mp3"
    dst = "audio.wav"

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

# r=root, d=directories, f = files
def get_files_list():
    files_list = list()
    for r, d, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".wav"):
                path = os.path.join(r, file)
                print(os.path.join(r, file))
                files_list.append(path)
    return files_list

txt_file = get_files_list()

txt_list = list()

for f in txt_file:
    txt_list.append(textRecogn(f))

with open('data.txt', 'w') as f:
    for txt in txt_list:
        f.write(txt)
        f.write("\n")
        f.write("\n")

print("")