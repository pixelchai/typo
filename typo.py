import random

# cordinate system: q=(0,0), a=(0,-1), w=(1,0), etc
# all keys 1x1 squares
import math

keys = ["qwertyuiop",
        "asdfghjkl",
        "zxcvbnm"]
xoffs = [0, 0.5, 1.5]


def getCoord(c):
    c = c.lower()
    i = 0
    for row in keys:
        if c in row:
            x = keys[i].index(c) + xoffs[i]
            return (x, -i)
        i += 1


def getCentre(c):
    (x, y) = getCoord(c)
    return (x + 0.5, y - 0.5)


def segsIntersects(x1, y1, x2, y2, x3, y3, x4, y4):
    a1 = y2 - y1
    b1 = x1 - x2
    c1 = (x2 * y1) - (x1 * y2)

    r3 = ((a1 * x3) + (b1 * y3) + c1)
    r4 = ((a1 * x4) + (b1 * y4) + c1)

    if ((r3 != 0) and (r4 != 0) and sameSign(r3, r4)):
        return 0

    a2 = y4 - y3
    b2 = x3 - x4
    c2 = (x4 * y3) - (x3 * y4)

    r1 = (a2 * x1) + (b2 * y1) + c2
    r2 = (a2 * x2) + (b2 * y2) + c2

    if ((r1 != 0) and (r2 != 0) and (sameSign(r1, r2))):
        return 0

    denom = (a1 * b2) - (a2 * b1)

    if denom == 0:
        return 1  # collinear
    return 1


def rectsegIntersects(ax, ay, bx, by, rx, ry, w=1, h=1):
    pts = [
        [rx, ry],
        [rx + w, ry],
        [rx + w, ry - h],
        [rx, ry - h]
    ]
    segs = [
        [pts[0], pts[1]],
        [pts[1], pts[2]],
        [pts[2], pts[3]],
        [pts[3], pts[0]],
    ]

    for seg in segs:
        if segsIntersects(ax, ay, bx, by, seg[0][0], seg[0][1], seg[1][0], seg[1][1]):
            return 1
    return 0


def sameSign(a, b):
    return math.copysign(a, b) == a


def crossWhich(sel, dir, mag):
    ret = ""

    (ax, ay) = getCentre(sel)
    (bx, by) = (ax + math.cos(dir) * mag, ay + math.sin(dir) * mag)

    (sx, sy) = getCoord(sel)
    sx = int(sx)
    sy = int(sy) * -1
    w = 10
    h = 3
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(w, h) ** 2):
        if (-w / 2 < x <= w / 2) and (-h / 2 < y <= h / 2):
            # do
            cx = sx + x
            cy = sy + y
            if cy > -1 and cy < 3:
                row = keys[cy]
                cx -= xoffs[cy]
                cx = int(round(cx))
                if cx > -1 and cx < len(row):
                    c = row[cx]
                    if c is not sel:
                        # print c
                        if rectsegIntersects(ax, ay, bx, by, *getCoord(c)):
                            ret += (c)

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return ret


def gen(str, f1=0.5, f2=1.5, must=1, n=1):
    if (''.join(ch for ch in str if ch.isalpha())).strip() == '':
        return str

    sel = ''
    while (''.join(ch for ch in sel if ch.isalpha())).strip() == '':
        index = random.randint(0, len(str) - 1)
        sel = str[index]

    dir = random.uniform(0, 2 * math.pi)
    mag = random.uniform(f1, f2)

    ret = str[:index] + sel + crossWhich(sel, dir, mag) + str[index + 1:]
    if must:
        while ret == str:
            ret = gen(str, f1, f2, must, n)
    if n > 1:
        ret = gen(ret, f1, f2, must, n - 1)
    return ret


print gen("the quick brown fox jumps over a lazy dog")