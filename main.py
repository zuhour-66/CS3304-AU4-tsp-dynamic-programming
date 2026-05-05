import itertools
import random
import time

# توليد مصفوفة مسافات عشوائية
def generate_distance_matrix(n, seed=42):
    random.seed(seed)
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = random.randint(10, 100)
            matrix[i][j] = matrix[j][i] = dist
    return matrix

# خوارزمية Held-Karp (Dynamic Programming)
def tsp_dp(dist):
    n = len(dist)
    dp = {}

    for i in range(1, n):
        dp[(1 << i, i)] = dist[0][i]

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) or v == 0:
                    continue
                new_mask = mask | (1 << v)
                if (mask, u) in dp:
                    dp[(new_mask, v)] = min(
                        dp.get((new_mask, v), float('inf')),
                        dp[(mask, u)] + dist[u][v]
                    )

    full_mask = (1 << n) - 1
    return min(dp[(full_mask ^ 1, i)] + dist[i][0] for i in range(1, n))


# القوة الغاشمة
def tsp_brute_force(dist):
    n = len(dist)
    cities = list(range(1, n))
    min_cost = float('inf')

    for perm in itertools.permutations(cities):
        cost = dist[0][perm[0]]
        for i in range(len(perm) - 1):
            cost += dist[perm[i]][perm[i+1]]
        cost += dist[perm[-1]][0]
        min_cost = min(min_cost, cost)

    return min_cost


# اختبار الأداء
def test():
    print("n\tDP Time\tBrute Time")
    for n in range(5, 13):
        dist = generate_distance_matrix(n)

        start = time.time()
        tsp_dp(dist)
        dp_time = time.time() - start

        start = time.time()
        tsp_brute_force(dist)
        bf_time = time.time() - start

        print(f"{n}\t{dp_time:.4f}\t{bf_time:.4f}")

test()