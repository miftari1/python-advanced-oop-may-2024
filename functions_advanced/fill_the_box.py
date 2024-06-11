def fill_the_box(height, lenght, width, *cubes):
    box_size = height * lenght * width
    cubes = list(cubes)
    i = 0
    while cubes[i] != 'Finish' and i < len(cubes):
        current_cube = int(cubes[i])
        if current_cube <= box_size:
            box_size -= current_cube
        else:
            cubes[i] = current_cube - box_size
            box_size = 0
            break
        i += 1
    else:
        if box_size > 0:
            return f'There is free space in the box. You could put {box_size} more cubes.'
    if box_size == 0 and i < len(cubes):
        cubes_left = 0
        for cube in cubes[i:-1]:
            cubes_left += cube
        return f'No more free space! You have {cubes_left} more cubes.'
