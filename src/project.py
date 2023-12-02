import random
import pygame
import math
import string

class Particle():


    def __init__(self, pos=(0, 0), size=15, life=1000):
        self.pos = pos #positon of paritcle
        self.size = size #size of particle

        rainbow = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.color = pygame.Color(rainbow) #color of particle
        
        self.age = 0  #age in mil sec
        self.life = life #in mil sec
        self. dead = False #the origin of the partical is not dead
        self.alpha = 255 
        # self.number = random.randint(0, 11) # assign a random number to the particle
        self.letter = random.choice(string.ascii_letters) # assign a random letter to the particle

    def update(self, dt):
        self.age += dt
        if self.age > self.life: 
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))
    
    def draw(self, surface):
        if self.dead:
            return
        font = pygame.font.Font(None, self.size)
        text = font.render(str(self.letter), True, self.color)
        text.set_alpha(self.alpha)
        surface.blit(text, self.pos) 


class ParticleTrail():

    def __init__(self, pos, size, life):
        self.pos = pos
        self.size = size
        self.life = life
        self.particles = []

    def update(self, dt):
        particle = Particle(self.pos, size = self.size, life=self.life)
        self.particles.insert(0, particle)
        self._update_particles(dt)
        self._update_pos()

    def _update_particles(self, dt):
        for idx, particle in enumerate (self.particles):
            particle.update(dt)
            if particle.dead: #deletes particles for there it not data accumulation
                del self.particles[idx]
        
    def _update_pos(self):
        x, y = self.pos
        y += self.size
        self.pos = (x, y)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)


class Rain():

    def __init__(self, screen_res):
        self.screen_res = screen_res
        self.particle_size = 15
        self.birth_rate = 1 #trails per frame
        self.trails = []
        
    def update(self, dt):
        self._birth_new_trails()
        self._update_trails(dt)

    def _update_trails(self, dt):
        for idx, trail in enumerate (self.trails):
            trail.update(dt)
            if self._trail_is_offscreen(trail):
                del self.trails[idx]


    def _trail_is_offscreen(self, trail):
        tail_is_offscreen = trail.particles[-1].pos[1] > self.screen_res[1]
        return tail_is_offscreen


    def _birth_new_trails(self):
        for count in range(self.birth_rate):
            screen_width = self.screen_res[0]
            x = random.randrange(0, screen_width, self.particle_size)
            pos = (x, 0)
            life = random.randrange(500, 3000)
            trail = ParticleTrail(pos, self.particle_size, life)
            self.trails.insert(0, trail)

    def draw(self, surface):
        for trail in self.trails:
            trail.draw(surface)


def main():
    pygame.init() #allows to initiallize the game engine
    pygame.display.set_caption("Inverting Digital Rain Drawing") #sets to display a tittle at the top of the window that will open
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600) #resolution(width,height)
    screen = pygame.display.set_mode(resolution) #makes a display and uses the reslution varriable to set the size instead of repeating over and over #since set_mode returns a function surface you set the wholw code in a variable to set the surface
    rain = Rain(resolution)
    running = True 

    show_face = True
    show_symbol = False

    while running:
        #event loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # built in function that gives you an X to quit 
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_symbol = not show_symbol
                    show_face = not show_face

        # game logic
        rain.update(dt)
        #render & display
        black = pygame.Color(0, 0, 0)
        screen.fill(black) #color of background

        if show_symbol:
            s_symbol(screen)
        if show_face:
            face(screen)

        rain.draw(screen)
        pygame.display.flip() #allows for flip function which allows for the code to make in a sense a flip book
        # print(particle.age)
        dt = clock.tick(12)

    pygame.quit() #clean up in order to shut down cleanly


def face(screen):
    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 490) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 485) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 475) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 470) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 460) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 455) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 445) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 440) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 430) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 425) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 415) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 410) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 400) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 395) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 385) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 380) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 370) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 365) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 355) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 350) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 340) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 335) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 325) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 320) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 310) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 305) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 295) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 290) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 280) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 275) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 265) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 260) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 250) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 245) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 235) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 230) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 220) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 215) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 205) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 200) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 190) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 185) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 175) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 170) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 160) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 155) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 145) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 140) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 130) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 125) # by 15 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 115) # by 15 pixels each
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 110) # by 10 pixels each

    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2, screen.get_height()//2), 100)
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 95)
    pygame.draw.circle(screen, (255,255,255), (screen.get_width()//2 - 10, screen.get_height()//2), 37)
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
    pygame.draw.polygon(screen, (255,255,255), [point1, point2, point3], 5)
    #Code for square
    pygame.draw.polygon(screen, (255,255,255), points, 5)





def s_symbol(screen):
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

    pygame.draw.circle(screen, (rainbow), (screen.get_width()//2, screen.get_height()//2), 100)
    pygame.draw.circle(screen, (0, 0, 0), (screen.get_width()//2, screen.get_height()//2), 95)
    pygame.draw.circle(screen, (rainbow), (screen.get_width()//2 - 10, screen.get_height()//2), 37)
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
    pygame.draw.polygon(screen, (rainbow), [point1, point2, point3], 5)
    #Code for square
    pygame.draw.polygon(screen, (rainbow), points, 5)


if __name__ == "__main__":
    main()
