MOD = 301907  # за модулем

def count_valid_parentheses(template):

    n = len(template)
    dp = [0] * (n + 1)

    dp[0] = 1
    stack = []
    
    for i in range(n):

        temp_dp = [0] * (n + 1)

        for open_count in range(n):

            if dp[open_count] == 0:
                continue

            if template[i] == "(":
                temp_dp[open_count + 1] = (temp_dp[open_count + 1] + dp[open_count]) % MOD
                stack.append('(')

            elif template[i] == ")" and open_count > 0:
                temp_dp[open_count - 1] = (temp_dp[open_count - 1] + dp[open_count]) % MOD
                if stack and stack[-1] == '(':
                    stack.pop()

            elif template[i] == "?":
                temp_dp[open_count + 1] = (temp_dp[open_count + 1] + dp[open_count]) % MOD
                if open_count > 0:
                    temp_dp[open_count - 1] = (temp_dp[open_count - 1] + dp[open_count]) % MOD
        
        dp = temp_dp
    
    return dp[0]

input_string = input().strip()
print(count_valid_parentheses(input_string))