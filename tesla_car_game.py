import pygame
import random
pygame.init()

win_wid = 600
win_hei= 500

win = pygame.display.set_mode((win_wid, win_hei))
pygame.display.set_caption('Tesla Car Game', 'Tesla AI Car Game automatic detect road')
clock = pygame.time.Clock()

#images
Tesla_image = pygame.image.load('Tesla1.png')
BackGround_image = pygame.image.load('Back_Ground.png')
road_lines_image = pygame.image.load('road_lines_image.png')
Gas_car_image = pygame.image.load ('Gas_car.png')
Gas_car_image2 = pygame.image.load('Gas_car2.png')
Gas_car_image3 = pygame.image.load('Gas_car3.png')
Gas_car_image4 = pygame.image.load('Gas_car4.png')



class tesla_car(object):
    def __init__(self, x, y, wid, hei):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.vel = 5    
        self.road_size = 50
        self.left = False
        self.right = False
        self.hitbox = (self.x + 12, self.y - 3, 70, 70)

    def draw(self, win):
        self.hitbox = (self.x + 12, self.y-20, 40, 65)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)
        return win.blit(Tesla_image, (self.x, self.y - 20))


class gas_car (object):
    def __init__(self, x, y, wid, hei, end ):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.end = end
        self.path = [self.y, self.end]
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 11, 50, 50)

    def draw(self, win):
        self.move()
        return win.blit(Gas_car_image, (self.x, self.y))

    def move(self):
        if self.vel > 0:
            if self.y + self.vel < self.path[1]:
                self.y += self.vel
            else:
                self.y = -300
        self.hitbox = (self.x + 12, self.y -3, 40, 70)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def hit(self):
        print('Hit!')

class gas_car2 (object):
    def __init__(self, x, y, wid, hei, end ):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.end = end
        self.path = [self.y, self.end]
        self.vel = 3
        self.hitbox = (self.x + 12, self.y - 3, 40, 70)

    def draw(self, win):
        self.move()
        return win.blit(Gas_car_image2, (self.x, self.y))

    def move(self):
        if self.vel > 0:
            if self.y + self.vel < self.path[1]:
                self.y += self.vel
            else:
                self.y = -300
        self.hitbox = (self.x + 12, self.y - 3, 40, 70)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def hit(self):
        print('Hit!')

class gas_car3 (object):
    def __init__(self, x, y, wid, hei, end ):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.end = end
        self.path = [self.y, self.end]
        self.vel = 3
        self.hitbox = (self.x + 12, self.y - 3, 40, 70)

    def draw(self, win):
        self.move()
        return win.blit(Gas_car_image3, (self.x, self.y))

    def move(self):
        if self.vel > 0:
            if self.y + self.vel < self.path[1]:
                self.y += self.vel
            else:
                self.y = -300
        self.hitbox = (self.x + 12, self.y - 3, 40, 70)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)

    def hit(self):
        print('Hit!')

class gas_car4 (object):
    def __init__(self, x, y, wid, hei, end ):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.end = end
        self.path = [self.y, self.end]
        self.vel = 3
        self.hitbox = (self.x + 12, self.y - 3, 40, 70)

    def draw(self, win):
        self.move()
        return win.blit(Gas_car_image4, (self.x, self.y))

    def move(self):
        if self.vel > 0:
            if self.y + self.vel < self.path[1]:
                self.y += self.vel
            else:
                self.y = -300
        self.hitbox = (self.x + 12, self.y - 3, 40, 70)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 1)
    def hit(self):
        print('Hit!')

class road_lines (object):
    def __init__(self, x, y, wid, hei, end ):
        self.x = x
        self.y = y
        self.wid = wid
        self.hei = hei
        self.end = end
        self.path = [self.y, self.end]
        self.vel = 6

    def draw(self, win):
        self.move()
        return win.blit(road_lines_image, (self.x, self.y))

    def move(self):
        if self.vel > 0:
            if self.y + self.vel < self.path[1]:
                self.y += self.vel
            else:
                self.y = -300


#draw function
def DrawInGame():
    win.blit(BackGround_image, (0, 0))
    road.draw(win)
    road2.draw(win)
    road3.draw(win)
    road4.draw(win)
    gas.draw(win)
    gas2.draw(win)
    gas3.draw(win)
    gas4.draw(win)
    tesla.draw(win)

    pygame.display.update()



#mainloop For Tesla
tesla = tesla_car(win_wid*0.45, 450, 64, 64)
road = road_lines(win_wid*0.45, win_hei*1, 10, 30, 600)
road2 = road_lines(win_wid*0.45, win_hei*0.5, 10, 30, 600)
road3 = road_lines(win_wid*0.45, win_hei*0.01, 10, 30, 600)
road4 = road_lines(win_wid*0.45, win_hei*0.005, 10, 30, 600)
gas = gas_car (random.randint(55, 475), -300, 64, 64, 600)
gas2 = gas_car2(random.randint(100, 475), -600, 64, 64, 600)
gas3 = gas_car3(random.randint(55, 200), -800, 64, 64, 600)
gas4 = gas_car4(random.randint(300, 475), -1000, 64, 64, 600)
run = True
while run:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if gas.y > 500:
        gas = gas_car (random.randint(55, 475), random.randint(-500, -300 ), 64, 64, 600)
    gas.move()

    if gas2.y > 500:
        gas2 = gas_car2(random.randint(100, 475), random.randint(-450, -400), 64, 64, 600)
    gas2.move()

    if gas3.y > 500:
        gas3 = gas_car3(random.randint(100, 475), random.randint(-600,-300), 64, 64, 600)
    gas3.move()

    if gas4.y > 500:
        gas4 = gas_car4(random.randint(100, 475), random.randint(-600, -400), 64, 64, 600)
    gas4.move()

    if tesla.hitbox[1] - tesla.hitbox[3] < gas.hitbox[1] + gas.hitbox[3] and tesla.hitbox[1] + tesla.hitbox[3] > gas.hitbox[1]:
        if tesla.hitbox[0] + tesla.hitbox[2] > gas.hitbox[0] and tesla.hitbox[0] - tesla.hitbox[2] < gas.hitbox[0] + gas.hitbox[2]:
            gas.hit()
    if tesla.hitbox[1] - tesla.hitbox[3] < gas2.hitbox[1] + gas2.hitbox[3] and tesla.hitbox[1] + tesla.hitbox[3] > gas2.hitbox[1]:
        if tesla.hitbox[0] + tesla.hitbox[2] > gas2.hitbox[0] and tesla.hitbox[0] - tesla.hitbox[2] < gas2.hitbox[0] + gas2.hitbox[2]:
            gas2.hit()
    if tesla.hitbox[1] - tesla.hitbox[3] < gas3.hitbox[1] + gas3.hitbox[3] and tesla.hitbox[1] + tesla.hitbox[3] > gas3.hitbox[1]:
        if tesla.hitbox[0] + tesla.hitbox[2] > gas3.hitbox[0] and tesla.hitbox[0] - tesla.hitbox[2] < gas3.hitbox[0] + gas3.hitbox[2]:
            gas3.hit()
    if tesla.hitbox[1] - tesla.hitbox[3] < gas4.hitbox[1] + gas4.hitbox[3] and tesla.hitbox[1] + tesla.hitbox[3] > gas4.hitbox[1]:
        if tesla.hitbox[0] + tesla.hitbox[2] > gas4.hitbox[0] and tesla.hitbox[0] - tesla.hitbox[2] < gas4.hitbox[0] + gas4.hitbox[2]:
            gas4.hit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and tesla.x > tesla.vel + tesla.road_size:
        tesla.x -= tesla.vel
    if keys[pygame.K_RIGHT] and tesla.x < win_wid - tesla.wid - tesla.road_size - tesla.vel:
        tesla.x += tesla.vel

    DrawInGame()

pygame.quit()
