# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 12:22:26 2021

@author: hugo_
"""
from RayTracer import Raytracer
from envmap import Envmap
from materials import Material, Light, AmbientLight, Texture
from shapes import Sphere, Cube, Pyramid
from obj import Color
from MATH import V3




#Materiaes y texturas
GREEN = Color(77, 102, 0)
leaf = Material(diffuse=GREEN, albedo=(1, 1, 0, 0), spec=50, refractive_index=0)
grass = Material(texture=Texture('./mcgrassT2.bmp'))
floor = Material(texture= Texture('./mcfloor.bmp'))
agua = Material(texture= Texture('./Minecraft-Water.bmp'))
wood = Material(texture= Texture('./block.bmp'))
leafs = Material(texture= Texture('./Oak-Leaves.bmp'))
creeper = Material(texture=Texture('./creeperT2.bmp'))
black = Material(texture=Texture('./black.bmp'))





render = Raytracer(768, 432)
render.envmap = Envmap('./MCsky.bmp')
render.light = Light(position=V3(0, 2, 0.2), intensity=1.5)
render.ambient_light = AmbientLight(strength = 0.1)

render.scene = [
    
    #Grass and water
    Cube(V3(0, -15, -20), 23, floor),
    
    Cube(V3(5, -6.2, -15), 6, agua),
    Cube(V3(5, -6.2, -13), 6, agua),
    Cube(V3(4, -6.2, -15), 6, agua),
    Cube(V3(4, -6.2, -13), 6, agua),
    Cube(V3(3, -6.2, -15), 6, agua),
    Cube(V3(3, -6.2, -13), 6, agua),
    
    
    #creeper
    Cube(V3(0,0,-10), 1.2, creeper),
    Cube(V3(0,-1,-10), 1.2, creeper),
    
    Cube(V3(-0.15, 0.1, -5), 0.15, black),
    Cube(V3(0.15, 0.1, -5), 0.15, black),
    Cube(V3(0, -0.15, -5), 0.2, black),



    

    
    
    
   #Montañas
    Pyramid([V3(3, -1.4, -10.5), V3(1.9, -0.1, -10.5), V3(0.8, -1.4, -10.5), V3(2.5, -1, -12)], leaf),
    Pyramid([V3(-3, -1.4, -10.5), V3(-1.9, -0.1, -10.5), V3(-0.8, -1.4, -10.5), V3(-2.5, -1, -12)], leaf),

    
    

    


    
    Cube(V3(-7, -2, -8), 1, grass),
    Cube(V3(-6.5, -2, -8), 1, grass),
    Cube(V3(-6, -2, -8), 1, grass),
    Cube(V3(-5.5, -2, -8), 1, grass),
    Cube(V3(-5, -2, -8), 1, grass),
    Cube(V3(-4.5, -2, -8), 1, grass),
    Cube(V3(-4.0, -2, -8), 1, grass),
    Cube(V3(-3.5, -2, -8), 1, grass),
    
    Cube(V3(-7, -2, -8.5), 1, grass),
    Cube(V3(-6.5, -2, -8.5), 1, grass),
    Cube(V3(-6, -2, -8.5), 1, grass),
    Cube(V3(-5.5, -2, -8.5), 1, grass),
    Cube(V3(-5, -2, -8.5), 1, grass),
    Cube(V3(-4.5, -2, -8.5), 1, grass),
    Cube(V3(-4.0, -2,-8.5), 1, grass),
    Cube(V3(-3.5, -2, -8.5), 1, grass),
    
   
    Cube(V3(-7, -2, -9), 1, grass),
    Cube(V3(-6.5, -2, -9), 1, grass),
    Cube(V3(-6, -2, -9), 1, grass),
    Cube(V3(-5.5, -2, -9), 1, grass),
    Cube(V3(-5, -2, -9), 1, grass),
    Cube(V3(-4.5, -2, -9), 1, grass),
    Cube(V3(-4.0, -2,-9), 1, grass),
    Cube(V3(-3.5, -2, -9), 1, grass),
    
    Cube(V3(-7, -2, -9.5), 1, grass),
    Cube(V3(-6.5, -2, -9.5), 1, grass),
    Cube(V3(-6, -2, -9.5), 1, grass),
    Cube(V3(-5.5, -2, -9.5), 1, grass),
    Cube(V3(-5, -2, -9.5), 1, grass),
    Cube(V3(-4.5, -2, -9.5), 1, grass),
    Cube(V3(-4.0, -2,-9.5), 1, grass),
    Cube(V3(-3.5, -2, -9.5), 1, grass),
    
    Cube(V3(-7, -2, -10), 1, grass),
    Cube(V3(-6.5, -2, -10), 1, grass),
    Cube(V3(-6, -2, -10), 1, grass),
    Cube(V3(-5.5, -2, -10), 1, grass),
    Cube(V3(-5, -2, -10), 1, grass),
    Cube(V3(-4.5, -2, -10), 1, grass),
    Cube(V3(-4.0, -2,-10), 1, grass),
    Cube(V3(-3.5, -2, -10), 1, grass),
    
    
    #tree
    Cube(V3(-5.5, -1 , -8.5), 1 , wood),
    Cube(V3(-5.5, 0   , -8.5), 1 , wood),
    Cube(V3(-5.5, 1   , -8.5), 1 , wood),
    
    
    #Ramas izquierdas
    Cube(V3(-5.5, 1   , -8), 1 , leafs),
    Cube(V3(-5.5, 1   , -7.5), 1 , leafs),
    
    #tronco
    Cube(V3(-5.5, 2   , -8.5), 1 , leafs),


    Cube(V3(-5.5, 1   , -9), 1 , leafs),

    #frontal
    Cube(V3(-5, 1   , -8.5), 1 , leafs),
    Cube(V3(-4.5, 1   , -8.5), 1 , leafs),

    
    
    #trasera
    Cube(V3(-6, 1  , -8.5), 1 , leafs),
    Cube(V3(-6.5, 1  , -8.5), 1 , leafs),
 
]

render.finish()
