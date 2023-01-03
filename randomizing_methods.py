import numpy as np
import pandas as pd
def get_points_mean_for_tier(df, tier):
    return df[df.Tier==tier].Points.mean()
def add_missing_players(df, points, missing):
    for player in missing:
        new_row = {'Player':player, 'Points':points, 'Tier':5}
        df = pd.concat([df, pd.DataFrame(new_row, index=[len(df)])], axis=0)
    return df
def sort_df(df):
    return df.sort_values(["Tier", "Points"], ascending=[False, False]).reset_index(drop=True)
def randomize_points(df, window):
    for i in range(len(df)):
        df.iloc[i, 1] += np.random.randint(-window, window+1)
    return df
def randomize_df(df, variance, missing=[]):
    # Quanto maior o valor maior vai ser a aleatoriedade de posicoes entre jogadores do mesmo tier 
    if missing:
        points = get_points_mean_for_tier(df, 5)
        df = add_missing_players(df, points, missing)
        df = sort_df(df)
    df = randomize_points(df, variance)
    df = sort_df(df)
    return df
