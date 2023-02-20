def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for y in range(2)]
    for i in range(n + 1):
        for w in range(W + 1):
            if (i == 0 or w == 0):
                K[i % 2][w] = 0
            elif (wt[i - 1] <= w):
                K[i % 2][w] = max(
                val[i - 1]
                + K[(i - 1) % 2][w - wt[i - 1]],
                K[(i - 1) % 2][w])
            else:
                K[i % 2][w] = K[(i - 1) % 2][w]
    return K[n % 2][W]
if __name__ == "__main__":
 val = [60, 100, 120]
 wt = [10, 20, 30]
 W = 50
 n = len(val)
 print("Knapsack using Dynamic Programming Approach")
 print("Items: \t",val)
 print("Weights: ",wt)
 print(knapSack(W, wt, val, n))