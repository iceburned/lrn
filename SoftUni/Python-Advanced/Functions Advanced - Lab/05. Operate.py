def operate(operator, *args):
    def add(x, *args):
        return x + sum(y for y in args)

    def substract(x, *args):
            return x + sum(-y for y in args)

    def multiply(*args):
        result = 1
        for value in args:
            result *= value
        return result

    def devide(x, *args):
        result = x
        for value in args:
            result /= value
        return result

    if operator == "+":
        return add(*args)
    elif operator == "-":
        return substract(*args)
    elif operator == "*":
        return multiply(*args)
    elif operator == "/":
        return devide(*args)



print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
