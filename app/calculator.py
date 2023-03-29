import operator


math_operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def calculate(math_operator, a, b):
    if math_operator not in math_operators:
        raise TypeError('{} is an illegal operator'.format(math_operator))
    return math_operators[math_operator](a, b)


def main():
    first_number = int(input('First number: '))
    math_operator = input(
        'Operator ({}): '.format(''.join(math_operators.keys())))
    second_number = int(input('Second number: '))
    print(calculate(math_operator, first_number, second_number))


if __name__ == "__main__":
    main()
