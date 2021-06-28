import os
from flask import Flask, request, redirect
from pytube import YouTube
#from werkzeug.utils import send_file
from flask import send_from_directory

app = Flask(__name__)

@app.route('/music')
def downloadMusic():
  url = request.args.get("url")
  print('pageUrl: ' + url)
  streams = YouTube(url).streams
  vidUrl = streams.first().url 
  print('vidUrl: ' + vidUrl)
  # return(vidUrl)
  return redirect(vidUrl)

@app.route('/audio')
def downloadAudio():
  url = request.args.get("url")
  print('pageUrl: ' + url)
  streams = YouTube(url).streams
  audio = streams.filter(only_audio=True).filter(file_extension='mp4').first()
  title = audio.title
  print('title: ' + title)
  audio.download('streams')
  return send_from_directory('streams', title + '.mp4')

@app.route('/video')
def downloadVid():
  url = request.args.get("url")
  print('pageUrl: ' + url)
  yt = YouTube(url)
  vidUrl = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().url
  print('vidUrl: ' + vidUrl)
  return redirect(vidUrl)  

if __name__ == "__main__": 
  app.run()
