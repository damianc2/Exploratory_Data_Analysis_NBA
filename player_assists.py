# analyze assist stats
import pandas as pd
import matplotlib.pyplot as plt


def main():
    player_data = pd.read_csv('data/Player_Per_Game.csv')

    player_data = player_data.drop(['birth_year'], axis=1)
    player_data = player_data.dropna()

    assists_by_position(player_data)


def average(lst):
    return sum(lst) / len(lst)


def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


def assists_by_position(player_data):
    player_position = player_data.groupby('pos')['ast_per_game'].apply(list)
    print(player_position)
    c_avg = round(average(player_position['C']), 2)
    pf_avg = round(average(player_position['PF']), 2)
    sf_avg = round(average(player_position['SF']), 2)
    sg_avg = round(average(player_position['SG']), 2)
    pg_avg = round(average(player_position['PG']), 2)

    pos_ast_data = {'Point Guard': pg_avg, 'Shooting Guard': sg_avg, 'Small Forward': sf_avg, 'Power Forward': pf_avg,
                    'Center': c_avg}
    positions = list(pos_ast_data.keys())
    pos_ast_vals = list(pos_ast_data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(positions, pos_ast_vals, width=0.4)

    add_labels(positions, pos_ast_vals)

    plt.xlabel('Player Position')
    plt.ylabel('Average Assists Per Game')
    plt.title("Average Assists per Player Position")

    plt.show()


if __name__ == '__main__':
    main()

