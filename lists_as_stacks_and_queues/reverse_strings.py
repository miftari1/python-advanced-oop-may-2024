# Read an input string
text = list(input())
# Generate a list using a loop
reversed_order = [text.pop() for _ in range(len(text))]
# Output the list
print(''.join(reversed_order))