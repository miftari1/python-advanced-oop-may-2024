def concatenate(*strings, **kwargs):
    concatenated = ''
    # Concatenate all string arguments together
    for txt in strings:
        concatenated += txt

    # Check if each key from the keyword arguments is present in the concatenated text
    for key, value in kwargs.items():
        if key in concatenated:
            # Changes the subtext with the corresponding value
            concatenated = concatenated.replace(key, value)
    return ''.join(concatenated)


print(concatenate("Soft", "UNI", "Is", "Grate", "!",

UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons",

C="P", s="", java='Java'))