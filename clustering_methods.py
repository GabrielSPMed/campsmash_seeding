def count_tiers(df):
    return len(df.Tier.unique())
def find_largest_diff(df, debug=False):
    largest_diff = 0
    for i in df.index[:-1]:
        if df.loc[i].Tier == df.loc[i+1].Tier:
            if df.loc[i].Points - df.loc[i+1].Points > largest_diff:
                largest_diff = df.loc[i].Points - df.loc[i+1].Points
                if debug:
                    print(f'Largest diff detected: {df.loc[i].Player} - {df.loc[i+1].Player}: {largest_diff}pts')
                split_index = i
    return split_index, largest_diff
def split_tiers(df, split_index, debug=False, base=False):
    df.loc[df.index>split_index, 'Tier'] -= 1
    if debug:
        diff = df.iloc[split_index, 1] - df.iloc[split_index+1, 1]
        st = f'Splitting {df.iloc[split_index, 0]} and {df.iloc[split_index+1, 0]}: {diff}pts'
        if base:
            st = '\nBase '+st
        else: 
            st = '\n'+st
        print(st)
    return df
def find_largest_tier(df, debug=False):
    largest_diff = 0
    for tier in df.Tier.unique():
        if df[df.Tier==tier].iloc[0, 1] - df[df.Tier==tier].iloc[-1, 1] > largest_diff:
            largest_diff = df[df.Tier==tier].iloc[0, 1] - df[df.Tier==tier].iloc[-1, 1]
            largest_tier=tier
    if debug:
        print(f'The largest tier is tier: {largest_tier}')
        st = f'{df[df.Tier==largest_tier].iloc[0, 0]} - {df[df.Tier==largest_tier].iloc[-1, 0]}: {largest_diff}pts'
        print(st)
    return largest_tier
              
def get_tier_size(df, tier):
    return df[df.Tier==tier].iloc[0, 1] - df[df.Tier==tier].iloc[-1, 1]

def cluster_df(df, target_tiers,  debug=False):
    while count_tiers(df)< target_tiers:
        if debug:
            print(f'\nSplit n{count_tiers(df)}')
        split_index, largest_diff = find_largest_diff(df)
        df = split_tiers(df, split_index, debug=debug, base=True)
        while(1):
            if count_tiers(df)== target_tiers:
                break
            largest_tier = find_largest_tier(df)
            if get_tier_size(df, largest_tier) <= largest_diff:
                break
            if debug:
                print(f'\nSplit n{count_tiers(df)}')
            split_index, _ = find_largest_diff(df[df.Tier==largest_tier])
            df = split_tiers(df, split_index, debug=debug)
    return df
