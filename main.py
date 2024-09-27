import math
def calculate_beta(x, y, z):
    beta = math.sqrt(10 * (math.pow(x, 1/3) + math.pow(x, y + 2))) * (math.asin(z) ** 2 - abs(x - y))
    return beta
def main():
    print("Введите значения для переменных x, y, z:")
    try:
        x = float(input("x: "))
        y = float(input("y: "))
        z = float(input("z (должен быть в пределах от -1 до 1 для arcsin): "))
        if z < -1 or z > 1:
            print("Ошибка: z должен быть в пределах от -1 до 1 для arcsin.")
            return
        beta = calculate_beta(x, y, z)
        print(f"Результат beta: {beta}")
    except ValueError:
        print("Ошибка: Пожалуйста, введите числовые значения.")
