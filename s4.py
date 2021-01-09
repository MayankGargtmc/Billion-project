import physics1 as pf
import pygame
from pygame.locals import *
import pygame.gfxdraw
import numpy as np

# initialize physics simulation
DIM = np.asarray([600, 600])
GRAVITY = np.asarray([0, 0])
dt = 0.01
env = pf.Environment(DIM, GRAVITY, dt)

pygame.init()
screen = pygame.display.set_mode((DIM[0], DIM[1]))
pygame.display.set_caption('Elastic Collision Particle Simulation')

number_of_particles = 12
part=[]

for n in range(number_of_particles):

    radius = int(10)
    density = int(2)
    mass = (4/3)*density*np.pi*radius**3
    X = np.random.rand(1, 2)*(DIM-radius)+radius
    V = np.asarray([[0, 0]], dtype='float64')*75
    A = np.asarray([0, 0])
    particle = pf.Particle(env, X, V, A, radius, mass, density)
    env.addParticle(particle)
    part.append(particle)

def display(env):
    for p in env.particles:
        pygame.gfxdraw.filled_circle(screen, int(p.X[0][0]), int(p.X[0][1]), p.radius, p.colour)

def create():
    particle.radius = 20
    particle.mass = 7000
    particle.key = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYUP:
            if event.key == K_UP:
                    particle.V = np.asarray([[0, -200]], dtype='float64')
                    create()


            if event.key == K_DOWN:
                particle.V = np.asarray([[0, 200]], dtype='float64')
                create()

            if event.key == K_LEFT:
                particle.V = np.asarray([[-200, 0]], dtype='float64')
                create()

            if event.key == K_RIGHT:
                particle.V = np.asarray([[200, 0]], dtype='float64')
                create()

            if event.key == K_SPACE:
                particle.X = np.asarray([[300, 550]], dtype='float64')
                create()
                #val = id(particle)


    screen.fill([255, 255, 255])
    env.update()
    display(env)
    pygame.display.flip()

''' for parts in part:
        if parts.V.all() > 0:
            if np.all(parts.V != [[0, 0]]) and particle.key:
                parts.addForce(-100)

        elif parts.V.all() < 0:
            if np.all(parts.V != [[0, 0]]) and particle.key:
                parts.addForce(100)

        else:
            pass'''

