import pygame as pg

pg.init()

#screen
h = 500
w = 500
screen = pg.display.set_mode((w,h))

#title of the window
pg.display.set_caption('Day 3 Challenge')

#button 
image = pg.image.load('easy.png').convert_alpha()
class Button():
	def __init__(self, x, y, i, s):
		w = i.get_width()
		h = i.get_height()
		self.image = pg.transform.scale(i, (int(w * s), int(h * s)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		pos = pg.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pg.mouse.get_pressed()[0] == 0:
			self.clicked = False

		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
		pos = pg.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pg.mouse.get_pressed()[0] == 0:
			self.clicked = False

		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

#music
music = 'that_was_easy.ogg'
pg.mixer.init()
pg.mixer.music.load(music)

#background image
back = pg.image.load('back.jpg').convert_alpha()
back = pg.transform.scale(back, (int(500), int(500)))
back_light = pg.image.load('back_light.jpg').convert_alpha()
back_light = pg.transform.scale(back, (int(500), int(500)))
back_dark = pg.image.load('back_dark.jpg').convert_alpha()
back_dark = pg.transform.scale(back, (int(500), int(500)))

#explosion effect
clock = pg.time.Clock()
fps = 60

class Explosion(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        i1 = pg.image.load('exp1.png')
        i2 = pg.image.load('exp2.png')
        i3 = pg.image.load('exp3.png')
        i4 = pg.image.load('exp4.png')
        i5 = pg.image.load('exp5.png')
        self.images.append(pg.transform.scale(i1, (100, 100)))
        self.images.append(pg.transform.scale(i2, (100, 100)))
        self.images.append(pg.transform.scale(i3, (100, 100)))
        self.images.append(pg.transform.scale(i4, (100, 100)))
        self.images.append(pg.transform.scale(i5, (100, 100)))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0
        
    def update(self):
        explosion_speed = 4
        self.counter += 1
        
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
            
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()
            
explosion = pg.sprite.Group()

button = Button(100, 100, image, 1)

run = True
while run:
    clock.tick(fps)
    screen.fill([255, 255, 255])
    screen.blit(back, [0,0])
    
    if button.draw(screen):
        pg.mixer.music.play()
        screen.blit(back_dark, [0,0])
        screen.blit(back_light, [0,0])
        
    explosion.draw(screen)
    explosion.update()
    pos = pg.mouse.get_pos()
    explosion_new = Explosion(pos[0], pos[1])
    explosion.add(explosion_new)
           
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()