from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.VOLUME)

    def zone_info(self):
        info = ['@Royal Zone Statistics@', f'Code: {self.code}; Volume: {self.volume}', 'Battleships currently in the '
                                           f'Royal Zone: {len(self.ships)}, {len([s for s in self.ships if s.__class__.__name__ == "PirateBattleship"])}'
                                           f' out of them are Pirate Battleships.']

        ships_lst = [s.name for s in self.get_ships()]
        if ships_lst:
            names_info = ', '.join(ships_lst)
            info.append(f'#{names_info}#')

        return '\n'.join(info)

