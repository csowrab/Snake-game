import pygame
import random
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

white = (255,255,255)

red = (255, 0, 0)

rect_size = 10
 
display_width = 600
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

def Create_Text(Text,x,y,size,color):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(Text, largeText, color)
    TextRect.center = ((x),(y))
    gameDisplay.blit(TextSurf, TextRect)

def text_objects(text, font, red):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

class snake():
    speed = 0.9
    
    def __init__(self):
        self.x = 300
        self.y = 300
        self.x_sp = self.speed
        self.y_sp = self.speed
        self.where = "left"
        self.length = 1
        self.body = []
        
    def direction(self, direct):
        self.where = direct

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_dir(self):
        return self.where

    def get_speed(self):
        return speed

    def add_body(self):
        pass
        



class Food():

    
    def __init__(self):
        self.x = random.randint(10,590)
        self.y = random.randint(10,590)

    def eaten(self):
        self.x = random.randint(0,300)
        self.y = random.randint(0,300)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y




class game():

    def __init__(self, max_score):
        self.score = 0
        self.max_score = max_score

    def spawn_food(self, food):
        x = food.get_x() - 10
        y = food.get_y() - 10
        pygame.draw.rect(gameDisplay, white,(x, y, rect_size, rect_size))

    def spawn_snek(self, snek):
        x = snek.get_x() - 10
        y = snek.get_y() - 10
        pygame.draw.rect(gameDisplay, red, (x, y, rect_size, rect_size))

    def move_snek(self, snek):
        if snek.get_dir() == "up":
            snek.y -= snek.speed
        elif snek.get_dir() == "left":
            snek.x -= snek.speed
        elif snek.get_dir() == "right":
            snek.x += snek.speed
        else:
            snek.y += snek.speed

    def check_eaten(self, snek, food):
        if (food.get_x() - rect_size < snek.x  < food.get_x() + rect_size)  and (food.get_y() - rect_size < snek.y < food.get_y() + rect_size):
            return True
        elif (snek.get_x() - rect_size < food.get_x()  < snek.get_x() + rect_size)  and (snek.get_y() - rect_size < food.get_y()  < snek.get_y() + rect_size):
            return True
        return False

    def snek_reflection(self, snek):
        if snek.x > 600:
            snek.x = 0
        elif snek.x < 0:
            snek.x = 600

        if snek.y > 600:
            snek.y = 0
        elif snek.y < 0:
            snek.y = 600

    def draw_snek_rest(self, snek):
        for each in snek.body:
            pygame.draw.rect(gameDisplay, red, (each[0] - 10, each[1] - 10, rect_size, rect_size))
        
        
    def main(self):
        intro = True
        snek = snake()
        food = Food()
        
        self.spawn_snek(snek)
        
        while intro:
                for event in pygame.event.get():
                    print(event)
                    pygame.display.update()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    #if event.type == pygame.KEYDOWN:
                        #if event.key == pygame.K_w:
                            #if 0 < snek.speed < 1:
                                #snek.speed += 0.1
                                #if snek.speed > 0.9:
                                    #snek.speed = 0.9
                        #elif  event.key == pygame.K_s:
                           # if  0 < snek.speed <1:
                                #snek.speed -= 0.1
                                #if snek.speed < 0.1:
                                    #snek.speed = 0.1

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            if snek.where != ("down"):
                                snek.direction("up")
                        elif event.key == pygame.K_LEFT:
                            if snek.where != ("right"):
                                snek.direction("left")
                        elif event .key == pygame.K_RIGHT:
                            if snek.where != ("left"):
                                snek.direction("right")
                        elif event.key == pygame.K_DOWN:
                            if snek.where != ("up"):
                                snek.direction("down")
                else:
                        New_coord = (snek.x, snek.y)
                        if New_coord in snek.body:
                            if self.score > self.max_score:
                                Game(self.score)
                            else:
                                Game(self.max_score)
                        gameDisplay.fill((0,0,0))
                        self.spawn_food(food)
                        self.move_snek(snek)
                        
                        if len(snek.body) > 0:
                            snek.body.append(New_coord)
                            self.draw_snek_rest(snek)
                            snek.body.pop(0)
                            
                            
                        if self.check_eaten(snek, food) == True:
                            food.eaten()
                            self.score += 1
                            for i in range(0,10):
                                snek.body.append(New_coord)
                                self.move_snek(snek)
                        self.snek_reflection(snek)
                        self.spawn_snek(snek)
                        Create_Text("Score: " +str(self.score) ,575,10,10,white)
                        Create_Text("Max: " + str(self.max_score), 575,25,10,white)
                        #Create_Text("Speed: " + str(snek.speed), 575, 40, 10, white)
                        
                    

                pygame.display.update()
                    
                

                    
def Game(max_score):
    G = game(max_score)
    G.main()

Game(0)



        
        
        
