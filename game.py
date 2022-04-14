import pygame

from main_field import MainFieldRegistry, MainField, MainFieldType
from world import World


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Strategy Game")

        self.screen = pygame.display.set_mode([1920, 1080])
        self.running = False

        self.main_field_registry = MainFieldRegistry()
        self.main_field_registry.add(MainField(MainFieldType.WATER))
        self.main_field_registry.add(MainField(MainFieldType.SAND))

        self.world = World(10, 10)

        #debug code, will be generated in future
        self.world.set_main_field(1, 1, MainFieldType.SAND)
        self.world.set_main_field(2, 2, MainFieldType.SAND)
        self.world.set_main_field(2, 3, MainFieldType.SAND)

    def update(self):
        self.screen.fill((0, 0, 0))

        self.world.update()
        self.world.render(self.main_field_registry, self.screen)

        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
            self.update()
