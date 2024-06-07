# analyze team stats
import pandas as pd
import matplotlib.pyplot as plt


def main():
    player_data = pd.read_csv('data/Team_Stats_Per_Game.csv')

    player_data = player_data.drop(['abbreviation'], axis=1)
    player_data = player_data.drop(['lg'], axis=1)
    player_data = player_data.dropna()

    points_by_position(player_data)


def average(lst):
    return sum(lst) / len(lst)


def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


def top_teams_percent(two_thousands, stat_line):
    avg_percent = 0
    for year in range(2000, 2025):
        current_season = two_thousands[two_thousands['season'] == year]

        top_teams = current_season.nlargest(16, [stat_line])
        num_in_playoffs = len(top_teams[top_teams['playoffs']])

        percent_in_playoffs = num_in_playoffs / 16
        avg_percent = avg_percent + percent_in_playoffs

    avg_percent = round(((avg_percent / 25) * 100), 2)

    return avg_percent


def points_by_position(player_data):
    two_thousands = player_data[player_data['season'] >= 2000]

    playoff_percent_fg = top_teams_percent(two_thousands, 'fg_percent')
    playoff_percent_ft = top_teams_percent(two_thousands, 'ft_percent')
    playoff_percent_trb = top_teams_percent(two_thousands, 'trb_per_game')
    playoff_percent_pts = top_teams_percent(two_thousands, 'pts_per_game')
    playoff_percent_ast = top_teams_percent(two_thousands, 'ast_per_game')
    playoff_percent_tov = top_teams_percent(two_thousands, 'tov_per_game')

    percent_stat_data = {'turnovers': playoff_percent_tov, 'free throw %': playoff_percent_ft,
                         'assists': playoff_percent_ast, 'rebounds': playoff_percent_trb, 'points': playoff_percent_pts,
                         'field goal %': playoff_percent_fg}

    stat_lines = list(percent_stat_data.keys())
    playoff_percent_vals = list(percent_stat_data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(stat_lines, playoff_percent_vals, width=0.4)

    add_labels(stat_lines, playoff_percent_vals)

    plt.xlabel('Team Stat types')
    plt.ylabel('Total Teams in Playoff (Percent)')
    plt.title("Importance of Team Stat Type to Make Playoff")
    plt.show()


if __name__ == '__main__':
    main()

