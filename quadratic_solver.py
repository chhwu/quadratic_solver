import math
print("It's Quadratic Solver!")
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

x = (b**2) - (4 * a * c)
if x < 0:
    print('No real roots.')
else:
    sqr_x = math.sqrt(x)
    y1 = (-b + sqr_x) / (2 * a)
    y2 = (-b - sqr_x) / (2 * a)
    if x == 0:
        print('One root: %.1f' % y1)
    else:
        print('Two roots: %.1f, %.1f' % (y1, y2))