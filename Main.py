import math
import pygame
import numpy as np
from Sim import Simulation

# Initialize global variables
NUMBER_OF_CARS = 10
ROAD_LENGTH = 100
# PERCENTOFROAD = 0 # from 0 to 100
SPEEDOFCAR = 0 # from 0 to 100
SIZEOFDISPLAY = 700
ROFCIRCLE = SIZEOFDISPLAY / 2.5


SIM = Simulation(NUMBER_OF_CARS)
cars = SIM.getCars()




def calculatePosition(position, r):
    """Given a position ranging from 0 ROAD_LENGTH, return x and y values of car's position on circle of radius r"""
    theta = (math.pi * 2 * position) / ROAD_LENGTH
    return [(r * math.cos(theta) + SIZEOFDISPLAY/2), (abs(r * math.sin(theta) - SIZEOFDISPLAY/2))]


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SIZEOFDISPLAY, SIZEOFDISPLAY])

# Run until the user asks to quit
running = True
while running:

    # Delays updates
    pygame.time.delay(10)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            #on click, spawn in car at given position
            mouseX, mouseY = pygame.mouse.get_pos()
            #calculate theta of line from center of circle to mouse
            #circle center is SIZEOFDISPLAY / 2
            center = SIZEOFDISPLAY/2
            opp = abs(center - mouseY)
            adj = abs(mouseX - center)
            theta = np.arctan(opp / adj)
            if mouseX < center and mouseY < center:
                theta = math.pi - theta
            elif mouseX < center and mouseY > center:
                theta = math.pi + theta
            elif mouseX > center and mouseY > center:
                theta = 2 * math.pi - theta
            pos = theta / (2 * math.pi) * 100
            #create and draw a car at the calculated position
            c = SIM.createCar(pos)
            pygame.draw.circle(screen, (abs(math.cos(c.velocity)) * 255, abs(math.sin(c.velocity)) * 255, 0), calculatePosition(c.position, ROFCIRCLE), 10)
            SIM.update()

    # Fill the background with white
    screen.fill((255, 255, 255))


    # Draw a circle to represent each car, color based off speed
    for car in SIM.getCars():
        pygame.draw.circle(screen, ((1 - car.velocity / car.maxVelocity) * 255, (car.velocity / car.maxVelocity) * 255, 0), calculatePosition(car.position, ROFCIRCLE), 10)

        
    # Update animation
    pygame.display.update() 
        

    #update state of each car
    SIM.update()
    
    # Flip the display
    pygame.display.flip()


pygame.quit()

