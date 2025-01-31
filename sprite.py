#Hunter class
import pygame as pg
from pygame.locals import *
from pygame.math import Vector2
import Constants


class astroids(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.astroid_frames = []
        self.image = pg.image.load('graphics/Astroid_medium/a10000.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10001.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10002.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10003.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10004.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10005.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10006.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10007.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10008.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10009.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10010.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10011.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10012.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10013.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10014.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        self.image = pg.image.load('graphics/Astroid_medium/a10015.png').convert_alpha()
#        self.image = pg.transform.scale(self.image, (70, 50))
        self.astroid_frames.append(self.image)
        # A reference to the original image to preserve the quality.
        self.orig_image = self.image
        self.frame = 0
        self.rect = self.image.get_rect(center=position)
        self.pos = Vector2(position)
        self.vel = Vector2(Constants.BLOCK_SPEED)


    def update(self):      
        self.pos += self.vel
        self.rect = self.image.get_rect(center=self.pos)
        self.check_edges()
        if self.frame <= 14:
            self.image = self.astroid_frames[self.frame]
            self.frame = self.frame + 1
        else:            
            self.image = self.astroid_frames[self.frame]
            self.frame = 0

            
    def check_edges(self):        
        if self.pos.y >= Constants.SCREEN_HEIGHT - 25:
            self.vel *= -1
        elif self.pos.y <= 0 + 25:
            self.vel *= -1
            


#################################################################

class Player(pg.sprite.Sprite):
    def __init__(self, position, scr):
        super(Player, self).__init__()
        self.thrust_animation = False
        self.sprites = []
        self.current_sprite = 0
        self.star_count = 0
        self.screen = scr
        
        self.pos = Vector2(position)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.direction = Vector2(0, 0)
        self.angle = 0
       
        self.image = pg.image.load('graphics/centred_rocket.bmp').convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 30))
        self.sprites.append(self.image)
                
        self.image = self.sprites[self.current_sprite]
        self.temp_image = self.image
        self.rect = self.image.get_rect(center=position)

        
        
    def update(self):
        self.rotate()
        
        if self.thrust_animation == True:
            self.thruster()
        elif self.thrust_animation == False:
            self.temp_image = self.sprites[0]
        self.rotated_image = pg.transform.rotate(self.temp_image, self.angle)
        self.check_edges()
        
        self.vel += self.acc
        self.pos += self.vel
        self.acc = self.acc *0

        
    def check_edges(self):
        if self.pos.x > Constants.SCREEN_WIDTH:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = Constants.SCREEN_WIDTH
        
        if self.pos.y > Constants.SCREEN_HEIGHT:
            self.pos.y = 0
        elif self.pos.y < 0:
            self.pos.y = Constants.SCREEN_HEIGHT
 
 
    def thruster(self):
        self.acc = self.direction * Constants.THRUST_SPEED

    
    def rotate(self):
        self.direction = (pg.mouse.get_pos() - self.pos).normalize()
        radius, angle = self.direction.as_polar()
  
        self.rotated_image = pg.transform.rotate(self.temp_image, -angle)

        self.rect = self.rotated_image.get_rect(center = self.pos)
        self.image = self.rotated_image
       
        
##################################################################    

class Star(pg.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pg.image.load('graphics/star.bmp').convert_alpha()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.image = pg.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect(center=position)




        