def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'
    first = ""
    second = ""
    dash = ""
    answer = ""

    for i, problem in enumerate(problems):
        parts = problem.split()

        num1, operators, num2 = parts

        if operators in ["+", "-"]:
            pass
        else:
            return "Error: Operator must be '+' or '-'."
    
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'


        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(num1), len(num2)) + 2

        space = "    " if i < len(problems) - 1 else ""

        first += num1.rjust(width) + space

        second += operators + " " + num2.rjust(width - 2) + space

        dash += "-" * width + space

        if show_answers:
            answers = str(eval(num1 + operators + num2))
            answer += answers.rjust(width) + space

    arranged = first.rstrip() + "\n" + second.rstrip() + "\n" + dash.rstrip()

    if show_answers:
        arranged += "\n" + answer.rstrip()


    return arranged

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
