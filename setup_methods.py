import pandas as pd
import glob
def get_PR():
    #retorna o df do pr
    df = pd.read_csv(glob.glob('PowerRankings/*')[0])
    df = df.drop(['Rank', 'Country', 'Characters'], axis=1)
    return df
def get_attendees():
    # retorna uma lista com os participantes do torneio
    with open('Attendees/Attendees.txt') as f:
        lines = f.read().splitlines()
    return lines
def filter_players(df, attendees):
    #Filtra os jogadores do pr que vao para o torneio
    return df[df['Player'].isin(attendees)].reset_index(drop=True)
def create_tier_column(df):
    df['Tier'] = 10
    return df
def get_players_not_pr(df, att):
    missing = list(set(att) - set(df.Player.unique()))
    if not missing:
        print('Todo jogador foi identificado no PR!')
    else:
        print(f'Jogadores nao identificados: {missing}')
    return missing
def setup_clustering():
    #df is the untiered dataframe
    #att is the list of attendees
    #missing is the list of attendees not in our PR
    att = get_attendees()
    df = get_PR()
    df = filter_players(df, att)
    df = create_tier_column(df)
    missing = get_players_not_pr(df, att)
    return df, att, missing
