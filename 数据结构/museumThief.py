# 0/1 背包问题

def knapsack(items, capacity):
    """
    items: 列表，每个元素是字典，例如 {"weight": 2, "value": 3}
    capacity: 背包容量（整数）
    返回最大价值和选择的物品索引
    """
    n = len(items)
    # dp[i][w] 表示前 i 件物品在容量 w 下的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 填表
    for i in range(1, n + 1):
        wt = items[i - 1]["weight"]
        val = items[i - 1]["value"]
        for w in range(capacity + 1):
            if wt > w:
                dp[i][w] = dp[i - 1][w]  # 装不下
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wt] + val)

    # 回溯找到选中的物品
    w = capacity
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # 说明第 i 件物品被选了
            selected.append(i - 1)
            w -= items[i - 1]["weight"]

    selected.reverse()  # 保持原顺序
    for raw in dp:
        print(raw)
    return dp[n][capacity], selected


if __name__ == "__main__":
    # 示例
    items = [
        {"weight": 2, "value": 3},
        {"weight": 3, "value": 4},
        {"weight": 4, "value": 5},
        {"weight": 5, "value": 8}
    ]
    capacity = 8

    max_value, chosen_items = knapsack(items, capacity)
    print("最大价值:", max_value)
    print("选择的物品索引:", chosen_items)
    print("选择的物品:", [items[i] for i in chosen_items])
