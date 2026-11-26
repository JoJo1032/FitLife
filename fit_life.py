"""Модуль для расчета ИМТ и нормы воды."""


WATER_PER_KG = 30
ML_PER_LITER = 1000

MIN_USER_AGE = 1
MAX_USER_AGE = 120

MIN_USER_HEIGHT = 0.5
MAX_USER_HEIGHT = 2.5

MIN_USER_WEIGHT = 10
MAX_USER_WEIGHT = 300


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
            if MIN_USER_AGE <= user_age <= MAX_USER_AGE:
                return user_age
            print(
                f"Ошибка: возраст должен быть в диапазоне от {MIN_USER_AGE} "
                f"до {MAX_USER_AGE} лет.")
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")


def get_valid_weight():
    """Запрашивает и проверяет корректность веса."""
    while True:
        try:
            user_weight = float(input("Введите ваш вес в кг (пример, 70.5): "))
            if MIN_USER_WEIGHT <= user_weight <= MAX_USER_WEIGHT:
                return user_weight
            print(
                f"Ошибка: вес должен быть в пределах от {MIN_USER_WEIGHT} "
                f"до {MAX_USER_WEIGHT} кг.")
        except ValueError:
            print("Ошибка: пожалуйста, введите число (можно с точкой).")


def get_valid_height():
    """Запрашивает и проверяет корректность роста."""
    while True:
        try:
            user_height = float(input("Введите рост в метрах (пример 1.8): "))
            if MIN_USER_HEIGHT <= user_height <= MAX_USER_HEIGHT:
                return user_height
            print(
                f"Ошибка: рост должен быть в пределах от {MIN_USER_HEIGHT} "
                f"до {MAX_USER_HEIGHT} метров.")
        except ValueError:
            print("Ошибка: пожалуйста, введите число (можно с точкой).")


def get_valid_user_name():
    """Запрашивает и проверяет корректность имени."""
    while True:
        try:
            user_name = input("Введите ваше имя: ").strip()
            if not user_name or any(char.isdigit() for char in user_name):
                print("Имя не может быть пустым и без чисел.")
            else:
                return user_name
        except ValueError:
            print("Ошибка: имя не должно состоять только из чисел.")


def main():
    """Основная логика программы."""
    print("---------------FitLife---------------\n")
    user_name = get_valid_user_name()
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
