import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 433193277 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.02
    a = st.anderson_ksamp([x, y]).significance_level
    
    return a < alpha 

433193277
