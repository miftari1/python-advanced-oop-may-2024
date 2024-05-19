queries_stack = []
number_of_lines = int(input())
for _ in range(number_of_lines):
    command = input()
    if command == '2':
        if queries_stack:
            queries_stack.pop()
    elif command == '3':
        if queries_stack:
            print(max(queries_stack))
    elif command == '4':
        if queries_stack:
            print(min(queries_stack))
    elif "1" in command:
        command_elements = command.split()
        number = int(command_elements[1])
        queries_stack.append(number)
print(*reversed(queries_stack), sep=', ')

