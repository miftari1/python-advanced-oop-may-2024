from collections import deque

packages = list(map(int, input().split()))
couriers = deque(map(int, input().split()))

total_weight_packages = 0
while packages and couriers:
    current_package = packages.pop()
    courier = couriers.popleft()

    if courier >= current_package:
        new_capacity = courier - 2 * current_package
        if new_capacity > 0:
            couriers.append(new_capacity)
        total_weight_packages += current_package

    else:
        new_weight = current_package - courier
        packages.append(new_weight)
        removed_weight = current_package - new_weight
        total_weight_packages += removed_weight

print(f'Total weight: {total_weight_packages} kg')

if not packages and not couriers:
    print('Congratulations, all packages were delivered successfully by the couriers today.')
elif packages and not couriers:
    print(f'Unfortunately, there are no more available couriers to deliver the following packages: \
{", ".join(list(map(str, packages)))}')
elif couriers and not packages:
    print(f'Couriers are still on duty: {", ".join(list(map(str, couriers)))} but there are no more packages to deliver.')
