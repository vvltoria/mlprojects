try:
    from triangle import is_triangle_possible
except ImportError:
    print("yе найден файл 'triangle.py'.")
    print("yбедитесь, что оба файла (main.py и triangle.py) находятся в одном каталоге.")
    exit()

try:
    side1 = float(input("Введите длину первой стороны (a): "))
    side2 = float(input("Введите длину второй стороны (b): "))
    side3 = float(input("Введите длину третьей стороны (c): "))

    if is_triangle_possible(side1, side2, side3):
        print(f"да, треугольник со сторонами {side1}, {side2} и {side3} можно построить.")
    else:
        print(f"нет, треугольник со сторонами {side1}, {side2} и {side3} построить нельзя.")

except ValueError:
    print("\nвведено нечисловое значение.")