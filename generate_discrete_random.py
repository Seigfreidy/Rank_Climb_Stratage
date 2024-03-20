import random

def method(prob_value_pairs):  
    # 提取概率和值  
    values, probabilities = zip(*prob_value_pairs)  
      
    # 确保概率之和为1  
    assert abs(sum(probabilities) - 1.0) < 1e-6, "Probabilities must sum to 1."  
      
    # 使用random.choices生成随机值  
    random_value = random.choices(values, weights=probabilities, k=1)[0]  
    return random_value 