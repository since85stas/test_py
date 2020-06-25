from os import path
import speech_recognition as sr
from pydub import AudioSegment
import pydub

pydub.AudioSegment.converter = "c:\\work\\python\\video_dir\\ffmpeg-20200623-ce297b4-win64-static\\bin\\ffmpeg.exe"

def textRecogn(file):
    r = sr.Recognizer()
    AudioSegment.ffmpeg = "c:\\work\\python\\video_dir\\ffmpeg-20200623-ce297b4-win64-static\\bin\\ffmpeg.exee"
    with sr.AudioFile("audio.wav") as source:
        audio = r.record(source)
    command = r.recognize_google(audio, language= "Ru")
    print (command)

def mp3_transform():
    # files
    src = "c:\\work\\python\\video_dir\\audio.mp3"
    dst = "audio.wav"

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

textRecogn()