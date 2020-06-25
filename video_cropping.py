import os

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_extract_audio
import moviepy.editor as mp


import glob

start_time = 55
end_time = 75

# def get_all_videos():
#     print(glob.glob("/*.txt"))

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
def get_files_list():
    files_list = list()
    for r, d, f in os.walk(thisdir):
        for file in f:
            if file.endswith(".avi"):
                path = os.path.join(r, file)
                print(os.path.join(r, file))
                files_list.append(path)
    return files_list

def find_video_name(path):
    file_split = file.split("\\")
    file_name = file_split[-1]
    return file_name

def crop_file(file):
    file_name = find_video_name(file)
    dur = find_dur(file_name)
    file_name_cropped = "crop_" + file_name
    file_name_audio = file_name.split('.')
    file_audio_ext = file_name_audio[:len(file_name_audio) - 1]
    out_str = "".join(file_audio_ext) + ".wav"

    ffmpeg_extract_subclip(file_name, dur - 60, dur, targetname=file_name_cropped)
    ffmpeg_extract_audio(file_name_cropped, out_str)
    print("cropped")

def find_dur(file):
    duration = mp.VideoFileClip(file).duration
    return duration

list_f = get_files_list()
for file in list_f:
    crop_file(file)

print('end')

#ffmpeg_extract_subclip("Variables.mp4", start_time, end_time, targetname="test.mp4")

