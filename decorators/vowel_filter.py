def vowel_filter(func):
    def wrapper():
        vowels = ['a', 'e', 'i', 'o', 'u']
        lst = func()
        new_lst = [letter for letter in lst if letter in vowels]
        return new_lst
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())