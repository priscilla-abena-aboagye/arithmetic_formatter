def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        raise ValueError('Error: Too many problems')
    operator = ["+", "-"]
    if operator not in ["+", "-"]:
        raise ValueError("Error: Operator must be '+' or '-'.")

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')