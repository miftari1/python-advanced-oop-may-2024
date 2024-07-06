def boarding_passengers(capacity, *passenger_groups):
    boarded_groups = {}
    all_passengers = 0
    passengers_boarded = 0
    print(passenger_groups)
    for group in passenger_groups:
        number_people = int(group[0])
        benefit_plan = group[1]
        all_passengers += number_people
        if capacity >= number_people:
            if benefit_plan not in boarded_groups:
                boarded_groups[benefit_plan] = 0
            boarded_groups[benefit_plan] += number_people
            capacity -= number_people
            passengers_boarded += number_people

    boarded_groups = dict(sorted(boarded_groups.items(), key=lambda x: (-x[1], x[0])))
    boarding_information = []
    boarding_information.append('Boarding details by benefit plan:')
    for benefit_plan, passengers in boarded_groups.items():
        info = f'## {benefit_plan}: {passengers} guests'
        boarding_information.append(info)
    txt = ''
    if all_passengers == passengers_boarded:
        txt = 'All passengers are successfully boarded!'
    elif not capacity and all_passengers > passengers_boarded:
        txt = 'Boarding unsuccessful. Cruise ship at full capacity.'
    elif capacity and all_passengers > passengers_boarded:
        txt = f'Partial boarding completed. Available capacity: {capacity}.'

    boarding_information.append(txt)

    return '\n'.join(boarding_information)

print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))