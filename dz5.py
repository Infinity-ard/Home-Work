class Calculator:
    @staticmethod
    def add(a, b):
        """Додавання"""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Віднімання"""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Множення"""
        return a * b

    @staticmethod
    def divide(a, b):
        """Ділення"""
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе!")
        return a / b


def wrapper(func):
    """Функція-обгортка для обробки винятків"""
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        result = func(a, b)
        print(f"Результат: {result}")
    except ValueError:
        print("Помилка: введіть коректні числа!")
    except ZeroDivisionError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")


def main():
    while True:
        print("\n=== Калькулятор ===")
        print("1. Додавання (+)")
        print("2. Віднімання (-)")
        print("3. Множення (*)")
        print("4. Ділення (/)")
        print("5. Вихід")

        choice = input("Оберіть дію (1-5): ")

        if choice == "1":
            wrapper(Calculator.add)
        elif choice == "2":
            wrapper(Calculator.subtract)
        elif choice == "3":
            wrapper(Calculator.multiply)
        elif choice == "4":
            wrapper(Calculator.divide)
        elif choice == "5":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")