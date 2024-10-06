def arithmetic_progression_sum(A, B, N):
    
    return (N * (2 * A + (N - 1) * B)) // 2


num_cases = int(input())


results = []

for _ in range(num_cases):
    A, B, N = map(int, input().split())
    sum_value = arithmetic_progression_sum(A, B, N)
    results.append(sum_value)


print(" ".join(map(str, results)))
