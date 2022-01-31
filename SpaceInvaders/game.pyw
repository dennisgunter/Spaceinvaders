#!/usr/bin/env python3

import sys, pygame, objectRect, circleClass, random, time
pygame.init()

clock = pygame.time.Clock()
size = width, height = 700, 700     #bildschimgroesse
black = (0, 0, 0)                   #definition der farben
blue = (0,0, 255)                   #definition der farben
red = (255,0,0)                     #definition der farben
white = (255,255,255)
green = (0,255,0)
transparent = (0, 0, 0, 0)

def initialize ():
    global aufladen, boom, friendlist, new,yellowlist, allEnemies, leben, textscore, screen, greenInvaders, greenlist, lebensliste, abschussliste, flyingObjects, score, kreis, keys
    aufladen = 0                        #zum schuesse aufladen (alle 15 tiks)
    new = 0
    allEnemies = 0
    leben = 3                           #wie viele leben man am anfang hat
    textscore = 0
    screen = pygame.display.set_mode(size)
    greenInvaders = []
    greenlist = []
    yellowlist = []
    friendlist =  []

    lebensliste = []
    abschussliste = []                  #eine liste aller schuesse
    flyingObjects =  []                 #eine liste aller enemies
    boom = []
    for i in range (10):                #erstellen von 10 startenemies
        type = random.randint(0,99)
        if 9 >= type >= 0:
            flyingObjects.append(objectRect.Green(black,[70+50*i,50],(27,22),2))
            greenInvaders.append(flyingObjects[-1])
            greenInvaders[-1].changeBild()

        elif 19 >= type >= 10:
            flyingObjects.append(objectRect.Yellow(black,[70+50*i,50],(27,22),2))
            flyingObjects[-1].changeBild()
            yellowlist.append(flyingObjects[-1])

        elif 21 >= type >= 20:
            flyingObjects.append(objectRect.Friend(black,[70+50*i,50],(27,22),2))
            flyingObjects[-1].changeBild()
            friendlist.append(flyingObjects[-1])
            
            
        else:
            flyingObjects.append(objectRect.FlyingBox(black,[70+50*i,50],(27,22),2))

    for i in range(3):
        lebensliste.append(objectRect.Lives(10+40*i,10))
    kreis = circleClass.Circle(transparent, [320, 630], [40,40]) #erstellen des spielers
    score = objectRect.Score("0",white,500,50)
    game()

def deathscreen ():
    global aufladen, boom, friendlist, new,yellowlist, allEnemies, leben, textscore, screen, greenInvaders, greenlist, lebensliste, abschussliste, flyingObjects, score, kreis, keys
    screen.fill((0,0,0))
    screen.blit(pygame.font.SysFont('Comic Sans MS', 60).render("Game Over", False, red),(200,200))
    screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render("Dein Score ist: " + str(textscore), False, white),(225,300))
    pygame.display.flip()
    while True:
        #handles the shutting down of the programm
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            break
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
    initialize()

def game ():
    global aufladen, boom, friendlist, new, allEnemies, leben, textscore, screen, greenInvaders,yellowlist, greenlist, lebensliste, abschussliste, flyingObjects, score, kreis, keys
    bg = pygame.image.load("bg2.png")
    while True:
        #handles the shutting down of the programm
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed() #gets the pressed keys
        #movement handling
        if keys[pygame.K_LEFT]:
            if kreis.box[0] >= 0:
                kreis.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            if kreis.box[0] + kreis.box[2] <= width:
                kreis.move(5, 0)
        if keys[pygame.K_UP]:
            if aufladen >= 22:
                abschussliste.append(objectRect.Schuesse(red,[kreis.box[0]+(kreis.box[2]/2),kreis.box [1]],(2,10),7))
                aufladen = 0
                   
        #handling of closing the game via ESC
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        for i in (greenlist):
            for j in abschussliste:

                if i.touch(j) == True:
                    abschussliste.remove(j)
                    greenlist.remove(i)
            

        #updating the screen
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        for obj in flyingObjects:
            obj.update()
            screen.blit(obj.bildVariable,(obj.box[0],obj.box[1]))
            if obj.box[1] >= 650:
                if obj in friendlist:
                    flyingObjects.remove(obj)
                    friendlist.remove(obj)
                    if leben == 1:
                        leben += 1
                        lebensliste.append(objectRect.Lives(50,10))
                    elif leben == 2:
                        leben += 1
                        lebensliste.append(objectRect.Lives(90,10))

                else:    
                    flyingObjects.remove(obj)
                    leben -= 1
                    lebensliste.remove(lebensliste[-1])
                    
        clock.tick(30)
        score.update()
        screen.blit(score.textsurface,(650,10))
        kreis.update()
        screen.blit(kreis.bildVariable,(kreis.box[0],kreis.box[1]))
        
        for i in lebensliste:
            screen.blit(i.bildVariable,(i.box[0],i.box[1]))
        for obj in abschussliste:
            obj.update()

        for i in (flyingObjects):
            if kreis.touch(i) == True:
                flyingObjects.remove(i)



        for i in (flyingObjects):
            for j in abschussliste:

                if i.touch(j) == True:
                    textscore += 1
                    abschussliste.remove(j)
                    if i in yellowlist:
                        textscore -= 1
                        flyingObjects.append(objectRect.Red(black,[i.box[0],i.box[1]],(i.box[2],i.box[3]),i.speed))
                        flyingObjects[-1].changeBild()
                        yellowlist.remove(i)
                    else:
                        boom.append(objectRect.Boom(i.box[0],i.box[1]))
           
                    if i in greenInvaders:
                        greenInvaders.remove(i)

                    if i in friendlist:
                        textscore -= 1
                        leben -= 1
                        lebensliste.remove(lebensliste[-1])
                        
                    score.change(str(textscore))
                    flyingObjects.remove(i)
            
        new += 1
        if new >= 25 and allEnemies < 50:
            type = random.randint(0,99)
            if 9 >= type >= 0:
                flyingObjects.append(objectRect.Green(black,[70,50],(27,22),2))
                greenInvaders.append(flyingObjects[-1])
                greenInvaders[-1].changeBild()

            elif 19 >= type >= 10:

                flyingObjects.append(objectRect.Yellow(black,[70,50],(27,22),2))
                flyingObjects[-1].changeBild()
                yellowlist.append(flyingObjects[-1])

            elif 21 >= type >= 20:
                flyingObjects.append(objectRect.Friend(black,[70,50],(27,22),2))
                flyingObjects[-1].changeBild()
                friendlist.append(flyingObjects[-1])
                
            else:
                flyingObjects.append(objectRect.FlyingBox(black,[70,50],(27,22),2))          #allEnemies += 1
            new = 0

        if leben == 0: 
            screen.fill((0,0,0))
            screen.blit(pygame.font.SysFont('Comic Sans MS', 60).render("Game Over", False, red),(200,200))
            screen.blit(pygame.font.SysFont('Comic Sans MS', 30).render("Dein Score ist: " + str(textscore), False, white),(225,300))
            break
                
        for i in greenInvaders:
            if i.clock >= 60:
                i.clock = 0
                greenlist.append(objectRect.Schuesse(green,[i.box[0]+(i.box[2]/2),i.box [1]+(i.box[3]/2)],(2,10),-5))

        for i in greenlist:
            if i.touch(kreis) == True: 
                greenlist.remove(i)
                leben -= 1
                lebensliste.remove(lebensliste[-1])

            if kreis.touch(i) == True:
                greenlist.remove(i)
                leben -= 1
                lebensliste.remove(lebensliste[-1])

        for i in (boom):
            screen.blit(i.dieZwei,(i.box[0],i.box[1]))
            i.timer += 1
            if i.timer == 2:
                i.change()
            if i.timer >= 4:
                boom.remove(i)

                
        for i in abschussliste:
            if i.box[1] < 0:
                abschussliste.remove(i)
                
        for i in greenlist:        
            i.update()
            if i.box[1] > 700:
                greenlist.remove(i)

        for i in greenInvaders:
             i.clock += 1
        aufladen += 1

        pygame.display.flip()
    
    deathscreen()
 

initialize()
