# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:00:04 2021

@author: hugo_
"""

from MATH import *
from materials import Intersect
from math import sqrt, inf


# Credito a https://github.com/tobycyanide/pytracer en el desarrollo de algunas figuras

class Plane(object):
    """
    Creates a new Plane model    
    """
    def __init__(self, position, normal, material):
        self.position = position
        self.normal = norm(normal)
        self.material = material

    def ray_intersect(self, origin, direction):
        d = dot(direction, self.normal)

        if abs(d) > 0.0001:
            t = dot(self.normal, sub(self.position, origin)) / d
            if t > 0:
                hit = sum(origin, V3(direction.x * t, direction.y * t, direction.z * t))

                return Intersect(distance=t, point=hit, normal=self.normal)

        return None

class cube(object):
    def __init__(self, position, size, material):
        self.position = position
        self.size = size
        self.material = material
        self.planes = []

        halfSizeX = size[0] / 2
        halfSizeY = size[1] / 2
        halfSizeZ = size[2] / 2

        self.planes.append( Plane( sumVectors(position, (halfSizeX, 0, 0)), (1, 0, 0), material))
        self.planes.append( Plane( sumVectors(position, (-halfSizeX, 0, 0)), (-1, 0, 0), material))

        self.planes.append( Plane( sumVectors(position, (0, halfSizeY, 0)), (0, 1, 0), material))
        self.planes.append( Plane( sumVectors(position, (0, -halfSizeY, 0)), (0, -1, 0), material))

        self.planes.append( Plane( sumVectors(position, (0, 0, halfSizeZ)), (0, 0, 1), material))
        self.planes.append( Plane( sumVectors(position, (0, 0, -halfSizeZ)), (0, 0, -1), material))


    def ray_intersect(self, orig, dir):

        epsilon = 0.001

        boundsMin = [0,0,0]
        boundsMax = [0,0,0]

        for i in range(3):
            boundsMin[i] = self.position[i] - (epsilon + self.size[i] / 2)
            boundsMax[i] = self.position[i] + (epsilon + self.size[i] / 2)

        t = float('inf')
        intersect = None
        uvs = None

        for plane in self.planes:
            planeInter = plane.ray_intersect(orig, dir)

            if planeInter is not None:
                if planeInter.point[0] >= boundsMin[0] and planeInter.point[0] <= boundsMax[0]:
                    if planeInter.point[1] >= boundsMin[1] and planeInter.point[1] <= boundsMax[1]:
                        if planeInter.point[2] >= boundsMin[2] and planeInter.point[2] <= boundsMax[2]:
                            if planeInter.distance < t:
                                t = planeInter.distance
                                intersect = planeInter

                                if abs(plane.normal[0]) > 0:
                                    u = (planeInter.point [1] - boundsMin[1]) / (boundsMax[1] - boundsMin[1])
                                    v = (planeInter.point [2] - boundsMin[2]) / (boundsMax[2] - boundsMin[2])

                                elif abs(plane.normal[1]) > 0:
                                    u = (planeInter.point [0] - boundsMin[0]) / (boundsMax[0] - boundsMin[0])
                                    v = (planeInter.point [2] - boundsMin[2]) / (boundsMax[2] - boundsMin[2])

                                elif abs(plane.normal[2]) > 0:
                                    u = (planeInter.point [0] - boundsMin[0]) / (boundsMax[0] - boundsMin[0])
                                    v = (planeInter.point [1] - boundsMin[1]) / (boundsMax[1] - boundsMin[1])

                                uvs = [u, v]

        if intersect is None:
            return None

        return Intersect(distance = intersect.distance,
                         point = intersect.point,
                         normal = intersect.normal,
                         texCoords = uvs,
                         sceneObject = self)

class Cube(object):
    """
    Creates a new Cube model    
    """
    def __init__(self, position, size, material):
        self.position = position
        self.size = size
        self.material = material
        
        mid_size = size / 2

        self.planes = [
            Plane(sum(position, V3(mid_size, 0, 0)), V3(1, 0, 0), material),
            Plane(sum(position, V3(-mid_size, 0, 0)), V3(-1, 0, 0), material),
            Plane(sum(position, V3(0, mid_size, 0)), V3(0, 1, 0), material),
            Plane(sum(position, V3(0, -mid_size, 0)), V3(0, -1, 0), material),
            Plane(sum(position, V3(0, 0, mid_size)), V3(0, 0, 1), material),
            Plane(sum(position, V3(0, 0, -mid_size)), V3(0, 0, -1), material)
        ]
        # mid_sizex = size[0] / 2
        # mid_sizey = size[1] / 2
        # mid_sizez = size[2] / 2

        # self.planes = [
        #     Plane(sumVectors(position, (mid_sizex, 0, 0)), (1, 0, 0), material),
        #     Plane(sumVectors(position, (-mid_sizex, 0, 0)), (-1, 0, 0), material),
        #     Plane(sumVectors(position, (0, mid_sizey, 0)), (0, 1, 0), material),
        #     Plane(sumVectors(position, (0, -mid_sizey, 0)), (0, -1, 0), material),
        #     Plane(sumVectors(position, (0, 0, mid_sizez)), (0, 0, 1), material),
        #     Plane(sumVectors(position, (0, 0, -mid_sizez)), (0, 0, -1), material)
        # ]
        

    def ray_intersect(self, origin, direction):
        epsilon = 0.001

        min_bounds = [0, 0, 0]
        max_bounds = [0, 0, 0]

        for i in range(3):
            min_bounds[i] = self.position[i] - (epsilon + self.size / 2)
            max_bounds[i] = self.position[i] + (epsilon + self.size / 2)

        t = float("inf")
        intersect = None
        texture_coords = None

        for plane in self.planes:
            plane_intersection = plane.ray_intersect(origin, direction)

            if plane_intersection is not None:
                if (
                    plane_intersection.point[0] >= min_bounds[0]
                    and plane_intersection.point[0] <= max_bounds[0]
                ):
                    if (
                        plane_intersection.point[1] >= min_bounds[1]
                        and plane_intersection.point[1] <= max_bounds[1]
                    ):
                        if (
                            plane_intersection.point[2] >= min_bounds[2]
                            and plane_intersection.point[2] <= max_bounds[2]
                        ):
                            if plane_intersection.distance < t:
                                t = plane_intersection.distance
                                intersect = plane_intersection

                                if abs(plane.normal[2]) > 0:
                                    coord0 = (plane_intersection.point [0] - min_bounds[0]) / (max_bounds[0] - min_bounds[0])
                                    coord1 = (plane_intersection.point [1] - min_bounds[1]) / (max_bounds[1] - min_bounds[1])

                                elif abs(plane.normal[1]) > 0:
                                    coord0 = (plane_intersection.point [0] - min_bounds[0]) / (max_bounds[0] - min_bounds[0])
                                    coord1 = (plane_intersection.point [2] - min_bounds[2]) / (max_bounds[2] - min_bounds[2])

                                elif abs(plane.normal[0]) > 0:
                                    coord0 = (plane_intersection.point [1] - min_bounds[1]) / (max_bounds[1] - min_bounds[1])
                                    coord1 = (plane_intersection.point [2] - min_bounds[2]) / (max_bounds[2] - min_bounds[2])

                                texture_coords = [coord0, coord1]

        if intersect is None:
            return None

        return Intersect(
            distance=intersect.distance, point=intersect.point, normal=intersect.normal, text_coords=texture_coords
        )


class Sphere(object):
    """
    Creates a new Sphere model    
    """
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, origin, direction):
        L = sub(self.center, origin)
        tca = dot(L, direction)
        l = length(L)
        d2 = l ** 2 - tca ** 2
        if d2 > self.radius ** 2:
            return None
        thc = (self.radius ** 2 - d2) ** 1 / 2
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None

        hit = sum(origin, mul(direction, t0))
        normal = norm(sub(hit, self.center))

        return Intersect(distance=t0, point=hit, normal=normal)


class Cylinder(object):
    """
    Creates a new Cylinder model    
    """
    def __init__(self, radius, height, center, material):
        self.radius = radius
        self.height = height
        self.closed = False
        self.center = center
        self.material = material

    def ray_intersect(self, origin, direction):
        a = direction.x ** 2 + direction.z ** 2
        if abs(a) < EPSILON:
            return None

        b = 2 * (
            direction.x * (origin.x - self.center.x)
            + direction.z * (origin.z - self.center.z)
        )
        c = (
            (origin.x - self.center.x) ** 2
            + (origin.z - self.center.z) ** 2
            - (self.radius ** 2)
        )

        discriminant = b ** 2 - 4 * (a * c)

        if discriminant < 0.0:
            return None

        t0 = (-b - sqrt(discriminant)) / (2 * a)
        t1 = (-b + sqrt(discriminant)) / (2 * a)

        if t0 > t1:
            t0, t1, t1, t0

        y0 = origin.y + t0 * direction.y
        if self.center.y < y0 and y0 <= (self.center.y + self.height):
            hit = sum(origin, mul(direction, t0))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t0, point=hit, normal=normal)

        y1 = origin.y + t1 * direction.y
        if self.center.y < y1 and y1 <= (self.center.y + self.height):
            hit = sum(origin, mul(direction, t1))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t1, point=hit, normal=normal)

        return self.intersect_caps(origin, direction)

    def check_cap(self, origin, direction, t):
        x = origin.x + t * direction.x
        z = origin.z + t * direction.z
        return (x ** 2 + z ** 2) <= abs(self.radius)

    def intersect_caps(self, origin, direction):
        if self.closed == False or abs(direction.y) < EPSILON:
            return None

        t_lower = (self.center.y - origin.y) / direction.y
        if self.check_cap(origin, direction, t_lower):
            hit = sum(origin, mul(direction, t_lower))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t_lower, point=hit, normal=normal)

        t_upper = ((self.center.y + self.height) - origin.y) / direction.y
        if self.check_cap(origin, direction, t_upper):
            hit = sum(origin, mul(direction, t_upper))
            normal = norm(sub(hit, self.center))
            return Intersect(distance=t_upper, point=hit, normal=normal)

        return None


class Triangle(object):
    """
    Creates a new Triangle model    
    """
    def __init__(self, vertices, material):
        self.vertices = vertices
        self.material = material

    def ray_intersect(self, origin, direction):
        v0, v1, v2 = self.vertices
        normal = cross(sub(v1, v0), sub(v2, v0))
        determinant = dot(normal, direction)

        if abs(determinant) < EPSILON:
            return None

        distance = dot(normal, v0)
        t = (dot(normal, origin) + distance) / determinant
        if t < 0:
            return None

        point = sum(origin, mul(direction, t))
        u, v, w = barycentric(v0, v1, v2, point)

        if w < 0 or v < 0 or u < 0:  # 0 is actually a valid value! (it is on the edge)
            return None
        
        return Intersect(distance=distance, point=point, normal=norm(normal))


class Pyramid(object):
    """
    Creates a new Pyramid model (made of 4 triangles)
    """

    def __init__(self, vertices, material):
        self.sides = self.generate_sides(vertices, material)
        self.material = material

    def generate_sides(self, vertices, material):
        if len(vertices) != 4:
            return [None, None, None, None]

        v0, v1, v2, v3 = vertices
        sides = [
            Triangle([v0, v3, v2], material),
            Triangle([v0, v1, v2], material),
            Triangle([v1, v3, v2], material),
            Triangle([v0, v1, v3], material),
        ]
        return sides

    def ray_intersect(self, origin, direction):
        t = float("inf")
        intersect = None

        for triangle in self.sides:
            local_intersect = triangle.ray_intersect(origin, direction)
            if local_intersect is not None:
                if local_intersect.distance < t:
                    t = local_intersect.distance
                    intersect = local_intersect

        return intersect