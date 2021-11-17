# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 17:17:07 2021

@author: hugo_

librerias matemáticas
"""
from collections import namedtuple

EPSILON = 0.0001
pi = 3.1416

V2 = namedtuple("Vertex2", ["x", "y"])
V3 = namedtuple("Vertex3", ["x", "y", "z"])

def sumVectors(vec1, vec2):
    sumList = []
    sumList.extend((vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2]))
    return sumList

def subVectors(vec1, vec2):
    # if len(vec1) == 0:
    #     vec1 = [1, 1, 1]
    # if len(vec2) == 0:
    #     vec2 = [1, 1, 1]
    subList = []
    subList.extend((vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2]))
    return subList

def mulVectors(vec1, vec2):
    mulList = []
    mulList.extend((vec1[0] * vec2[0], vec1[1] * vec2[1], vec1[2] * vec2[2]))
    return mulList

def dotVectors(v0, v1):
    # if len(v0) == 0:
    #     v0 = [1, 1, 1]
    #     # return ((v1[0]) + (v1[1]) + (v1[2]))
    # if len(v1) == 0:
    #     v1 = [1, 1, 1]
    
    return ((v0[0] * v1[0]) + (v0[1] * v1[1]) + (v0[2] * v1[2]))
    
# Producto cruz entre dos vectores
def cross(v0, v1):
    arr_cross = []
    arr_cross.extend((v0[1] * v1[2] - v1[1] * v0[2], -(v0[0] * v1[2] - v1[0] * v0[2]), v0[0] * v1[1] - v1[0] * v0[1]))
    return arr_cross

# Multiplicacion de un escalar con un vector de 3 elementos
def multiply(dotNumber, normal):
    arrMul = []
    arrMul.extend((dotNumber * normal[0], dotNumber * normal[1], dotNumber * normal[2]))
    return arrMul

def divVN(v, n):
    arrDiv = []
    arrDiv.extend((v[0] / n, v[1] / n, v[2] / n))
    return arrDiv

# Calculo de la normal
def frobeniusNorm(v0):
    return((v0[0]**2 + v0[1]**2 + v0[2]**2)**(1/2))


def sum(v0, v1):
    """
        Input: 2 size 3 vectors
        Output: Size 3 vector with the per element sum
    """
    return V3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)

def sumVectors(vec1, vec2):
    sumList = []
    sumList.extend((vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2]))
    return sumList

def sub(v0, v1):
    """
        Input: 2 size 3 vectors
        Output: Size 3 vector with the per element substraction
    """
    return V3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)


def mul(v0, k):
    """
        Input: 2 size 3 vectors
        Output: Size 3 vector with the per element multiplication
    """
    return V3(v0.x * k, v0.y * k, v0.z * k)


def dot(v0, v1):
    """
        Input: 2 size 3 vectors
        Output: Scalar with the dot product
    """
    return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z


def length(v0):
    """
        Input: 1 size 3 vector
        Output: Scalar with the length of the vector
    """
    return (v0.x ** 2 + v0.y ** 2 + v0.z ** 2) ** 0.5


def norm(v0):
    """
        Input: 1 size 3 vector
        Output: Size 3 vector with the normal of the vector
    """
    v0length = length(v0)

    if not v0length:
        return V3(0, 0, 0)

    return V3(v0.x / v0length, v0.y / v0length, v0.z / v0length)


def bbox(*vertices):
    xs = [vertex.x for vertex in vertices]
    ys = [vertex.y for vertex in vertices]

    xs.sort()
    ys.sort()

    xmin = xs[0]
    xmax = xs[-1]
    ymin = ys[0]
    ymax = ys[-1]

    return xmin, xmax, ymin, ymax


def cross(v1, v2):
    return V3(
        v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x * v2.z, v1.x * v2.y - v1.y * v2.x,
    )


def barycentric(A, B, C, P):
    cx, cy, cz = cross(
        V3(B.x - A.x, C.x - A.x, A.x - P.x), V3(B.y - A.y, C.y - A.y, A.y - P.y),
    )

    if abs(cz) < 1:
        return -1, -1, -1

    u = cx / cz
    v = cy / cz
    w = 1 - (cx + cy) / cz

    return w, v, u


def reflect(I, N):
    Lm = mul(I, -1)
    n = mul(N, 2 * dot(Lm, N))
    return norm(sub(Lm, n))

def refract(I, N, refractive_index):  # Implementation of Snell's law
    cosi = -max(-1, min(1, dot(I, N)))
    etai = 1
    etat = refractive_index

    if cosi < 0:  # if the ray is inside the object, swap the indices and invert the normal to get the correct result
        cosi = -cosi
        etai, etat = etat, etai
        N = mul(N, -1)

    eta = etai/etat
    k = 1 - eta**2 * (1 - cosi**2)
    if k < 0:
        return V3(1, 0, 0)

    return norm(sum(
        mul(I, eta),
        mul(N, (eta * cosi - k**(1/2)))
    ))
