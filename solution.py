import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 373544056

def solution(p: float, x: np.array) -> tuple:
	from scipy.stats import chi2

	alpha = 1 - p
	size = len(x)
	
	x2 = np.array([xi**2 for xi in x])
	x2_mean = x2.mean()
	
	chi2_rv = chi2(df = 2 * size)
	
	left = chi2_rv.ppf(1 - alpha / 2)
	right = chi2_rv.ppf(alpha / 2)
	
	return np.sqrt(size * x2_mean / (left * 41)), np.sqrt(size * x2_mean / (right * 41))
