from enum import IntEnum;

import pygame.image


class MainFieldType(IntEnum):
    WATER = 0,
    SAND = 1


class MainField:
    def __init__(self, main_field_type):
        self.main_field_type = main_field_type

        self.texture = pygame.image.load(str(self.main_field_type) + ".png")

    def get_type(self):
        return self.main_field_type

    def get_texture(self):
        return self.texture


class MainFieldRegistry:
    def __init__(self):
        self.fields = []
        self.closed = False

    def close(self):
        self.closed = True

    def add(self, main_field):
        main_field_type = main_field.get_type()
        if int(main_field_type) != len(self.fields):
            raise Exception("Invalid index")
        self.fields.append(main_field)

    def get_field(self, main_field_type):
        return self.fields[int(main_field_type)]