import numpy as np


class pointsGenerator():

    def __init__(self):

        self.arr = []

    def line(self, x1, y1, x2, y2, method):
        if method == 'bresenham':
            # Conditions:
            # * x1 < x2 and y1 < y2
            # * 0 < m < 1
            if (x1 > x2) or (y1 > y2) or ((y2-y1)/(x2-x1) > 1) or ((y2-y1)/(x2-x1) < 0):
                print("first if statement")
                raise ValueError('Invalid points for Bresenham algorithm')
            m = 2 * (y2-y1)
            mErr = m - (x2-x1)

            y = y1
            points = np.zeros((0,), dtype=np.int32)

            for x in range(x1, x2 + 1):
                points = np.append(points, np.array([x, y], dtype=np.int32))
                mErr = mErr + m
                if mErr >= 0:
                    y += 1
                    mErr = mErr - 2 * (x2 - x1)

            return points.reshape(-1, 2)

        if method == 'DDA':
            dx = abs(x2-x1)
            dy = abs(y2-y1)
            if (dx > dy):
                step = dx
            else:
                step = dy

            xinc = dx/step
            yinc = dy/step
            points = np.zeros((0,), dtype=np.int32)
            x = x1
            y = y1
            points = np.append(points, np.array([x, y], dtype=np.int32))
            for k in range(1, step+1):
                x = x + xinc
                y = y + yinc
                points = np.append(points, np.array(
                    [round(x), round(y)], dtype=np.int32))
            return points.reshape(-1, 2)

        if method == 'basic':
            m = (y2-y1)/(x2-x1)
            x = x1
            y = y1
            points = np.zeros((0,), dtype=np.int32)
            while (x <= x2):
                points = np.append(points, np.array(
                    [x, round(y)], dtype=np.int32))
                y += m
                x += 1
            return points.reshape(-1, 2)

    def circle(self, x0, y0, r, method):
        if method == 'mid-point':
            x = r
            y = 0

            points = np.zeros((0,), dtype=np.int32)
            points = np.append(points, np.array(
                [x0 + x, y0 + y], dtype=np.int32))
            print("first point:", points)

            if (r > 0):
                points = np.append(points, np.array(
                    [x0 + x, y0 - y], dtype=np.int32))
                points = np.append(points, np.array(
                    [x0 + y, y0 + x], dtype=np.int32))
                points = np.append(points, np.array(
                    [x0 - y, y0 + x], dtype=np.int32))

            p = 1 - r
            print("p = ", 1, " - ", r)
            print("p = ", p)

            iteration = 0

            while (x > y):
                iteration += 1  # debugging
                print("iteration:", iteration)
                y += 1

                # Mid-point inside or on the perimeter
                if p <= 0:
                    print("p <= 0")
                    print("p = ", p, " + ", 2 * y, " + ", 1)
                    p = p + 2 * y + 1
                    print("p = ", p)

                # Mid-point outside the perimeter
                else:
                    print("p > 0")
                    x -= 1
                    print("p = ", p, " + ", 2 * y, " - ", 2 * x, " + ", 1)
                    p = p + 2 * y - 2 * x + 1
                    print("p = ", p)

                #print("p = ", p)

                # All the perimeter points have already been printed
                if (x < y):
                    break

                # adding the generated point and its reflections
                points = np.append(points, np.array(
                    [x0 + x, y0 + y], dtype=np.int32))
                print("next point: ", points[-2:])
                points = np.append(points, np.array(
                    [x0 - x, y0 + y], dtype=np.int32))
                points = np.append(points, np.array(
                    [x0 + x, y0 - y], dtype=np.int32))
                points = np.append(points, np.array(
                    [x0 - x, y0 - y], dtype=np.int32))

                # If the generated point is on the line x = y then
                # the perimeter points have already been added
                if (x != y):
                    points = np.append(points, np.array(
                        [x0 + y, y0 + x], dtype=np.int32))
                    #print("next point: ", points[-2:])
                    points = np.append(points, np.array(
                        [x0 - y, y0 + x], dtype=np.int32))
                    points = np.append(points, np.array(
                        [x0 + y, y0 - x], dtype=np.int32))
                    points = np.append(points, np.array(
                        [x0 - y, y0 - x], dtype=np.int32))

            return points.reshape(-1, 2)
