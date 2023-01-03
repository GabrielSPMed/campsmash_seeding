def print_seed(df):
    print('\nSeed Sugerida\n')
    for i in df.index:
        print(f'{i+1}.{df.iloc[i, 0]} - Tier {df.iloc[i, 2]}')