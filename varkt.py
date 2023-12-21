from math import pi


def HohmannTransferOrbit():
    separator()
    G = 6.67 * 10 ** (-11)
    print('Математическая модель команды "Ракета Тьюринга".')
    separator()
    print('Все величины внутри программы рассчитываются в единицах Си.')
    separator()
    print("Введём данные для первой планеты.", end='\n\n')
    v1 = 1000 * \
        float(input("Введите значение средней скорости первой планеты в км/c: "))
    r1 = 1000 * \
        float(input("Введите значение среднего радиуса орбиты первой планеты в км: "))
    f01 = pi * float(input(
        "Введите значение начального отклонения угла от оси x в градусах для первой планеты: ")) / 180
    m1 = 10 ** 24 * \
        float(input("Введите массу первой планеты в 10 ** 24 кг: "))
    separator()
    print("Введём данные для второй планеты.", end='\n\n')
    v2 = 1000 * \
        float(input("Введите значение средней скорости второй планеты в км/c: "))
    r2 = 1000 * \
        float(input("Введите значение среднего радиуса орбиты второй планеты в км: "))
    f02 = pi * float(input(
        "Введите значение начального отклонения угла от оси x в градусах для второй планеты: ")) / 180
    separator()
    print("Введём данные для третьей планеты.", end='\n\n')
    v3 = 1000 * \
        float(input("Введите значение средней скорости третьей планеты в км/c: "))
    r3 = 1000 * \
        float(input("Введите значение среднего радиуса орбиты третьей планеты в км: "))
    f03 = pi * float(input(
        "Введите значение начального отклонения угла от оси x в градусах для третьей планеты: ")) / 180
    separator()
    separator()
    print('Промежуточные расчёты:')
    print('Необходимый угол для осуществления Гомановского перехода между 1 и 2 планетой равен: ', end='')
    delta_f12 = pi * (1 - (1 / (2 * 2 ** 0.5)) * ((r1 / r2 + 1) ** 3) ** 0.5)
    print(f'{(delta_f12 * 180 / pi):.5f}')
    print('Необходимый угол для осуществления Гомановского перехода между 2 и 3 планетой равен: ', end='')
    delta_f23 = pi * (1 - (1 / (2 * 2 ** 0.5)) * ((r2 / r3 + 1) ** 3) ** 0.5)
    print(f'{(delta_f23 * 180 / pi):.5f}')
    w1 = v1 / r1
    print("Угловая скорость первой планеты равна: ", f'{w1:.10f}')
    w2 = v2 / r2
    print("Угловая скорость второй планеты равна: ", f'{w2:.10f}')
    w3 = v3 / r3
    print("Угловая скорость третьей планеты равна: ", f'{w3:.10f}')
    delta_t12 = (((r1 + r2) ** 3 / (8 * G * m1)) ** 0.5) * pi
    print("Время первого Гомановского перехода в днях составляет: ",
          f'{delta_t12/(3600*24):.10}')
    t01 = (delta_f12 - (f01 - f02))/(w2 - w1)
    t02 = (delta_f23 - (f03 - f02)) / (w3 - w2) - delta_t12
    separator()
    print("Время (в днях), которое необходимо выждать до первого перехода: ",
          f'{t01/(3600*24):.20f}')
    print("Это время должно совпадать с временем: ")
    print(f'{t02/(3600*24):.20f}')
    print("Если это время приблизительно совпадает, то из данного положения можно совершить переход Гомана.")


def separator():
    print('-' * 105)


def main():
    HohmannTransferOrbit()


if __name__ == '__main__':
    main()

# ---------------------------------------------------------------------------------------------------------
# Математическая модель команды "Ракета Тьюринга".
# ---------------------------------------------------------------------------------------------------------
# Все величины внутри программы рассчитываются в единицах Си.
# ---------------------------------------------------------------------------------------------------------
# Введём данные для первой планеты.
#
# Введите значение средней скорости первой планеты в км/c: 29.765
# Введите значение среднего радиуса орбиты первой планеты в км: 149600000
# Введите значение начального отклонения угла от оси x в градусах для первой планеты: 30
# Введите массу первой планеты в 10 ** 24 кг: 5.9736
# ---------------------------------------------------------------------------------------------------------
# Введём данные для второй планеты.
#
# Введите значение средней скорости второй планеты в км/c: 6.81
# Введите значение среднего радиуса орбиты второй планеты в км: 30670000000
# Введите значение начального отклонения угла от оси x в градусах для второй планеты: 45
# ---------------------------------------------------------------------------------------------------------
# Введём данные для третьей планеты.
#
# Введите значение средней скорости третьей планеты в км/c: 5.44
# Введите значение среднего радиуса орбиты третьей планеты в км: 4498472000
# Введите значение начального отклонения угла от оси x в градусах для третьей планеты: 60
