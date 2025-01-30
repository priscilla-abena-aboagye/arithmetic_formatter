def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    operators = ["+", "-"]
    if operators not in operators:
        return "Error: Operator must be '+' or '-'."
    for number in arithmetic_arranger:
        pass
    else:
        return "Error: Operator must be '+' or '-'."
        

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')