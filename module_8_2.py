
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for number in numbers:
            try:
                result += number
            except TypeError as exc:
                incorrect_data += 1
                print(f'{exc} Некорректный тип данных для подсчёта суммы - {number}')
        return ((result, incorrect_data))
    except TypeError as exc:
        print(f'{exc} В numbers записан некорректный тип данных')



def calculate_average(numbers):
    try:
        sum_numbers = personal_sum(numbers)
        try:
            average = round(sum_numbers[0] / (len(numbers) - sum_numbers[1]), 2)
        except ZeroDivisionError as exc:
            print(f'{exc} Корректных значений в коллекции нет или она пуста')
            average = 0

        return average
    except TypeError as exc:
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
print(f'Результат 5: {calculate_average([])}')

