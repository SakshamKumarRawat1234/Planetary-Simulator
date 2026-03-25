import pygame
import math
pygame.init()

FONT = pygame.font.SysFont("comicsans", 16)
WIDTH, HEIGHT = 1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

class Planet:

    AU = 1.496e11
    G = 6.67428e-11
    SCALE = 300 / AU
    TIMESTEP = 3600*24


    def __init__(self, name, x, y, radius, color, mass):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_position = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_position.append((int(x), int(y)))

            pygame.draw.lines(win, self.color, False, updated_position, 2)
        pygame.draw.circle(win, self.color, (int(x), int(y)), self.radius)
        name_text = FONT.render(self.name, True, (255, 255, 255))
        win.blit(name_text, (int(x)+20, int(y)+10))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / (distance ** 2)
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx 
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet("Sun",0, 0, 30, (255, 255, 0), 1.989e30 )
    sun.sun = True

    earth = Planet("Earth", -1* Planet.AU, 0, 14, (0, 0, 255), 5.97219e24)
    earth.y_vel = 29.783 * 1000

    mars = Planet("Mars", -1.52 * Planet.AU, 0, 16, (255, 0, 0), 6.39e23)
    mars.y_vel = 24.077 * 1000

    venus = Planet("Venus", -0.72 * Planet.AU, 0, 12, (255, 255, 255), 4.867e24)
    venus.y_vel = 35.02 * 1000

    planets = [sun, earth, mars, venus]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets )
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()
main()
