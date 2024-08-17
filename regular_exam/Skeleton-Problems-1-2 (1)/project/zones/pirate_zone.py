from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.VOLUME)

    def zone_info(self):
        info = ['@Pirate Zone Statistics@', f'Code: {self.code}; Volume: {self.volume}', 'Battleships currently in the '
                                           f'Pirate Zone: {len(self.ships)}, {len([s for s in self.ships if s.__class__.__name__ == "RoyalBattleship"])}'
                                           f' out of them are Royal Battleships.']

        ships_lst = [s.name for s in self.get_ships()]
        if ships_lst:
            names_info = ', '.join(ships_lst)
            info.append(f'#{names_info}#')

        return '\n'.join(info)

