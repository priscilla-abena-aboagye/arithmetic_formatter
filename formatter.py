def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    first = ""
    second = ""
    dash = ""
    answer = ""

    for problem in problems:
        parts = problem.split()

        num1, operators, num2 = parts

        operators = ["+", "-"]

        if operators not in operators:
            return "Error: Operator must be '+' or '-'."
    
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'


        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(num1), len(num2)) + 1


 
        

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')