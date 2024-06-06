from minimization import *
from truth_table import  *

def main():
   
    print("Выберите действие:")
    print("1. Ввести готовую функцию в СКНФ или СДНФ")
    print("2. Написать свою функцию")
    
    choice = input("Введите номер действия: ")


    if choice == "1":
        function_type = input("Выберите тип функции (СДНФ или СКНФ): ").upper()
        if function_type == "СДНФ":
            print("Выберите функцию:")
            print("1. (a & b & c) | (a & !b & !c) | (!a & b & !c) | (!a & !b & c)")
            print("2. (a & b & c) | (a & b & !d) | (a & !c & d) | (!a & c & d)")
            print("3. (!a & !b & c) | (a & b & !d) | (a & !b & d) | (a & !b & d)" )
            function_choice = input("Введите номер функции: ")
            if function_choice == "1":
                logical_formula = "(a&b&c)|(a&!b&!c)|(!a&b&!c)|(!a&!b&c)"
            elif function_choice == "2":
                logical_formula = "(a&b&c)|(a&b&!d)|(a&!c&d)|(!a&c&d)"
            elif function_choice == "3":
                logical_formula = "(!a&!b&c)|(a&b&!d)|(a&!b&d)|(a&!b&d)"
            else:
                print("Некорректный выбор.")
                return
        elif function_type == "СКНФ":
            print("Выберите функцию:")
            print("1. (a | b | c) & (a | !b | !c) & (!a | b | !c) & (!a | !b | c)")
            print("2. (a | b | c) & (a | b | !d) & (a | !c | d) & (!a | c | d)")
            print("3. (!a | !b | c) & (a | b | !d) & (a | !b | d) & (a | !b | d)")
            function_choice = input("Введите номер функции: ")
            if function_choice == "1":
                logical_formula = "(a|b|c)&(a|!b|!c)&(!a|b|!c)&(!a|!b|c)"
            elif function_choice == "2":
                logical_formula = "(a|b|c)&(a|b|!d)&(a|!c|d)&(!a|c|d)"
            elif function_choice == "3":
                logical_formula = "(!a|!b|c)&(a|b|!d)&(a|!b|d)&(a|!b|d)"
            else:
                print("Некорректный выбор.")
                return
        else:
            print("Некорректный выбор.")
            return
    elif choice == "2":
        logical_formula = input("Введите свою логическую функцию: ")
    else:
        print("Некорректный выбор.")
        return
    
    print("\nМинимизация с использованием метода вычислений:")
    print(calculate_minimization(logical_formula))

    print("\nМинимизация с использованием метода таблицы-вычислений:")
    print(table_minimization(logical_formula))

    print("\nМинимизация с использованием метода Карно:")
    carno_map = build_carno_map(get_truth_table(Logicalexp(logical_formula)))
    print_carno_map(carno_map)
    print()
    print(carno_minimization(logical_formula))

if __name__ == "__main__":
    main()
