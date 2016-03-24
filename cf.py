__author__ = "Jaime Pastor"

import pandas as pd
import numpy as np
import argparse
import time

''' COLLABORATIVE FILTERING ================================================'''

if __name__ == "__main__":

    print '\n === Collaborative Filtering ==='
    print 'Reading input'
    start = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('--train')
    parser.add_argument('--test')
    args = parser.parse_args()
    argsdict = vars(args)

    train = pd.read_csv(argsdict['train'], header=None)
    test = pd.read_csv(argsdict['test'], header=None)
    train.columns = ['movieid', 'customerid', 'rating']
    test.columns = ['movieid', 'customerid', 'rating']

    print 'Computing similarity matrix'
    train2 = train.pivot(index = 'customerid', columns = 'movieid',
                         values = 'rating')
    user_mean = train2.mean(axis = 1)
    cor_matrix = train2.T.corr().fillna(0)

    print 'Building predictions'
    rating_diff = train2.sub(train2.mean(axis=1), axis=0)
    user_mean_of_means = user_mean.mean()
    users_all = user_mean.index
    movies_all = rating_diff.columns
    predictions = []

    for i in range(len(test)):
        movie_k, user_i, = [int(test.iat[i,0]), int(test.iat[i,1])]
        # Get user i's mean or assign mean of means
        if user_i in users_all:
            user_i_mean = user_mean.loc[user_i]
        else:
            user_i_mean = user_mean_of_means
        # Obtain all ratings of movie k
        if movie_k in movies_all:
            rating_diff_js = rating_diff.loc[:,movie_k]
            users_j_no_k = rating_diff_js[rating_diff_js.isnull()].index
            # Obtain similarities of user i and users that rated movie k
            w = cor_matrix.loc[user_i,:].copy()
            w.loc[users_j_no_k] = None
            sum_w = w.abs().sum()
            # Calculate collaborative rating
            if sum_w != 0:
                coll_rating = (w * rating_diff_js).sum() / sum_w
            else:
                coll_rating = 0
        else:
            coll_rating = 0
        rating_ik = user_i_mean + coll_rating
        # Check bound and round to nearest rating
        predictions.append( round(max(min(rating_ik, 5),1),1) )

    print 'Summary results:'
    test['predictions'] = predictions
    print '  RMSE:' , round(np.sqrt( ((test['rating'] -
                                     test['predictions'])**2).mean()),4)
    print '  MAE: ' , round(np.mean(abs(test['rating'] -
        test['predictions'])),4), '\n'
    test.to_csv('predictions.txt', sep=',', header = False, index = False)

    print 'Elapsed time: ', time.time() - start

''' ========================================================================'''