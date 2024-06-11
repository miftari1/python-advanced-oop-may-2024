def grocery_store(**kwargs):
    alphabetically_sorted = sorted(kwargs.items())

    completely_sorted = sorted(alphabetically_sorted, key=lambda kv: (kv[1], len(kv[0]), -ord(kv[0][0])), reverse=True)

    result = [f'{name}: {quantity}' for name, quantity in completely_sorted]
    return '\n'.join(result)
