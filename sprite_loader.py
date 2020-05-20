import pygame

class SpriteSheet:
  def __init__(self, img_path):
    self.sprite_sheet = pygame.img.load(img_path)
  def get_image(self, x, y, width, height):
    image = pygame.Surface([width, height])
    image.blip(self.sprite_sheet, (0,0), (x,y,width,height))
    image.set_colorkey(image.get_at((0,0)))
    return image