import sys


def sum_frequencies(freq, i, j):
    return sum(freq[k] for k in range(i, j + 1))


def optimal_bst(freq, i, j, dp, root):
    if i > j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    min_cost = sys.maxsize

    for r in range(i, j + 1):
        left_cost = optimal_bst(freq, i, r - 1, dp, root)
        right_cost = optimal_bst(freq, r + 1, j, dp, root)
        total_cost = left_cost + right_cost + sum_frequencies(freq, i, j)

        if total_cost < min_cost:
            min_cost = total_cost
            root[i][j] = r

    dp[i][j] = min_cost
    return dp[i][j]


def construct_optimal_bst(root, i, j, keys):
    if i > j:
        return None

    r = root[i][j]
    left_subtree = construct_optimal_bst(root, i, r - 1, keys)
    right_subtree = construct_optimal_bst(root, r + 1, j, keys)

    return (keys[r], left_subtree, right_subtree)


def optimal_bst_cost(keys, freq, n):
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    root = [[-1 for _ in range(n)] for _ in range(n)]
    optimal_cost = optimal_bst(freq, 0, n - 1, dp, root)
    optimal_tree = construct_optimal_bst(root, 0, n - 1, keys)
    return optimal_cost, optimal_tree


# Example
if __name__ == "__main__":
    keys = [10, 20, 30, 40]
    freq = [4, 2, 6, 3]

    n = len(keys)

    cost, tree = optimal_bst_cost(keys, freq, n)

    print(f"Optimal cost: {cost}")
    print(f"Optimal Binary Search Tree: {tree}")
