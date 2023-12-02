import pygame
pygame.init()
import math
import random

#Code for display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Magic Circle')

#Code for color
rainbow = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#Code for outer circle
pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 490) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 485) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 475) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 470) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 460) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 455) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 445) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 440) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 430) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 425) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 415) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 410) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 400) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 395) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 385) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 380) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 370) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 365) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 355) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 350) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 340) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 335) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 325) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 320) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 310) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 305) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 295) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 290) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 280) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 275) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 265) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 260) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 250) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 245) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 235) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 230) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 220) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 215) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 205) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 200) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 190) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 185) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 175) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 170) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 160) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 155) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 145) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 140) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 130) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 125) # by 15 pixels each

pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 115) # by 15 pixels each
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 110) # by 10 pixels each

pygame.draw.circle(screen, (255, 0, 0), (screen.get_width()//2, screen.get_height()//2), 100)
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 95)
pygame.draw.circle(screen, (255, 0, 0), (screen.get_width()//2 - 10, screen.get_height()//2), 37)
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2 - 10, screen.get_height()//2), 32)

#calculate where the points go for triangle
x = 800 // 2
y = 600 // 2
radius = 95

# Code to define the points of the triangle
angle1 = math.radians(0)
angle2 = math.radians(120)
angle3 = math.radians(240)

point1 = (x + radius * math.cos(angle1), y + radius * math.sin(angle1))
point2 = (x + radius * math.cos(angle2), y + radius * math.sin(angle2))
point3 = (x + radius * math.cos(angle3), y + radius * math.sin(angle3))

#Code to define the points of square
x = 780 // 2
y = 600 // 2
side_length = 77

points = [(x - side_length // 2, y - side_length // 2),
          (x + side_length // 2, y - side_length // 2),
          (x + side_length // 2, y + side_length // 2),
          (x - side_length // 2, y + side_length // 2)]

#code for triangle
pygame.draw.polygon(screen, (255, 0, 0), [point1, point2, point3], 5)
#Code for square
pygame.draw.polygon(screen, (255, 0, 0), points, 5)

pygame.display.flip()

#Code for quiting and any other key functions
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()