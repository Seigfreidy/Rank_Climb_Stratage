import generate_discrete_random

def random_rank(x):
    prob_value_pairs = [(-40,1-x),(100,x**2),(10,x*(1-x))] 
    rank = generate_discrete_random.method(prob_value_pairs)  
    return rank

def average_rank(x):
    # rate = 0
    rank = 0

    # lose 1st game
    rank += -40 * (1-x)
    # win 2 game
    rank += 100 * x**2
    # win 1 lose 1
    rank += 10 * x * (1-x)

    return rank