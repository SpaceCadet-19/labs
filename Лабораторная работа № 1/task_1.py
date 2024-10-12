numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

sum_of_numbers_1 = sum(numbers[0:4]) # Сумма элементов с 0 по 3
sum_of_numbers_2 = sum(numbers[5:]) # сумма элементов с 5 до конечного
final_sum = sum_of_numbers_1 + sum_of_numbers_2 # сумма всех элементов

count_of_numbers = len(numbers) # длина списка
average = final_sum / count_of_numbers # ср. арифетическое
numbers[4] = average


print("Измененный список:", numbers)
