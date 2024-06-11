def repeat_text(text, times):
    try:
        result = text * times
    except TypeError:
        return 'Variable times must be an integer'
    else:
        return result
