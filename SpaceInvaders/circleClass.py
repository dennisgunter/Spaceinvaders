import sys, pygame, random

class Circle(object):
    def __init__(self,color,position,radius):
        self.box = [position[0],position[1],radius[0],radius[1]] # Liste mit Position, Laenge und Breite
        self.color = color
        self.screen = pygame.display.get_surface() #Legt die Oberfläche fest, auf die gezeichnet wird
        #pygame.draw.rect(self.screen, self.color, self.box, 0) #Zeichnet das Objekt in der Initialisierung
        self.bildVariable =  pygame.image.load("shuttle.png")

    # Update Methode, die das Objekt an seine aktuelle Position mit seinen aktuellen Eigenschaften zeichnet
    def update(self):
        pass
        #pygame.draw.rect(self.screen, self.color, self.box, 0)

    def move(self,x,y):
        self.box[0] += x
        self.box[1] += y

    def touch(self,enemy):
        if self.box[1] < enemy.box[1] < self.box[1] + self.box[3] and self.box[0] < enemy.box[0] < self.box[0] + self.box[2]:
            return True
        return False
