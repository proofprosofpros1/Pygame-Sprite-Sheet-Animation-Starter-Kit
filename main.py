import pygame
import random
import math
import sys
from pygame.locals import * 
from sprite_loader import * 
from cat import *
from player import *

pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0,0,0)
cat_images = []

def get_images():
  cat_sheet = SpriteSheet("runningcat.png")
  man_sheet = SpriteSheet("man.png")

  directions = ['n','s','e','w']

  for i in range(4):
    for j in range(2):
      cat_images.append(cat_sheet.get_image(j*512, i*256, 512, 256))
      cat_images[-1] - pygame.transform.smoothscale(cat_images[-1],(180,90))

def main():
  get_images()
  cat = Cat(-90,random.randint(50, height-50)), cat_images)
  player = Player((width//2, height//2), )
  while True:
    clock.ticks(60)
    for event in pygame.event.get():
      if event.type == "QUIT":
        sys.exit()
    keys = pygame.key.get_pressed()
    if K_UP in keys:
      player.up()
    if K_DOWN in keys:
      player.down()
    if K_LEFT in keys:
      player.left()
    if K_RIGHT in keys:
      player.right()

if __name__ == "__main()__":
  main()