import numpy as np
import matplotlib.pyplot as plt


p = 0.4
gamma = 1
w = 200
wealth_steps = 0.2
action_steps = 0.01
A = np.arange(0, 1 + action_steps, action_steps)
num_states = int(w / wealth_steps) + 1

X = np.linspace(0, w, num_states)
V = np.zeros(num_states)
V[-1] = 1
iterations = 500

for _ in range(iterations):
    V_new = V.copy()
    for i in range(1, num_states - 1):
        best_value = 0
        for a in A:
            bet = a * X[i]
            X_win = min(w, X[i] + bet)
            X_lose = max(0, X[i] - bet)

            i_win = np.searchsorted(X, X_win)
            i_lose = np.searchsorted(X, X_lose)

            expected_value = p * V[i_win] + (1 - p) * V[i_lose]
            best_value = max(best_value, expected_value)

        V_new[i] = best_value
    V = V_new



optimal_policy = np.zeros(num_states)
for i in range(1, num_states - 1):
    best_a = 0
    best_value = 0
    for a in A:
        bet = a * X[i]
        X_win = min(w, X[i] + bet)
        X_lose = max(0, X[i] - bet)

        i_win = np.searchsorted(X, X_win)
        i_lose = np.searchsorted(X, X_lose)

        expected_value = p * V[i_win] + (1 - p) * V[i_lose]
        if expected_value > best_value:
            best_value = expected_value
            best_a = a

    optimal_policy[i] = best_a

for i in range(num_states):
    print("X: ", X[i], "Optimal Policy: ", optimal_policy[i])
