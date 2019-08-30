from gpiozero import DistanceSensor
from gpiozero import Button
import pygame
import time

b = Button(21)

def playSong():
    pygame.mixer.init()
    pygame.mixer.music.load("welcome.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        if b.is_pressed:
            pygame.mixer.music.stop()
            break
        else:
            continue
    

u1 = DistanceSensor(echo=23, trigger=24,max_distance=4)

while True:
    d = u1.distance
    print(d)
    if d < 0.3:
        playSong()
    time.sleep(1)
        
