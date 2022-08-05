# Predefined Functions
check_digit = lambda operand: operand.isdigit()
str_exec = lambda res: eval(res)
less_than_five = lambda less: len(less) < 5 

# User_Defined Funtions
def arithmetic_arranger(test_list: list, state = False):
    
    # Resuls State
    assertion_checker = ''
    
    # First Exception = Too Many Problems.
    if len(test_list) > 5:
        assertion_checker = "Error: Too many problems."
        return assertion_checker

    # Second Exception = Error: Operator must be '+' or '-'.
    all_operator = []
    for problem in test_list: operator = problem.split()[1]; all_operator.append(operator)
    if set(all_operator) != {'+', '-'} and len(set(all_operator)) > 2: 
        assertion_checker = "Error: Operator must be '+' or '-'."
        return assertion_checker

    # Third Exception = Numbers must only contain digits.
    all_operand = []
    for operand in test_list: operand = operand.split(); all_operand.extend([operand[0], operand[2]])
    if not all(map(check_digit, all_operand)):
        assertion_checker = "Error: Numbers must only contain digits."
        return assertion_checker

    # Fourth Exception = Numbers cannot be more than four digits.
    if not all(map(less_than_five, all_operand)):
        assertion_checker = "Error: Numbers cannot be more than four digits."
        return assertion_checker


    # Contruct the template
    exact_result = list(map(str_exec, test_list))
    
    # First Row
    first_row = ''; get_dash = ''; get_solutions = ''
    for first in range(0, len(all_operand), 2):
        first_width = max(len(all_operand[first]), len(all_operand[first + 1])) + 2
        first_row += str(all_operand[first]).rjust(first_width)
        get_dash += '-' * first_width
        get_solutions += str(exact_result[first // 2]).rjust(first_width)

        if first != len(all_operand) - 2:
            first_row += ' ' * 4
            get_dash += ' ' * 4
            get_solutions += ' ' * 4            

    #Second Row
    second_row = ''
    for second in range(1, len(all_operand), 2):
        second_width = max(len(all_operand[second - 1]), len(all_operand[second])) + 1
        second_row += all_operator[second // 2]
        second_row += str(all_operand[second]).rjust(second_width)
        if second != len(all_operand) - 1:
            second_row += ' ' * 4

    # Append depends of the state condition
    state_true = [first_row, second_row, get_dash, get_solutions]
    state_false = [first_row, second_row, get_dash]

    # return assertion_checker
    if state == True: assertion_checker = '\n'.join(res for res in state_true)
    else: assertion_checker = '\n'.join(res for res in state_false)
    return assertion_checker