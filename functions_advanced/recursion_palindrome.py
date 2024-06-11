def palindrome(word, index):
    first_index = index
    last_index = -(index + 1)
    if first_index == len(word)//2:
        return f'{word} is a palindrome'
    if word[first_index] == word[last_index]:
        return palindrome(word, index + 1)
    else:
        return f'{word} is not a palindrome'


