def get_variables(full_normal_form: str) -> list[set]:
    result = []
    variables = set()
    i = 0

    while i < len(full_normal_form):
        if full_normal_form[i] == '(':
            variables = set()
        elif full_normal_form[i] == ')':
            result.append(variables)
        elif full_normal_form[i] == '!':
            variables.add(full_normal_form[i:i + 2])
            i += 1
        elif full_normal_form[i].isalpha():
            variables.add(full_normal_form[i])
        i += 1

    return result

def get_normal_form(variables: list[set], form_type: chr) -> str:
    operations = ['|', '&'] if form_type == '|' else ['&', '|']
    sknf = ''

    for i, conjuct in enumerate(variables):
        sknf += '(' + operations[0].join(conjuct) + ')'
        if i + 1 != len(variables):
            sknf += operations[1]

    return sknf

def delete_duplicates(lst: list) -> list:
    result = []
    [result.append(item) for item in lst if item not in result]
    return result

def is_reciprocal(variables: set) -> bool:
    if len(variables) != 2:
        return False
    var1, var2 = variables
    return var1 == '!' + var2 or var2 == '!' + var1

def gluing(variables: list[set], is_print: bool = False) -> list[set]:
    if is_print:
        print(variables)

    processed_variables = []
    result = []
    flag = False

    for i in range(len(variables)):
        for j in range(i + 1, len(variables)):
            intersection = variables[i].intersection(variables[j])
            difference = variables[i].symmetric_difference(variables[j])
            if len(intersection) == len(variables[i]) - 1 and is_reciprocal(difference):
                result.append(intersection)
                processed_variables.extend([variables[i], variables[j]])
                flag = True

    result.extend(var for var in variables if var not in processed_variables)
    result = delete_duplicates(result)

    if flag:
        return gluing(result, is_print)
    return result

def delete_extra(post_variables: list[set]) -> list[set]:
    extras = []

    for implicant in post_variables:
        if len(implicant) == 1:
            continue
        for variables in post_variables:
            if implicant != variables and implicant.issubset(variables):
                extras.append(variables)

    return [el for el in post_variables if el not in extras]

def get_formula_type(log_form: str) -> chr:
    closebracket_index = log_form.find(')')
    if closebracket_index == len(log_form) - 1:
        return '|' if '|' in log_form else '&'
    return log_form[closebracket_index + 1]
