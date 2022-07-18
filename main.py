from turtle import width
import pygame
import time
import random

if __name__ == "__main__":
    pygame.init()

    width, height = 400, 400
    surface = pygame.display.set_mode((width,height))
    surface.fill((255, 255, 255))
    pygame.display.set_caption("The Snake")

    x, y = 200, 200
    delta_x, delta_y = 10, 0
    food_x = random.randrange(0, width)//10*10
    food_y = random.randrange(0, height)//10*10

    body = [(x, y)]

    clock = pygame.time.Clock()

    game_over = False

    def snake():
        global x, y, food_x, food_y, game_over
        x=(x+delta_x)%width
        y=(y+delta_y)%height

        if((x,y)) in body:
            game_over = True
            return
        
        body.append((x, y)) 
        print(body)

        if(food_x == x and food_y == y):
            print(body)
            body.append((x, y)) 
            while (food_x, food_y) in body:
                food_x, food_y = random.randrange(0,width)//10*10, random.randrange(0, height)//10*10   
        else:
            del body[0]

        surface.fill((255, 255, 255))
        pygame.draw.rect(surface, (0, 255, 0), [food_x, food_y, 10, 10])
        for (i,j) in body:
            pygame.draw.rect(surface, (0, 0, 0), [i, j, 10, 10] )
        pygame.display.update()


    while True:
        if(game_over):
            pygame.quit()
            quit()
            
        events = pygame.event.get()
        for event in events:
            if(event.type == pygame.QUIT):
                pygame.quit()
            

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                    if delta_x != 10:
                        delta_x = -10
                    delta_y = 0
                
                elif(event.key == pygame.K_RIGHT):
                    if delta_x != -10:
                        delta_x = 10
                    delta_y = 0

                elif(event.key == pygame.K_UP):
                    delta_x = 0
                    if delta_y != 10:
                        delta_y = -10

                elif(event.key == pygame.K_DOWN):
                    delta_x = 0
                    if delta_y != -10:
                        delta_y = 10
                
                else:
                    continue
                
        if(not events):
            snake()
        clock.tick(10)            
           
