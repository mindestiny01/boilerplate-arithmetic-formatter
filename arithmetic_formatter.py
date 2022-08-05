
def arithmetic_formmatter(equation: list, state = False):
    normal_situation = ''
    if len(equation) >= 5:
        print("Error: Too Many Problems")
    operator = list(map(lambda oper: oper.split()[1], equation))
    if set(equation) != {'+', '-'} and len(set(equation)) != 2:
        pass


