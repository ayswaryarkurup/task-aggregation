

import pandas as pd

# Majority vote

def majority_vote(mturk_res):
    pass

def majority_vote_workers(mturk_res, votes):
    pass


# Part 1 - Weighted majority vote

def weighted_majority_vote_workers(mturk_res):
    pass

def weighted_majority_vote(mturk_res, workers):
    pass


# EM algorithm

def em_worker_quality(rows, labels):
    pass

def em_votes(rows, worker_qual):
    pass

def em_iteration(rows, worker_qual):
    labels = em_votes(rows, worker_qual)
    worker_qual = em_worker_quality(rows, labels)
    return labels, worker_qual

def em_vote(rows, iter_num):
    pass


#Qualified workers

def select_qualified_worker(mturk_res):
    pass


# Your main function

def main():
    # Read in CVS result file with pandas
      mturk_res = pd.read_csv('data.csv')

    # Call functions and output required CSV files
    pass

if __name__ == '__main__':
    main()
