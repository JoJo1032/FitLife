"""Модуль для расчета ИМТ и нормы воды."""

WATER_PER_KG = 30
ML_PER_LITER = 1000


def calculate_bmi(weight, height):
    """Вычисляет индекс массы тела."""
    return round(weight / (height ** 2), 1)


def calculate_water_norm(weight):
    """Вычисляет норму воды в день."""
    return (weight * WATER_PER_KG) / ML_PER_LITER


def main():
    """Основная логика программы."""
    print("---------------FitLife---------------\n")
    user_name = input("Введите ваше имя: ")
    user_age = int(input("Введите ваш возраст: "))

    user_weight = float(input("Введите ваш вес (в кг)(пример 70.5): "))
    user_height = float(input("Введите ваш рост (в метрах)(пример 1.8): "))

    bmi = calculate_bmi(user_weight, user_height)
    water = calculate_water_norm(user_weight)

    print("\n---------------Сформировал отчет \
          по вашим данным---------------\n")
    print(f"Пользователь {user_name} ({user_age} г.)")
    print(f"Ваш Индекс Массы тела составляет: {bmi}")
    print(f"Рекомендуемая норма воды: {water} л. в день")
    print("\nРасчет окончен. Будьте здоровы!")


if __name__ == "__main__":
    main()
