from matrix_operations import MatrixOperations
from logical_operations import LogicalOperations
from matrix_logical_operations import MatrixLogicalOperations
from address_operations import AddressOperations
from matching_operations import MatchingOperations
from interval_search import IntervalSearch

def print_menu():
    print("1. Записать слово в столбец")
    print("2. Выполнить логическую операцию и вставить результат")
    print("3. Найти слово в матрице")
    print("4. Вывести матрицу")
    print("5. Поиск значений в интервале")
    print("6. Добавить поля для сопоставления v")
    print("7. Вывести адреса столбцов")
    print("8. Выйти")

def write_word_to_column(matrix_operations):
    column_index = int(input("Введите индекс столбца: "))
    word = input("Введите слово для записи: ")
    matrix_operations.write_word_to_column(word, column_index)
    print("Слово записано в столбец.")

def perform_logical_operation_and_paste(matrix_logical_operations):
    index1 = int(input("Введите индекс 1: "))
    index2 = int(input("Введите индекс 2: "))
    target_column_index = int(input("Введите индекс целевого столбца: "))

    print("Выберите логическую операцию:")
    print("1. Дизъюнкция")
    print("2. Пирс")
    print("3. Конъюнкция с отрицанием")
    print("4. Отрицание с дизъюнкцией")

    choice = int(input("Введите выбор (1/2/3/4): "))

    operation_map = {
        1: LogicalOperations.perform_disjunction,
        2: LogicalOperations.perform_pierce,
        3: LogicalOperations.perform_conjunction_negation,
        4: LogicalOperations.perform_negation_disjunction
    }

    if choice not in operation_map:
        print("Неверный выбор. Пожалуйста, выберите допустимый вариант.")
        return

    operation_func = operation_map[choice]
    matrix_logical_operations.apply_and_paste(index1, index2, target_column_index, operation_func)

    print("Логическая операция выполнена и результат вставлен.")

def find_word(matrix_operations):
    word = input("Введите искомое слово: ")
    result = matrix_operations.find_word(word)
    if result:
        print(f"Слово найдено в столбце с индексом {result[0]}")
    else:
        print("Слово не найдено.")

def search_values_in_interval(matrix_operations):
    lower_bound = input("Введите нижнюю границу: ")
    upper_bound = input("Введите верхнюю границу: ")
    result = IntervalSearch.search_values_in_interval(matrix_operations, lower_bound, upper_bound)
    print("Индексы слов в интервале:", result)

def add_fields_for_matching_v(matrix_operations):
    v_key = input("Введите ключ v: ")
    matrix_operations = MatchingOperations.add_fields_for_matching_v(matrix_operations, v_key)
    print("Поля, добавленные для сопоставления v.")

def print_addresses_of_columns(matrix_operations):
    number = int(input("Введите номер: "))
    AddressOperations.adres_row(matrix_operations.matrix, number)

def main():
    matrix_operations = MatrixOperations([[0 for _ in range(16)] for _ in range(16)])
    matrix_logical_operations = MatrixLogicalOperations(matrix_operations)

    while True:
        print_menu()
        choice = input("Введите ваш выбор: ")

        if choice == "1":
            write_word_to_column(matrix_operations)
        elif choice == "2":
            perform_logical_operation_and_paste(matrix_logical_operations)
        elif choice == "3":
            find_word(matrix_operations)
        elif choice == "4":
            matrix_operations.print_matrix()
        elif choice == "5":
            search_values_in_interval(matrix_operations)
        elif choice == "6":add_fields_for_matching_v(matrix_operations)
        elif choice == "7":
            print_addresses_of_columns(matrix_operations)
        elif choice == "8":
            print("Выход...")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

if __name__ == "__main__":
    main()