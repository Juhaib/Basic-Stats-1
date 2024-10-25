import numpy as np
import scipy.stats as stats

# Data
data = [1.13, 1.55, 1.43, 0.92, 1.25, 1.36, 1.32, 0.85, 1.07, 1.48, 1.20, 1.33, 1.18, 1.22, 1.29]

# Sample statistics
mean = np.mean(data)
std_dev = np.std(data, ddof=1)  # Sample standard deviation (ddof=1)
n = len(data)

# 99% confidence level (alpha = 0.01)
alpha = 0.01
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)

# Confidence interval calculation
margin_of_error = t_critical * (std_dev / np.sqrt(n))
confidence_interval = (mean - margin_of_error, mean + margin_of_error)

# Results
print(f"Sample Mean: {mean}")
print(f"Sample Standard Deviation: {std_dev}")
print(f"99% Confidence Interval: {confidence_interval}")

# Given population standard deviation
pop_std_dev = 0.2

# 99% confidence level
z_critical = stats.norm.ppf(1 - alpha/2)

# Confidence interval calculation
margin_of_error = z_critical * (pop_std_dev / np.sqrt(n))
confidence_interval = (mean - margin_of_error, mean + margin_of_error)

# Results
print(f"99% Confidence Interval with Known Population Standard Deviation: {confidence_interval}")
