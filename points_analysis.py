# analyze point stats
import pandas as pd
import matplotlib.pyplot as plt


def main():
    player_data = pd.read_csv('data/Player_Per_Game.csv')

    player_data = player_data.drop(['birth_year'], axis=1)
    player_data = player_data.dropna()

    points_by_position(player_data)


def position_analysis(position_data):
    position_data = position_data.groupby('season')['x3pa_per_game'].apply(list)

    years_before = []
    avg_val_before = []
    years_after = []
    avg_val_after = []

    for year in range(1980, 2010):
        years_before.append(year)
        current_season = position_data[year]
        season_avg = round(average(current_season), 2)
        avg_val_before.append(season_avg)

    for year in range(2010, 2025):
        years_after.append(year)
        current_season = position_data[year]
        season_avg = round(average(current_season), 2)
        avg_val_after.append(season_avg)

    return years_before, years_after, avg_val_before, avg_val_after


def points_by_position(player_data):
    year_before_pg, year_after_pg, avg_before_pg, avg_after_pg = \
        position_analysis(player_data[player_data['pos'] == 'PG'])

    year_before_sg, year_after_sg, avg_before_sg, avg_after_sg = \
        position_analysis(player_data[player_data['pos'] == 'SG'])

    year_before_pf, year_after_pf, avg_before_pf, avg_after_pf = \
        position_analysis(player_data[player_data['pos'] == 'PF'])

    year_before_c, year_after_c, avg_before_c, avg_after_c = \
        position_analysis(player_data[player_data['pos'] == 'C'])

    plt.rcParams["figure.figsize"] = (12, 8)

    plt.subplot(2, 2, 1)
    plt.scatter(year_before_pg, avg_before_pg, c='blue')
    plt.scatter(year_after_pg, avg_after_pg, c='green')
    plt.grid()

    plt.legend(['Before Curry', 'After Curry'])
    plt.title('Threes Attempted By Point Guards Over The Years')

    plt.subplot(2, 2, 2)
    plt.scatter(year_before_sg, avg_before_sg, c='blue')
    plt.scatter(year_after_sg, avg_after_sg, c='green')
    plt.grid()

    plt.legend(['Before Curry', 'After Curry'])
    plt.title('Threes Attempted By Shooting Guards Over The Years')

    plt.subplot(2, 2, 3)
    plt.scatter(year_before_pf, avg_before_pf, c='blue')
    plt.scatter(year_after_pf, avg_after_pf, c='green')
    plt.grid()

    plt.legend(['Before Curry', 'After Curry'])
    plt.title('Threes Attempted By Power Forwards Over The Years')

    plt.subplot(2, 2, 4)
    plt.scatter(year_before_c, avg_before_c, c='blue')
    plt.scatter(year_after_c, avg_after_c, c='green')
    plt.grid()

    plt.legend(['Before Curry', 'After Curry'])
    plt.title('Threes Attempted By Centers Over The Years')

    plt.show()


def average(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':
    main()

