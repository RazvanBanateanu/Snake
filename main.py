from turtle import width
import pygame
import time

if __name__ == "__main__":
    pygame.init()

    width, height = 400, 400
    surface = pygame.display.set_mode((width,height))
    surface.fill((255, 255, 255))
    pygame.display.set_caption("The Snake")

    x, y = 200, 200
    delta_x, delta_y = 0, 0

    clock = pygame.time.Clock()

    def snake():
        global x, y
        x=(x+delta_x)%width
        y=(y+delta_y)%height
        surface.fill((255, 255, 255))
        pygame.draw.rect(surface, (0, 0, 0), [x, y, 10, 10] )
        pygame.display.update()


    while True:
        events = pygame.event.get()
        for event in events:
            if(event.type == pygame.QUIT):
                pygame.quit()
            

            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                    delta_x = -10
                    delta_y = 0
                
                elif(event.key == pygame.K_RIGHT):
                    delta_x = 10
                    delta_y = 0

                elif(event.key == pygame.K_UP):
                    delta_x = 0
                    delta_y = -10

                elif(event.key == pygame.K_DOWN):
                    delta_x = 0
                    delta_y = 10
                
                else:
                    continue
                
        if(not events):
            snake()
        clock.tick(10)            
           
