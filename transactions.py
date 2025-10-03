import numpy as np

transactions = np.array ([
    [120, 150, 130, 170, 160, 180],
    [200, 210, 190, 220, 230, 250],
    [90, 100, 95, 110, 120, 130],
    [300, 310, 320, 330, 340, 350]
])

print("Transaction Volumes:\n", transactions)

totals = transactions.sum(axis=1)
print("\nTotal per branch:", totals)

highest_branch = np.argmax(totals) + 1
print("\nBranch with highest transactions: Branch", highest_branch)

avg_monthly = transactions.mean()
print("\nAverage monthly transaction volume:", avg_monthly)

reshaped = transactions.reshape(3, 8)
print("\nReshaped array (3x8):\n", reshaped)
print("\nImplication: Reshaping changes the structure but not data; useful for " \
"analysis in different views.")
