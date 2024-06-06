from boolean_operations import *

def build_table(variables: list[set], post_variables: list[set]) -> dict:
    table = {}

    for constituent in variables:
        implicants = [implicant for implicant in post_variables if implicant.issubset(constituent)]
        table[tuple(constituent)] = delete_duplicates(implicants)

    return table

def calculate_minimization(log_form: str) -> str:
    implicants = get_variables(log_form)
    formula_type = get_formula_type(log_form)

    print("Склеивание:")
    post_variables = gluing(implicants, is_print=True)
    post_variables = delete_extra(post_variables)

    print("Удаление лишних импликант:")
    print(post_variables)

    return get_normal_form(post_variables, formula_type)

def table_minimization(log_form: str) -> str:
    implicants = get_variables(log_form)
    formula_type = get_formula_type(log_form)

    print("Склеивание:")
    post_variables = gluing(implicants, is_print=True)
    table = build_table(implicants, post_variables)

    print("Таблица импликант:")
    for key, value in table.items():
        print(f"{key}: {value}")

    minimum_variables = [implicant for key in table for implicant in table[key] if len(table[key]) == 1]
    minimum_variables = delete_duplicates(minimum_variables)

    print("Удаление лишних импликант:")
    print(minimum_variables)

    return get_normal_form(minimum_variables, formula_type)

def carno_minimization(log_form: str) -> str:
    implicants = get_variables(log_form)
    formula_type = get_formula_type(log_form)

    post_variables = gluing(implicants)
    post_variables = delete_extra(post_variables)

    return get_normal_form(post_variables, formula_type)

def bin_sign_to_dec(bin_sign: str) -> int:
    dec = 0
    for i in range(len(bin_sign)):
        dec += 2 ** (-i + len(bin_sign) - 1) * int(bin_sign[i])
    return dec

def carno_map(formula_values, carno_values) -> list[dict[str, int]]:
    carno_map = []
    for value in carno_values:
        carno_map.append({value: formula_values[bin_sign_to_dec('0' + value)]})
    return carno_map 

def build_carno_map(truth_table):
    formula_values = list(map(lambda a: int(str(a[1])[-2]), truth_table))
    values_count = len(formula_values)

    match values_count:
        case 0: return None
        case 2: return {'0': formula_values[0], '1': formula_values[1]}
        case 4: return carno_map(formula_values, ['00', '01', '10', '11'])
        case 8: 
            values = ['000', '001', '011', '010', 
                      '100', '101', '111', '110']
            return carno_map(formula_values, values)
        case 16: 
            values = ['0000', '0001', '0011', '0010', 
                      '0100', '0101', '0111', '0110', 
                      '1100', '1101', '1111', '1110',
                      '1000', '1001', '1011', '1010']
            return carno_map(formula_values, values)

def print_carno_map(carno_map: list[dict[str, int]]):
    if not carno_map:
        print("Пустая карта Карно")
        return
    
    headers = []
    table = []
    
    for item in carno_map:
        for key, value in item.items():
            if len(key) > 2:
                row = key[:-2]
                col = key[-2:]
            else:
                row = key[0]
                col = key[1]
                
            if col not in headers:
                headers.append(col)
            
            found = False
            for tbl in table:
                if tbl['row'] == row:
                    tbl[col] = value
                    found = True
                    break
            
            if not found:
                table.append({'row': row, col: value})
    
    headers = sorted(headers)
    table = sorted(table, key=lambda x: x['row'])
    
    print("   " + " ".join(headers))
    for row in table:
        line = row['row'] + "  "
        for col in headers:
            if col in row:
                line += str(row[col]) + "  "
            else:
                line += "0  "
        print(line)
