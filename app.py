import os
from flask import Flask, request, redirect
from pytube import YouTube

app = Flask(__name__)

@app.route('/music')
def downloadMusic():
  url = request.args.get("url")
  print('pageUrl: ' + url)
  streams = YouTube(url).streams#.first().download()
  vidUrl = streams.first().url 
  print('vidUrl: ' + vidUrl)
  # return(vidUrl)
  return redirect(vidUrl)

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
