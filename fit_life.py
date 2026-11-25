"""Модуль для расчета ИМТ и нормы воды."""


WATER_PER_KG = 30
ML_PER_LITER = 1000


def calculate_bmi(weight, height):
    """Вычисляет индекс массы тела."""
    return round(weight / (height ** 2), 1)


def calculate_water_norm(weight):
    """Вычисляет норму воды в день."""
    return round((weight * WATER_PER_KG) / ML_PER_LITER, 2)


def get_valid_age():
    """Запрашивает и проверяет корректность возраста."""
    while True:
        try:
            user_age = int(input("Введите ваш возраст: "))
            if 0 < user_age < 120:
                return user_age
            print("Ошибка: возраст должен быть в диапазоне от 1 до 119 лет.")
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")


def get_valid_weight():
    """Запрашивает и проверяет корректность веса."""
    while True:
        try:
            user_weight = float(input("Введите ваш вес в кг (пример, 70.5): "))
            if 10 <= user_weight <= 300:
                return user_weight
            print("Ошибка: вес должен быть в пределах от 10 до 300 кг.")
        except ValueError:
            print("Ошибка: пожалуйста, введите число (можно с точкой).")


def get_valid_height():
    """Запрашивает и проверяет корректность роста."""
    while True:
        try:
            user_height = float(input("Введите рост в метрах (пример 1.8): "))
            if 0.5 <= user_height <= 2.5:
                return user_height
            print("Ошибка: рост должен быть в пределах от 0.5 до 2.5 метров.")
        except ValueError:
            print("Ошибка: пожалуйста, введите число (можно с точкой).")


def main():
    """Основная логика программы."""
    print("---------------FitLife---------------\n")

    user_name = input("Введите ваше имя: ").strip()
    while not user_name or user_name.isdigit():
        if not user_name:
            print("Имя не может быть пустым.")
        else:
            print("Ошибка: имя не должно состоять только из чисел.")
        user_name = input("Введите ваше имя: ").strip()

    user_age = get_valid_age()
    user_weight = get_valid_weight()
    user_height = get_valid_height()

    bmi = calculate_bmi(user_weight, user_height)
    water = calculate_water_norm(user_weight)

    print("\n----------Сформировал отчет по вашим данным----------\n")
    print(f"Пользователь {user_name} ({user_age} г.)")
    print(f"Ваш Индекс Массы тела составляет: {bmi}")
    print(f"Рекомендуемая норма воды: {water} л. в день")
    print("\nРасчет окончен. Будьте здоровы!")


if __name__ == "__main__":
    main()
