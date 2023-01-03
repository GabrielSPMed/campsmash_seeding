from clustering_methods import *
from setup_methods import *
from randomizing_methods import *
from printing_methods import *
import math

variance = 1000
n_tiers = 0
debug=False


if __name__ == '__main__':
    df, att, missing = setup_clustering()
    if n_tiers==0:
        n_tiers=math.ceil(df.shape[0]/2)
        if n_tiers >10:
            n_tiers=10
    df = cluster_df(df, target_tiers=n_tiers, debug=debug)
    df = randomize_df(df, variance, missing=missing)
    print_seed(df)
