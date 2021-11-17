# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:04:42 2021

@author: hugo_
"""

import struct
from obj import Color
from MATH import V3

WHITE = Color(255, 255, 255)


class AmbientLight(object):
    def __init__(self, strength = 0, _color = WHITE):
        self.strength = strength
        self.color = _color

class PointLight(object):
    def __init__(self, position = V3(0,0,0), _color = WHITE, intensity = 1):
        self.position = position
        self.intensity = intensity
        self.color = _color

class Light(object):
    def __init__(self, position=V3(0, 0, 0), intensity=1):
        self.position = position
        self.intensity = intensity


class Material(object):
    def __init__(self, diffuse=WHITE, albedo=(1, 0, 0, 0), spec=0, refractive_index=1, texture = None):
        self.diffuse = diffuse
        self.albedo = albedo
        self.spec = spec
        self.refractive_index = refractive_index
        self.texture = texture

class Texture(object):
    def __init__(self, path):
        self.path = path
        self.read()
        
    def read(self):
        image = open(self.path, 'rb')
        image.seek(10)
        header_size = struct.unpack('=l', image.read(4))[0]

        image.seek(14 + 4)
        self.width = struct.unpack('=l', image.read(4))[0]
        self.height = struct.unpack('=l', image.read(4))[0]
        image.seek(header_size)

        self.pixels = []

        for y in range(self.height):
            self.pixels.append([])
            for x in range(self.width):
                b = ord(image.read(1)) / 255
                g = ord(image.read(1)) / 255
                r = ord(image.read(1)) / 255
                self.pixels[y].append(Color(r,g,b))

        image.close()

    def get_color(self, tx, ty):
        if tx >= 0 and tx <= 1 and ty >= 0 and ty <= 1:
            x = int(tx * self.width - 1)
            y = int(ty * self.height - 1)

            return self.pixels[y][x]
        else:
            return Color(0,0,0)


class Intersect(object):
    def __init__(self, distance, point, normal, text_coords = None):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.text_coords = text_coords