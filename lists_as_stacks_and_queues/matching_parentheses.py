parentheses_stack = []
expression = input()

for index in range(len(expression)):
    if expression[index] == "(":
        parentheses_stack.append(index)
    elif expression[index] == ")":
        print(expression[parentheses_stack.pop():index + 1])