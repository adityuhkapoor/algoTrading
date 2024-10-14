import numpy as np
import matplotlib.pyplot as plt

S0 = 100
K = 105
C = 2

ST = np.linspace(50, 150, 100)

def coveredCallPayoff(ST, S0, K, C):
    payoff = np.where(ST > K, K - S0 + C, ST - S0 + C)
    return payoff

P_max = K - S0 + C
L_max = S0 - C

payoff = coveredCallPayoff(ST, S0, K, C)

plt.figure(figsize=(10, 6))
plt.plot(ST, payoff, label='Covered Call Payoff', color='b')
plt.axhline(P_max, linestyle='--', color='g', label=f'Max Profit = {P_max}')
plt.axhline(-L_max, linestyle='--', color='r', label=f'Max Loss = -{L_max}')
plt.axvline(S0, linestyle='--', color='black', label=f'Initial Stock Price (S0) = {S0}')
plt.axvline(K, linestyle='--', color='purple', label=f'Strike Price (K) = {K}')

plt.title('Covered Call Strategy Payoff Diagram')
plt.xlabel('Stock Price at Expiration (ST)')
plt.ylabel('Payoff')
plt.legend(loc='best')
plt.grid(True)
plt.show()