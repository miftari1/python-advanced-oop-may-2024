from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self, red_bull_team: RedBullTeam = None, mercedes_team: MercedesTeam = None):
        self.red_bull_team = red_bull_team
        self.mercedes_team = mercedes_team

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == 'Mercedes':
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError('Invalid team name!')
        return f'{team_name} has joined the new F1 season.'

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception('Not all teams have registered for the season.')

        if red_bull_pos < mercedes_pos:
            team_with_better_position = 'Red Bull'
        else:
            team_with_better_position = 'Mercedes'

        return f'Red Bull: {RedBullTeam.calculate_revenue_after_race(self.red_bull_team, red_bull_pos)}.' \
               f' Mercedes: {MercedesTeam.calculate_revenue_after_race(self.mercedes_team, mercedes_pos)}.' \
               f' {team_with_better_position} is ahead at the {race_name} race.'


