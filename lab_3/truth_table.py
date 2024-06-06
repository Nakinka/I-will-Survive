class Validator:
    @staticmethod
    def brackets_check(exp: str) -> bool:
        stack = []

        for symbol in exp:
            if symbol == "(":
                stack.append(symbol)
            elif symbol == ")":
                if not stack:
                    return False
                stack.pop()
        return not stack

    @staticmethod
    def syntax_check(exp: str) -> bool:
        index = 0

        def expression():
            nonlocal index
            result = term()
            while index < len(exp) and exp[index] in ('&', '|'):
                op = exp[index]
                index += 1
                term_val = term()
                if op == '&':
                    result = result and term_val
                elif op == '|':
                    result = result or term_val
            return result

        def term():
            nonlocal index
            result = factor()
            if index < len(exp) and exp[index] == '!':
                index += 1
                result = not factor()
            return result

        def factor():
            nonlocal index
            if exp[index] == '(':
                index += 1
                result = expression()
                if exp[index] != ')':
                    return False
                index += 1
                return result
            elif exp[index] in 'abcd':
                index += 1
                return True
            else:
                return False

        return expression() and index == len(exp)

    @staticmethod
    def is_valid(exp: str) -> bool:
        return Validator.syntax_check(exp) and Validator.brackets_check(exp)


def parse_brackets(open_bracket_index: int, exp: str) -> str:

    brackets: int = 1
    exp = exp[open_bracket_index + 1:]
    result = ""

    for symbol in str(exp):

        if symbol == '(': brackets += 1
        elif symbol == ')': brackets -= 1

        if not brackets: break

        result += symbol

    return result

class LogicalOperation():

    def __init__(self, operation: chr, right_op=None, left_op=None):

        self.__operation = operation
        self.__right_operand = right_op
        self.__left_operand = left_op

    def get_operation(self): return self.__operation
    def get_right_operand(self): return self.__right_operand
    def get_left_operand(self): return self.__left_operand

    def __str__(self):

        left_op = str(self.get_left_operand())
        operation = str(self.get_operation())
        right_op = str(self.get_right_operand())

        if left_op == "None": left_op = ''
        elif isinstance(left_op, LogicalOperation):
            left_op = str(left_op)
        if isinstance(right_op, LogicalOperation):
            right_op = str(right_op)

        return f"{left_op}{operation}{right_op}"


def parse_exp(exp: str) -> LogicalOperation:

    i = 0
    while i < len(exp):
        match exp[i]:
            case 'a'|'b'|'c'|'d':
                logical_operations = exp[i]
                i += 1
            
            case '!': 
                if exp[i + 1] != '(':
                    logical_operations = LogicalOperation('!', exp[i + 1])
                    i += 2
                    continue
                
                bracket_exp = parse_brackets(i + 1, exp)
                logical_operations = LogicalOperation('!', parse_exp(bracket_exp))
                i += len(bracket_exp) + 3
                continue 
                
            case '|'|'&':
                if exp[i + 1] == '(': 
                    bracket_exp = parse_brackets(i + 1, exp)
                    logical_operations = LogicalOperation(exp[i], parse_exp(bracket_exp),
                                                          logical_operations)
                    i += len(bracket_exp) + 3
                    continue

                elif exp[i + 1] == '!' and exp[i + 2] != '(':
                    logical_operations = LogicalOperation(exp[i], parse_exp(exp[i + 1:i + 3]),
                                                          logical_operations)
                    i += 3
                    continue
                
                elif exp[i + 1] == '!' and exp[i + 2] == '(':
                    bracket_exp = parse_brackets(i + 2, exp)
                    logical_operations = LogicalOperation(exp[i], parse_exp(f"!({bracket_exp})"),
                                                          logical_operations)
                    i += len(bracket_exp) + 3
                    continue

                logical_operations = LogicalOperation(exp[i], exp[i + 1], logical_operations)
                i += 2

            case '(': 
                if not i:
                    bracket_exp = parse_brackets(i, exp)
                    logical_operations = parse_exp(bracket_exp)
                    i += len(bracket_exp) + 2
    
    return logical_operations


class Logicalexp:

    def __init__(self, exp: str):

        logical_exp = exp.replace("->", '→')


        self.__variables = sorted(list(set(filter(lambda a: a.isalpha(), logical_exp))))
        self.__logical_operations = parse_exp(logical_exp)


    def __str__(self): return self.__exp

    def get_logical_operations(self): return self.__logical_operations
    def get_variables(self): return self.__variables

    
def adding(bin1: str, bin2: str) -> str:
    result = ""
    carry = False

    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)

    for i in range(max_len - 1, 0, -1):

        if (bin1[i] == "1" and bin2[i] == "1"):
            
            if carry:
                result = "1" + result
            else:
                result = "0" + result
                carry = True
                continue

        elif (bin1[i] == "0" and bin2[i] == "0"):

            if carry:
                result = "1" + result
                carry = False
            else: result = "0" + result 

        else:

            if carry:
                result = "0" + result
            else: result = "1" + result 

    result = result.zfill(31)

    return result

def values_generator(var_count: int):

    values = "0" * var_count

    while values != "1" * var_count:

        yield list(map(lambda bit: int(bool(int(bit))), values))
        values = adding('0' + values, "1".zfill(var_count + 1))[-var_count:]
    
    else: yield list(map(lambda bit: int(bool(int(bit))), values))

def solve_tree(logical_tree: LogicalOperation, variables: dict, operations: dict={}): 

    if isinstance(logical_tree, str):
        return variables[logical_tree], operations

    if not logical_tree.get_left_operand():
        str_op = str(logical_tree)
        operations[str_op] = int(not solve_tree(logical_tree.get_right_operand(), variables, operations)[0])
        return operations[str_op], operations

    left_value = solve_tree(logical_tree.get_left_operand(), variables, operations)[0]
    right_value = solve_tree(logical_tree.get_right_operand(), variables, operations)[0]
    str_op = str(logical_tree)

    match logical_tree.get_operation():
        case '&': 
            operations[str_op] = int(left_value and right_value)
            return operations[str_op], operations
        case '|': 
            operations[str_op] = int(left_value or right_value)
            return operations[str_op], operations

        
    return operations

def get_truth_table(logical_expr: Logicalexp):

    logic_vars = logical_expr.get_variables()

    list_values = values_generator(len(logic_vars))

    for values in list_values:
        variables = dict(zip(logic_vars, values))
        yield variables, solve_tree(logical_expr.get_logical_operations(), variables)[1]