#create a Maze game!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,p_image,p_x,p_y,p_speed):
        super().__init__()

        self.image=transform.scale(image.load(p_image),(50,50))
        self.speed=p_speed
        self.rect=self.image.get_rect()
        self.rect.x=p_x
        self.rect.y=p_y

    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x-=self.speed
        if keys[K_RIGHT] and self.rect.x<width-80:
            self.rect.x+=self.speed
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_DOWN] and self.rect.y<width-80:
            self.rect.y+=self.speed
        

class Enemy(GameSprite):
    direction ='left'
    def update(self):
        if self.rect.x<=470:
            self.direction='right'
        if self.rect.x>width-85:
            self.direction='left'

        if self.direction=='left':
            self.rect.x-=self.speed
        else:
            self.rect.x+=self.speed

class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,wall_X,wall_y,wall_width,wall_height):
        super().__init__()
        self.color1=color1
        self.color2=color2
        self.color3=color3
        self.wall_X=wall_X
        self.wall_y=wall_y
        self.width=wall_width
        self.height=wall_height

        self.image=Surface((self.width,self.height))        
        self.image.fill((color1,color2,color3))
        self.rect=self.image.get_rect()
        self.rect.x=wall_X
        self.rect.y=wall_y

    def draw_wall(self):
        win.blit(self.image,(self.rect.x,self.rect.y))



width=700
height=500

win=display.set_mode((width,height))
display.set_caption('Maze')
background=transform.scale(image.load('background.jpg'),(width,height))

personazhi=Player('Hero.png',50,420,4)
enemy=Enemy('cyborg.png',630,260,4)
final=GameSprite('treasure.png',570,400,0)

w1=Wall(78,195,5,100,15,400,10)
w2=Wall(78,195,5,100,15,10,380)
w3=Wall(78,195,5,275,15,10,340)
w4=Wall(78,195,5,120,485,340,10)
w5=Wall(78,195,5,190,150,10,340)
w6=Wall(78,195,5,450,150,10,340)
w7=Wall(78,195,5,405,150,100,10)



game=True
clock=time.Clock()
FPS=60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick=mixer.Sound('kick.ogg')
money=mixer.Sound('money.ogg')
font.init()
font=font.SysFont("Arial",70)
lose=font.render('YOU LOSE!',True,(255,0,0))
winn=font.render("YOU WIN",True,(0,255,0))
finish=False
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if finish != True:
        win.blit(background,(0,0))
        personazhi.update()
        enemy.update()

        personazhi.reset()
        enemy.reset()
        final.reset()
        
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

        if sprite.collide_rect(personazhi,enemy) or sprite.collide_rect(personazhi,w1) or sprite.collide_rect(personazhi,w2) or sprite.collide_rect(personazhi,w2) or sprite.collide_rect(personazhi,w3) or sprite.collide_rect(personazhi,w4) or sprite.collide_rect(personazhi,w5) or sprite.collide_rect(personazhi,w6) or sprite.collide_rect(personazhi,w7):
            finish=True
            win.blit(lose,(200,200))
            kick.play()
        if sprite.collide_rect(personazhi,final):
            finish=True
            win.blit(winn,(200,200))
            money.play()
    display.update()
    clock.tick(FPS)