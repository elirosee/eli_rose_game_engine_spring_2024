# loop through a list

import pygame as pg

clock = pg.time.Clock()

frames = ["frame1", "frame2", "frame3", "frame4"]

# print(len(frames))

current_frame = 0

frames_length = len(frames)

current_frame += 1

print(current_frame%frames_length)

current_frame += 1

print(current_frame%frames_length)

current_frame += 1

print(current_frame%frames_length)

current_frame += 1

print(current_frame%frames_length)

# print (frames[frames_length])
# What will

