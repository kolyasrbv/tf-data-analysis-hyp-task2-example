import pandas as pd
import numpy as np


chat_id = 433193277 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    simulations = 1000
    n_s = 1000
    res = []
    # Running A/A Test Simulations
    x = pd.DataFrame(x)
    y = pd.DataFrame(y)
    for i in tqdm(range(simulations)):
        res.append(stats.ttest_ind(x.sample(n_s, replace = False), \
                                   y.sample(n_s, replace = False), \
                                   equal_var = False)[1]) # saving p-value
# Checking that the number of false positive cases does not exceed alpha
    m = sum(np.array(res) < 0.02) / simulations
    if m < 0.02:
        return False
    return True
solution(x, y)
