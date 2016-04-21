import pygame

audio_to_play = '/home/pi/Documents/Python_projects/ChurchBells/AMAZING.WAV'
pygame.mixer.init()
pygame.mixer.music.load(audio_to_play)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
