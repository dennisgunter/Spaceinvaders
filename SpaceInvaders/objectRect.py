import sys, pygame, random

class FlyingBox(object):
    def __init__(self,color,position,rect, speed):
        self.box = [position[0],position[1],rect[0],rect[1]] #Box Attribut mit [xPos,yPos,Laenge,Breite]
        self.color = color
        self.speed = speed
        self.screen = pygame.display.get_surface()
        self.bildVariable = pygame.image.load("Invader.png")
        #pygame.draw.rect(self.screen, self.color, self.box, 0) #Zeichnet anhand der Color und des Box-Attributs

    #bewegt das FlyingObject und zeichnet es neu
    def update(self):
        self.move()
        #pygame.draw.rect(self.screen, self.color, self.box, 0)

    #Bewegung des Objektes
    def move(self):
        self.box[0] = self.box[0] + self.speed
        if self.box[0] > 700-self.box[2]:
            self.speed = (self.speed *-1) -1
            self.box[1] += 50
        if self.box[0] < 0:
            self.speed = (self.speed *-1) +1
            self.box[1] += 50

    def changeSpeed(self,speed):
        self.speed[0] = self.speed[0] + speed

    def randomPosition(self):
        self.box[0] = random.randint(0,700)
        self.box[1] = random.randint(100,550)
        
    def touch(self,enemy):
        if self.box[1] < enemy.box[1] < self.box[1] + self.box[3] and self.box[0] < enemy.box[0] < self.box[0] + self.box[2]:
            return True
        return False

class Green(FlyingBox):
    def changeBild(self):
        self.bildVariable = pygame.image.load("InvaderGreen.png")
        self.clock = 0

class Yellow(FlyingBox):
    def changeBild(self):
        self.bildVariable = pygame.image.load("invaderYellow.png")

class Red(FlyingBox):
    def changeBild(self):
        self.bildVariable = pygame.image.load("invaderRed.png")

class Friend(FlyingBox):
    def changeBild(self):
        self.bildVariable = pygame.image.load("friendlyRight.png")
        self.other = pygame.image.load("friendlyLeft.png")
        
    def move(self):
        self.box[0] = self.box[0] + self.speed
        if self.box[0] > 700-self.box[2]:
            self.speed = (self.speed *-1) -1
            self.box[1] += 50
            hif = self.bildVariable
            self.bildVariable = self.other
            self.other = hif 
        if self.box[0] < 0:
            self.speed = (self.speed *-1) +1
            self.box[1] += 50
            hif = self.bildVariable
            self.bildVariable = self.other
            self.other = hif 

class Boom(object):
    def __init__(self,x,y):
        self.dieEins = pygame.image.load("dieEins.png")
        self.dieZwei = pygame.image.load("dieZwei.png")
        self.box = [x, y]
        self.timer = 0

    def change(self):
        self.dieZwei = self.dieEins
        
        
        
class Schuesse(object):
    def __init__(self,color,position,rect,speed):
        self.box = [position[0],position[1],rect[0],rect[1]] #Box Attribut mit [xPos,yPos,Laenge,Breite]
        self.color = color
        self.speed = speed
        self.screen = pygame.display.get_surface()
        pygame.draw.rect(self.screen, self.color, self.box, 0)

    def update(self):
        self.move()
        pygame.draw.rect(self.screen, self.color, self.box, 0)

    def move(self):
        self.box [1] -= self.speed

    def touch(self,enemy):
        if self.box[1] < enemy.box[1] < self.box[1] + self.box[3] and self.box[0] < enemy.box[0] < self.box[0] + self.box[2]:
            return True
        return False

class Score(object):
    def __init__(self,text,color,x,y):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = text
        self.color = color
        self.box = [x,y]
        self.textsurface = self.myfont.render(self.text, False, self.color)
        
    def update(self):
        self.textsurface = self.myfont.render(self.text, False, self.color)

    def change(self,newtext):
        self.text = newtext

class Lives(object):
    def __init__(self,x,y):
        self.box = [x,y]
        self.bildVariable = pygame.image.load("Herz.png")

