import random
import pygame

class Particle():


    def __init__(self, pos=(0, 0), size=15, life=1000):
        self.pos = pos #positon of paritcle
        self.size = size #size of particle
        self.color = pygame.Color(0, 255, 0) #color of particle
        self.age = 0  #age in mil sec
        self.life = life #in mil sec
        self. dead = False #the origin of the partical is not dead
        self.alpha = 255 
        self.number = random.randint(1, 10) # assign a random number to the particle

    def update(self, dt):
        self.age += dt
        if self.age > self.life: 
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))
    
    def draw(self, surface):
        if self.dead:
            return
        font = pygame.font.Font(None, self.size)
        text = font.render(str(self.number), True, self.color)
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
    pygame.display.set_caption("Digital Rain") #sets to display a tittle at the top of the window that will open
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600) #resolution(width,height)
    screen = pygame.display.set_mode(resolution) #makes a display and uses the reslution varriable to set the size instead of repeating over and over #since set_mode returns a function surface you set the wholw code in a variable to set the surface
    rain = Rain(resolution)
    running = True 
    while running:
        #event loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # built in function that gives you an X to quit 
                running = False
        # game logic
        rain.update(dt)
        #render & display
        black = pygame.Color(0, 0, 0)
        screen.fill(black) #color of background
        rain.draw(screen)
        pygame.display.flip() #allows for flip function which allows for the code to make in a sense a flip book
        # print(particle.age)
        dt = clock.tick(12)

    pygame.quit() #clean up in order to shut down cleanly

if __name__ == "__main__":
    main()
