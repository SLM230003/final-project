import pygame
pygame.init()
import math

#Code for display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Magic Circle')

#calculate where the points go
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

#Code for outer circle
pygame.draw.circle(screen, (255, 0, 0), (screen.get_width()//2, screen.get_height()//2), 100)
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 95)
pygame.draw.circle(screen, (255, 0, 0), (screen.get_width()//2 - 10, screen.get_height()//2), 37)
pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2 - 10, screen.get_height()//2), 32)

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