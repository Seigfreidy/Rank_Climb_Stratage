import generate_discrete_random

def random_rank(x, a = 0.5):
    if x <= a:
        prob_value_pairs = [(-40,1-x),(100,x**2),(10,x*(1-x))]
    else:
        prob_value_pairs = [(100,x**2),(-30,(x * (1-x)**2) * 2),(60,(x**2 * (1-x)) * 2),(-80,(1-x)**2)]
    rank = generate_discrete_random.method(prob_value_pairs)  
    return rank

def random_rank_one_to_run(x, a = 0.5):
    if x <= a:
        prob_value_pairs = [(-40,1-x),(50,x)]
    else:
        prob_value_pairs = [(100,x**2),(-30,(x * (1-x)**2) * 2),(60,(x**2 * (1-x)) * 2),(-80,(1-x)**2)]
    rank = generate_discrete_random.method(prob_value_pairs)  
    return rank

def average_rank(x):
    # rate = 0
    rank = 0

    if x <= 0.5:
        # lose 1st game
        rank += -40 * (1-x)
        # win 2 game
        rank += 100 * x**2
        # win 1 lose 1
        rank += 10 * x * (1-x)
    else:
        # win 2 match
        rate = x**2
        rank += 100 * rate
        # win 1, lose 2
        rate = (x * (1-x)**2) * 2
        rank += (-30) * rate
        # win 2, lose 1
        rate = (x**2 * (1-x)) * 2
        rank += 60 * rate
        # lose 2
        rate = (1-x)**2
        rank += (-80) * rate

    return rank

