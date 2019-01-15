# https://www.hackerrank.com/challenges/coin-change/problem

def coin_change_recursive(n, X):

    if n == 0:
        return 1

    if n < 0:
        return 0

    if n > 0 and len(X) == 0:
        return 0
    
    X_copy = list(X)
    val = X_copy.pop()
    return coin_change_recursive(n-val, X) + coin_change_recursive(n, X_copy)

def coin_change_dp(n, S):
    m = len(S)

    table = [[0]*m for _ in range(0, n+1)]
    
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table entries in bottom up manner 
    for i in range(1, n+1): 
        for j in range(m): 
  
            # Count of solutions including S[j] 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
  
            # Count of solutions excluding S[j] 
            y = table[i][j-1] if j >= 1 else 0
  
            # total count 
            table[i][j] = x + y 
  
    return table[n][m-1]

            



print(coin_change_recursive(10, [2, 5, 3, 6]))
print(coin_change_dp(4, [1, 2, 3]))
