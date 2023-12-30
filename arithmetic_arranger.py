def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"top": [], "bottom": [], "operator": [], "line": []}

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        arranged_problems["top"].append(num1.rjust(width))
        arranged_problems["bottom"].append(operator + num2.rjust(width - 1))
        arranged_problems["operator"].append(operator.ljust(1))
        arranged_problems["line"].append('-' * width)

    result = ""

    for i in range(len(arranged_problems["top"])):
        result += arranged_problems["top"][i] + '    '

    result += '\n'

    for i in range(len(arranged_problems["bottom"])):
        result += arranged_problems["operator"][i] + arranged_problems["bottom"][i][1:] + '    '

    result += '\n'

    for i in range(len(arranged_problems["line"])):
        result += arranged_problems["line"][i] + '    '

    if show_answers:
        result += '\n'

        answers = [str(eval(problem)) for problem in problems]
        for answer in answers:
            width = max(len(answer), len(arranged_problems["line"][0]))
            result += answer.rjust(width) + '    '

    return result.rstrip()


