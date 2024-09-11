import numpy as np

def solution(x, y):
    w_hat = []
    for i in range(len(x)):
        w_hat.append(sum(x[i][j] * y[j] for j in range(len(y))))

    print("w_hat:", w_hat)

    sum_w_hat = sum(np.exp(w_hat[j]/100.) for j in range(len(w_hat)))
    print(sum_w_hat)
    w = []
    for i in range(len(w_hat)):
        w.append(np.exp(w_hat[i]/100.) / sum_w_hat)
    # w = [np.exp(w_hat[i]/100.) / sum_w_hat for i in range(len(w_hat))]
    print("w", w)

    y_hat = []
    for i in range(len(x)):
        y_hat.append(sum(w[i] * x[i][j] for j in range(len(w))))

    print("y_hat:", y_hat)
    int_y_hat = [round(x) for x in y_hat]
    return int_y_hat

# Example usage:
x = [[1, 2, 3],
     [8, 9, 5],
     [5, 1, 9]]
y = [1, 2, 3]

result = solution(x, y)
print(result)
# correct: [4, 4, 5]


"""
import numpy as np
def solution(x, y):
    w_hat = []
    for j in range(len(y)):
        w_hat.append(sum(i * y[j] for i in x[j]))
    print(w_hat)

    sum_w_hat = sum(np.exp(w_hat[j]/100.) for j in range(len(w_hat)))
    print(sum_w_hat)
    w = []
    for i in range(len(w_hat)):
        w.append(np.exp(w_hat[i]/100.) / sum_w_hat)
    # w = [np.exp(w_hat[i]/100.) / sum_w_hat for i in range(len(w_hat))]
    print(w)

    # y_hat = []
    # for i in range(len(w)):
    #     y_hat.append(sum(w[i] * j for j in x[i]))

    y_hat = []
    for i in range(len(x)):
        y_hat.append(sum(w[j] * x[i][j] for j in range(len(w))))

    print(y_hat)
    int_y_hat = [int(x) for x in y_hat]
    return int_y_hat

# Example usage:
x = [[1, 2, 3],
     [8, 9, 5],
     [5, 1, 9]]
y = [1, 2, 3]
result = solution(x, y)
print(result)
# correct: [4, 4, 5]
"""

    
        
    