import re
firstRow = []
secondRow = []
thirdRow = []
solutionRow = []


def arithmetic_arranger(problems, *argv):
    firstRow.clear()
    secondRow.clear()
    thirdRow.clear()
    solutionRow.clear()
    numberOfProblems = len(problems)
    if numberOfProblems > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        try:
            firstNum, operator, secondNum = problem.split()
        except:
            return 'Error: Invalid formatting.'
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        if (not re.search('^[0-9]+$', firstNum)
                or not re.search('^[0-9]+$', secondNum)):
            return 'Error: Numbers must only contain digits.'
        if len(firstNum) > 4 or len(secondNum) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        # The real processing starts here
        output_handler(firstNum, operator, secondNum)
    # Output to console the compiled solutions
    finalStr = ''
    finalStr += '    '.join(firstRow) + '\n'
    finalStr += '    '.join(secondRow) + '\n'
    finalStr += '    '.join(thirdRow)
    if len(argv) == 1 and argv[0] == True:
        finalStr += '\n' + '    '.join(solutionRow)
    return finalStr


def output_handler(firstNum, operator, secondNum):
    firstLen = len(firstNum)
    secondLen = len(secondNum)
    # Find which of the 2 number length is larger and add 2
    # 1 for operator and 1 space between operator and number
    requiredLen = max(firstLen, secondLen) + 2
    # Pad them with spaces before adding them to the list
    firstRow.append(firstNum.rjust(requiredLen))
    secondRow.append(operator.ljust(requiredLen - secondLen) + secondNum)
    thirdRow.append('-' * requiredLen)
    # Calculate the solution
    try:
        if operator == '+':
            solution = int(firstNum) + int(secondNum)
        else:
            solution = int(firstNum) - int(secondNum)
    except:
        return 'Error: Invalid formatting.'
    solutionRow.append(str(solution).rjust(requiredLen))
