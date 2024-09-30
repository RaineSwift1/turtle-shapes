import turtle as t
DEGREES_IN_A_CIRCLE = 360
DEGREES_IN_A_LINE = 180
def star(points,size):
    if points % 2 == 1:
        angle = int(DEGREES_IN_A_LINE-(DEGREES_IN_A_LINE/points))
        for i in range(points):
            t.forward(size)
            t.right(angle)
star(15,300)
