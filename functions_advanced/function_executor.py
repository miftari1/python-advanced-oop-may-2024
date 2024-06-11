def func_executor(*args):
    # Create an empty list which will store the functions' names with their results
    results = []
    # Assign the function's name and arguments of each tuple in the argument to a variables
    for arg in args:
        func_name = arg[0]
        arguments = arg[1]
        # Call the current function and assign it's result to a variable
        result = func_name(*arguments)
        # Append function's name and result to the 'results' list in the needed format
        results.append(f'{func_name.__name__} - {result}')

    # Return each element on a new line
    return '\n'.join(results)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(

(make_upper, ("Python", "softUni")),

(make_lower, ("PyThOn",)),

))