def math_operations(*floats, a, s, d, m):
    results = {
        'a': a,
        's': s,
        'd': d,
        'm': m
    }

    operations = ('+', '-', '/', '*')

    for i in range(0, len(floats), 4):
        if i + 3 < len(floats):
            current_slice_nums = floats[i:(i+4)]
        else:
            current_slice_nums = floats[i: len(floats)]

        i = 0
        for key in results:
            if i < len(current_slice_nums):
                current_num = current_slice_nums[i]

                try:
                    results[key] = eval(f'{results[key]}{operations[i]}{current_num}')
                except ZeroDivisionError:
                    i += 1
                    continue
                i += 1

    results = sorted(results.items(), key=lambda kv: (-kv[1], kv[0]))
    final_dict = {}
    for element in results:
        final_dict[element[0]] = element[1]
    txt = ''
    for k, v in final_dict.items():
        txt += f'{k}: {v:.1f}\n'
    return txt

