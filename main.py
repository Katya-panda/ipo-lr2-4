import math
#x = 2
#y = 3
#z = 0.5
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = float(input("Enter z: "))
root_x_3 = math.pow(x, 1 / 3)
x_pow_y_plus_2 = math.pow(x, y + 2)
sum_value = root_x_3 + x_pow_y_plus_2
sqrt_value = math.sqrt(10 * sum_value)
arcsin_z_squared = math.asin(z) ** 2
absolute_difference = abs(x - y)
beta = sqrt_value * (arcsin_z_squared - absolute_difference)
print("beta = ", beta)
