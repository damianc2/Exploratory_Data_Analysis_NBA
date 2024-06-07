# analyze team playoff stats
# REMEMBER TO MAKE THIS BASED OFF USER INPUT!!!!
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter


def main():
    player_data = pd.read_csv('data/Team_Stats_Per_Game.csv')

    player_data = player_data.drop(['abbreviation'], axis=1)
    player_data = player_data.drop(['lg'], axis=1)

    league_avg_remove = player_data[player_data['team'] == 'League Average'].index
    player_data.drop(league_avg_remove, inplace=True)

    player_data = player_data.dropna()

    points_by_position(player_data)


def team_shooting_summary(teams):
    team_playoffs_made = {}

    for team in teams.index:
        if teams['playoffs'][team]:
            current_team = teams['team'][team]
            team_playoffs_made[current_team] = team_playoffs_made.get(current_team, 0) + 1

    return team_playoffs_made


def points_by_position(player_data):

    team_playoffs = team_shooting_summary(player_data)

    number_of_teams = 7
    top_teams = dict(sorted(team_playoffs.items(), key=itemgetter(1), reverse=True)[:number_of_teams])

    top_teams_values = [*top_teams.values()]
    top_teams_names = [*top_teams.keys()]

    # originally used to show percentages of each team too
    # def func(pct, all_values):
    #     absolute = int(pct / 100. * np.sum(all_values))
    #     return "{:.1f}%\n{:d} playoffs".format(pct, absolute)

    def func_new(pct, all_values):
        absolute = int(pct / 100. * np.sum(all_values))
        return "{:d} playoffs".format(absolute)

    fig, ax = plt.subplots(figsize=(8, 5))
    wedges, texts, autotexts = ax.pie(top_teams_values, autopct=lambda pct: func_new(pct, top_teams_values),
                                      startangle=90, labels=top_teams_names,
                                      textprops=dict(color="black"))

    ax.set_title('Teams with Most Playoff Appearances')

    plt.show()


if __name__ == '__main__':
    main()
