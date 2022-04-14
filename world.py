import pygame.key
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN

from main_field import MainFieldType

offset_constant = 5.0


class World:
    def __init__(self, width, height):
        self.render_offset_x = 0
        self.render_offset_y = 0

        self.width = width
        self.height = height

        self.main_field_array = []
        for i in range(0, width * height):
            self.main_field_array.append(MainFieldType.WATER)

    def get_main_field(self, x, y):
        return self.main_field_array[y * self.width + x]

    def set_main_field(self, x, y, value):
        self.main_field_array[y * self.width + x] = value

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.render_offset_x += offset_constant  # todo: delta time
        if keys[K_RIGHT]:
            self.render_offset_x -= offset_constant
        if keys[K_UP]:
            self.render_offset_y += offset_constant
        if keys[K_DOWN]:
            self.render_offset_y -= offset_constant

    def render(self, main_field_registry, screen):
        for x in range(0, self.width):
            for y in range(0, self.height):
                field = main_field_registry.get_field(self.get_main_field(x, y))

                screen.blit(field.get_texture(), (self.render_offset_x + x * 128, self.render_offset_y + y * 128))
