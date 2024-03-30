import random

import pygame
from pygame.math import Vector2

frame_count = 0
width = 800
height = 600


class PyHearts:

    def __init__(self):
        pygame.init()

        self._running = True

        self._clock = pygame.time.Clock()
        self._setup()

    def start(self):
        self._loop()

    def _setup(self):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("PyHearts")

        self.hearts = []

        for _ in range(60):
            self.hearts.append(Heart(Vector2(random.uniform(0.0, width), random.uniform(height + 16, height + 360))))

    def _loop(self):
        global frame_count
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.WINDOWCLOSE:
                    self._running = False

            self._draw()
            pygame.display.flip()
            self._clock.tick(60)
            frame_count += 1

    def _draw(self):
        self.window.fill((0, 0, 0))
        for heart in self.hearts:
            heart.show(self.window)
            heart.update()


class Heart:

    def __init__(self, pos: Vector2):
        self._heart = pygame.image.load("Heart.png").convert_alpha()
        self._pos = pos
        self._vel = Vector2(0.0, random.uniform(-1.6, -0.6))
        self._wob = Vector2()
        self._rad = random.uniform(1.0, 4.0)
        self._heart = pygame.transform.scale(self._heart, (int(self._heart.get_width() * self._rad), int(self._heart.get_width() * self._rad)))

    def update(self):
        if frame_count % 16 == 0:
            self._wob = Vector2(random.uniform(-0.6, 0.6), 0.0)
            self._pos += self._wob

        self._pos += self._vel

        if self._pos.y + self._heart.get_height() * self._rad < 0.0:
            self._pos.y = random.uniform(height, height + 160)
            self._vel = Vector2(0.0, random.uniform(-1.6, -0.6))
            self._rad = random.uniform(40.0, 60.0)

    def show(self, surface: pygame.Surface):
        surface.blit(self._heart, (self._pos.x, self._pos.y))


def main():
    PyHearts().start()
