from typing import List

from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    VALID_ZONES = {'RoyalZone': RoyalZone, 'PirateZone': PirateZone}
    VALID_SHIPS = {'RoyalBattleship': RoyalBattleship, 'PirateBattleship': PirateBattleship}

    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        zone_class = self.VALID_ZONES.get(zone_type)

        if not zone_class:
            raise Exception("Invalid zone type!")

        zone = next((z for z in self.zones if z.code == zone_code), None)

        if zone:
            raise Exception("Zone already exists!")

        zone_obj = zone_class(zone_code)
        self.zones.append(zone_obj)

        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        ship_class = self.VALID_SHIPS.get(ship_type)

        if not ship_class:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        ship = ship_class(name, health, hit_strength)
        self.ships.append(ship)

        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        zone_type = zone.__class__.__name__
        ship_type = ship.__str__()

        if ship_type in zone_type:
            ship.is_attacking = True
        else:
            ship.is_attacking = False

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name), None)

        if not ship:
            return f'No ship with this name!'

        if not ship.is_available:
            return f"The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attacker = next((s for s in zone.ships if s.is_attacking), None)
        enemy = next((s for s in zone.ships if not s.is_attacking), None)

        if not attacker or not enemy:
            return f"Not enough participants. The battle is canceled."

        sorted_by_power = sorted(zone.ships, key=lambda s: s.hit_strength, reverse=True)
        sorted_by_health = sorted(zone.ships, key=lambda s: s.health, reverse=True)

        most_powerful = next((s for s in sorted_by_power if s.is_attacking), None)
        enemy = next((s for s in sorted_by_health if not s.is_attacking), None)

        most_powerful.attack()
        enemy.take_damage(most_powerful)

        if enemy.health <= 0:
            zone.ships.remove(enemy)
            self.ships.remove(enemy)
            return f"{enemy.name} lost the battle and was sunk."

        if most_powerful.ammunition <= 0:
            zone.ships.remove(most_powerful)
            self.ships.remove(most_powerful)
            return f"{most_powerful.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        info = []
        available_ships = [s for s in self.ships if s.is_available]
        if available_ships:
            info.append(f'Available Battleships: {len(available_ships)}')
            names = ', '.join([s.name for s in available_ships])
            info.append(f'#{names}#')

        info.append(f'***Zones Statistics:***')
        info.append(f'Total Zones: {len(self.zones)}')
        sorted_zones = sorted(self.zones, key=lambda z: int(z.code))
        [info.append(z.zone_info()) for z in sorted_zones]

        return '\n'.join(info)




