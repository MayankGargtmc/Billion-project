import numpy as np


# define size of physics environment
class Environment():
    def __init__(self, DIM, GRAVITY, dt):
        self.DIM = DIM
        self.GRAVITY = GRAVITY
        self.dt = dt
        self.particles = []
        self.e = 2

    def update(self):
        for p1 in self.particles:
            p1.stateUpdate()
            self.bounce(p1)
            for p2 in self.particles:
                if p1 != p2:
                    self.elasticCollision(p1, p2)

    def addParticle(self, p):
        self.particles.append(p)
        p.addAcceleration(self.GRAVITY)

    def bounce(self, p):
        for p in self.particles:
            i = 0
            for x in p.X[0]:
                if x > self.DIM[i] - p.radius:
                    dist = p.radius - (self.DIM[i] - x)
                    p.addPosition(-dist)
                    tmp = np.zeros(np.size(p.V))
                    tmp[i] = -2 * p.V[0][i]
                    p.addVelocity(tmp)
                elif x < p.radius:
                    dist = p.radius - x
                    p.addPosition(dist)
                    tmp = np.zeros(np.size(p.X))
                    tmp[i] = -2 * p.V[0][i]
                    p.addVelocity(tmp)
                i += 1

    def elasticCollision(self, p1, p2):
        dX = p1.X - p2.X
        dist = np.sqrt(np.sum(dX ** 2))
        if dist < p1.radius + p2.radius:
            offset = dist - (p1.radius + p2.radius)
            p1.addPosition((-dX / dist) * offset / 2)
            p2.addPosition((dX / dist) * offset / 2)
            total_mass = p1.mass + p2.mass
            dv1 = -2 * p2.mass / total_mass * np.inner(p1.V - p2.V, p1.X - p2.X) / np.sum((p1.X - p2.X) ** 2) * (
                        p1.X - p2.X)
            dv2 = -2 * p1.mass / total_mass * np.inner(p2.V - p1.V, p2.X - p1.X) / np.sum((p2.X - p1.X) ** 2) * (
                        p2.X - p1.X)
            p1.addVelocity(dv1)
            p2.addVelocity(dv2)


# define particle class
class Particle():
    def __init__(self, env, X, V, A, radius, mass, density, key=0):
        self.env = env
        self.X = X
        self.V = V
        self.A = A
        self.radius = radius
        self.mass = mass
        self.density = density
        self.colour = (0, 0, int((density - 5) / 95 * 240 + 15))
        self.key = key

    def control_v(self, V):
        if self.key:
            self.V = V

    def control_pos(self, X):
        self.X = X

    def addForce(self, F):
        self.A += F / self.mass

    def addAcceleration(self, acc):
        self.A += acc

    def addVelocity(self, vel):
        self.V += vel

    def addPosition(self, pos):
        self.X += pos

    def attract(self, particle):
        r = self.X - particle.X
        self.A += 6.67408e-11 * particle.mass / r ** 2

    def stateUpdate(self):
        self.V += self.A * self.env.dt
        self.X += self.V * self.env.dt - 0.5 * self.A * self.env.dt ** 2


