def rectangle(lenght, width):
    if not isinstance(lenght, int) or not isinstance(width, int):
        return 'Enter valid values!'

    def area():
        rectangle_area = lenght * width
        return rectangle_area

    def perimeter():
        rectangle_perimeter = (width + lenght) * 2
        return rectangle_perimeter

    return f'Rectangle area: {area()}\n' \
           f'Rectangle perimeter: {perimeter()}'
