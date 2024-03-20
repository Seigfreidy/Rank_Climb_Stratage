import random  
  
def generate_discrete_random(prob_value_pairs):  
    # 提取概率和值  
    values, probabilities = zip(*prob_value_pairs)  
      
    # 确保概率之和为1  
    assert abs(sum(probabilities) - 1.0) < 1e-6, "Probabilities must sum to 1."  
      
    # 使用random.choices生成随机值  
    random_value = random.choices(values, weights=probabilities, k=1)[0]  
    return random_value  

def strive_to_win_random(x):
    prob_value_pairs = [(100,x**2),(-30,(x * (1-x)**2) * 2),(60,(x**2 * (1-x)) * 2),(-80,(1-x)**2)] 
    random_value = generate_discrete_random(prob_value_pairs)  
    return random_value