import math


def planar(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    p = float((a + b + c) / 2)
    return float(math.sqrt(p * (p - a) * (p - b) * (p - c)))


def side_length(x1, x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def sides_count(a, b, c):
    sides = [side_length(a[0], a[1], b[0], b[1]),
             side_length(a[0], a[1], c[0], c[1]),
             side_length(b[0], b[1], c[0], c[1])]
    return planar(sides)


def main():
    d = int(input())
    if d < 1 or d > 1000:
        exit(1)
    X = list(map(int, input().split()))
    if X[0] < -1000 or X[0] > 1000 or X[1] < -1000 or X[1] > 1000:
        exit(1)
    A = [0, 0]
    B = [d, 0]
    C = [0, d]
    points = [X, A, B, C]
    for i in range(1, len(points)):
        if X[0] == points[i][0] and X[1] == points[i][1]:
            return 0
    


if __name__ == '__main__':
    print(main())



    main_triangle = sides_count(points['A'], points['B'], points['C'])
    first_triangle = sides_count(points['A'], points['B'], points['X'])
    second_triangle = sides_count(points['A'], points['X'], points['C'])
    third_triangle = sides_count(points['X'], points['B'], points['C'])
    if main_triangle < first_triangle + second_triangle + third_triangle:


