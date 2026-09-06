"""
Bank Transaction Analysis

A bank has transactions:

transactions = [5000, -2000, 10000, -3000, 15000, -1000]

Task:

Positive values represent deposits.
Negative values represent withdrawals.
Use a loop and conditional statements to calculate total deposits, withdrawals, and final balance.
"""

print("========================================")
print("       BANK TRANSACTION ANALYSIS")
print("========================================")

transactions = [5000, -2000, 10000, -3000, 15000, -1000]
starting_balances=20,000


depoists=0
withdraw=0
starting_balances=20000

for sum in transactions:
    if sum>0:
        depoists=depoists+sum
    else:
        withdraw=withdraw+sum
    final_balances=depoists+withdraw+starting_balances

print("total deposits:",depoists)
print("total withdrawals:",withdraw)
print("\n")
print("starting balances:",starting_balances)
print("final balances:",final_balances)

print("\n")
print("========================================")