#!/usr/bin/python

import sqlite3
import pygame
import datetime
import time
import os

#House keeping
sysday = time.strftime("%a")
syshour = time.strftime("%H")
    
#########################################################
#what music ?
conn = sqlite3.connect('/home/pi/Documents/Python_projects/Database/My_Python_SqliteDB')
query_build = 'select filename from audiofilelist where pk = ' + syshour
#cursor = conn.execute( query_build )
cursor = conn.execute( query_build )
#audio_filename = conn.fetchone()
#print audio_filename

#print row
#print "audio_filename " , row[0]

#cursor = conn.execute( query_build )
#print cursor
#cursor = conn.execute( "select date('now') " )
for row in cursor:
    #print row
    audio_filename = str(row)
    print audio_filename
conn.close()
##############################################################

#Lets start the music
#audio_to_play = '/home/pi/Documents/Python_projects/ChurchBells/AMAZING.WAV'
root_music_dir = '/home/pi/Documents/Python_projects/ChurchBells/'
audio_to_play = root_music_dir + audio_filename
pygame.mixer.init()
pygame.mixer.music.load(audio_to_play)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
