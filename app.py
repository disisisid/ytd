import os
from flask import Flask, request, redirect
from pytube import YouTube
# from moviepy.editor import *
# import urllib.parse as urlparse

app = Flask(__name__)


@app.route('/music/')
def downloadVid():
  url = request.args.get("url")
  # url = 'https://www.youtube.com/watch?v=dRVjgd__AGk'
  print('pageUrl: ' + url)

  streams = YouTube(url).streams#.first().download()
  vidUrl = streams.first().url 
  print('vidUrl: ' + vidUrl)
  # return(vidUrl)
  return redirect(vidUrl)

@app.route('/create', methods=['POST'])
def take_note():
    return({})

if __name__ == "__main__": 
        app.run()


'''
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams
.filter(progressive=True, file_extension='mp4')
.order_by('resolution')
.desc()
.first()
'''


def convertmp42mp3(fileName):
  curr_path = os.getcwd()
  song_name = 'Time_To_Talk'
  video = VideoFileClip(os.path.join(curr_path, song_name + '.mp4'))
  video.audio.write_audiofile(os.path.join(curr_path, song_name + '.mp3'))


# url = 'https://www.youtube.com/watch?v=dRVjgd__AGk'
# downloadVid()