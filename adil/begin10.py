# Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.

a = float(input("Введите первое ненулевое число: "))
b = float(input("Введите второе ненулевое число: "))

sum_squares = a**2 + b**2
diff_squares = a**2 - b**2
prod_squares = a**2 * b**2
quot_squares = a**2 / b**2

print("Сумма квадратов:", sum_squares)
print("Разность квадратов:", diff_squares)
print("Произведение квадратов:", prod_squares)
print("Частное квадратов:", quot_squares)