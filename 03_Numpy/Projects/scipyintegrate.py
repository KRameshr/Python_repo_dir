import scipy.integrate as intg

# 1. Define the function you want to integrate: f(x) = x^2
def integrad(x):
    return x**2

# 2. Perform the integration (quad stands for Quadrature)
# Parameters: (function, start_point, end_point)
# This calculates the area under x^2 from 0 to 1
ans, error = intg.quad(integrad, 0, 1)

print(f"The integral of x^2 from 0 to 1 is: {ans:.4f}")
print(f"The estimated error in calculation is: {error}")

import scipy.integrate as intg

# 1. Define the function: f(x, y) = x * y
def f_2d(y, x):
    return x * y

# 2. Integrate over a rectangle: 
# x goes from 0 to 2
# y goes from 0 to 1
# Note: dblquad expects the order (func, x_start, x_end, y_start, y_end)
ans, error = intg.dblquad(f_2d, 0, 2, 0, 1)

print(f"2D Integral (Area/Volume) result: {ans:.4f}")

# 1. Define the function: f(x, y, z) = x + y + z
def f_3d(z, y, x):
    return x + y + z

# 2. Integrate over a cube:
# x: 0 to 1 | y: 0 to 1 | z: 0 to 1
ans, error = intg.tplquad(f_3d, 0, 1, 0, 1, 0, 1)

print(f"3D Integral (Triple) result: {ans:.4f}")