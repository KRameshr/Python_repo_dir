# 1. Calculating Z-Scores (Standardized Scores)
# A $z$-score tells you how many standard deviations a value is from the mean.
#  Positive score: Above average.
#  Negative score: Below average.
#  -0.9 (your Mocha): Slightly below the average sugar content of the other drinks.





import numpy as np
from scipy import stats

# 1. Create the sugar content array from your screenshot
sugar_data = np.array([15, 18, 20, 26, 32, 38, 32, 24, 21, 16, 13, 11, 14])

# 2. Calculate Z-scores
z_scores = stats.zscore(sugar_data)

print("Sugar Content Mean:", np.mean(sugar_data))
print("Standard Deviation:", np.std(sugar_data))
print("\nZ-Scores for each drink:")
print(z_scores)

# Finding the Mocha specifically (which was 14g)
mocha_z = z_scores[-1]
print(f"\nThe Z-score for the 14g Mocha is: {mocha_z:.2f}")




# 2. Chi-Squared Test (Dependency Testing)
# This is used to see if the differences in your observed data are due to chance or a real relationship.

# P-value > 0.05: The result is not significant (it's likely just random chance).

# P-value < 0.05: There is a significant relationship.
# Create the observation matrix from your screenshot
# Rows could be 'Store Location' and Columns could be 'Drink Type Sold'
obs = np.array([
    [7, 1, 3],
    [87, 18, 84],
    [12, 3, 4],
    [9, 1, 7]
])

# Run the Chi-squared contingency test
chi2, p, dof, expected = stats.chi2_contingency(obs)

print(f"Chi-squared Statistic: {chi2:.4f}")
print(f"P-value: {p:.4f}")

if p > 0.05:
    print("Conclusion: P-value is greater than 0.05. No significant relationship found.")
else:
    print("Conclusion: P-value is less than 0.05. The relationship is statistically significant.")