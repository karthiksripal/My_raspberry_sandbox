#!usr/bin/env python
#coding=utf-8

import pygame
import pyaudio
import wave


#define stream chunk
chunk = 512*15

# open a wav format music
f = wave.open(r"/home/pi/Downloads/ChurchBells/1000BLES.WAV","rb")
#instantiate pyaudio
p = pyaudio.PyAudio()

#open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate =f.getframerate(),
                output = True)

#read data
data = f.readframes(chunk)

#play stream
while data !='':
    stream.write(data)
    data = f.readframes(chunk)

#stop stream
stream.stop_stream()
stream.close()

#close pyaudio
p.terminate()
