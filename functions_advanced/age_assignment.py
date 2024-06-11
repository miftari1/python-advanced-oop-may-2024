def age_assignment(*names, **kwargs):
    # Create a dictionary which stores the names and ages
    names_with_age = {}
    # Assign each first letter of name with it's corresponding letter in the key-value pairs
    for name in names:
        first_letter = name[0]
        if first_letter in kwargs:
            names_with_age[name] = kwargs[first_letter]

    # Prepare the information in the dict for the final output
    result = [f'{name} is {age} years old.' for name, age in sorted(names_with_age.items())]

    return '\n'.join(result)
