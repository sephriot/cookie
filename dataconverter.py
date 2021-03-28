import math

from scipy.spatial.qhull import ConvexHull


def rectangle(data):
    points = data.children[-1].points
    a = math.dist([points[0], points[1]], [points[2], points[3]])
    b = math.dist([points[2], points[3]], [points[4], points[5]])
    ret = {'type': 'Rectangle', 'length': 2 * a + 2 * b, 'area': a * b, 'volume': 0}
    return ret


def circle(data):
    points = data.children[-1].points
    x = 0
    y = 0
    i = 0
    while i < len(points):
        x += points[i]
        y += points[i+1]
        i += 2

    x /= len(points) / 2.0
    y /= len(points) / 2.0
    radius = math.dist([points[0], points[1]], [x, y])
    ret = {'type': 'Circle', 'length': 2 * math.pi * radius, 'area': math.pi * radius * radius, 'volume': 0}
    ret['volume'] = ret['area'] * radius * 4.0 / 3.0
    return ret


def line(data):
    points = data.children[-1].points
    ret = {'type': 'Line', 'length': math.dist([points[0], points[1]], [points[2], points[3]]), 'area': 0, 'volume': 0}
    return ret


def freeform(data):
    points = data.children[-1].points
    pts = []
    i = 0
    while i < len(points):
        pts.append([points[i], points[i+1]])
        i += 2
    hull = ConvexHull(pts)
    ret = {'type': 'Freeform', 'length': hull.area, 'area': hull.volume, 'volume': 0}
    return ret


def convert(kind, data):
    ret = {'type': 'Dummy', 'length': 0, 'area': 0, 'volume': 0}
    if kind == 'rectangle':
        ret = rectangle(data)
    elif kind == 'circle':
        ret = circle(data)
    elif kind == 'line':
        ret = line(data)
    elif kind == 'freeform':
        ret = freeform(data)
    ret['length'] = round(ret['length'], 2)
    ret['area'] = round(ret['area'], 2)
    ret['volume'] = round(ret['volume'], 2)
    return ret
