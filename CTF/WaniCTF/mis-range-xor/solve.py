def min_xor_count(N, A):
    MOD = 10**9 + 7

    # ステップ1: 整数列Aの各要素に対して操作fを適用するか適用しないかの選択肢を考慮
    B = [(min(a, 1000 - a), a) for a in A]

    # ステップ2: それぞれの選択肢について、0と1の個数をカウント
    bit_count = [[0, 0] for _ in range(10)]
    for b_min, b_max in B:
        for i in range(10):
            if b_min & (1 << i):
                bit_count[i][1] += 1
            else:
                bit_count[i][0] += 1
            if b_max & (1 << i):
                bit_count[i][1] -= 1
            else:
                bit_count[i][0] -= 1
    
    print(bit_count)

    # ステップ3: 各桁について、操作fを適用するかどうかを選択し、Xを最小にするためにその桁を反転させる整数の個数を計算
    min_changes = [min(count_0, count_1) for count_0, count_1 in bit_count]

    # ステップ4: 計算した値の積を求め、10^9+7で割った余りを返す
    result = 1
    for change in min_changes:
        result = (result * (change + 1)) % MOD

    return result

# 例
N = 10
A = [532, 746, 606, 601, 293, 825, 912, 826, 789, 190]
print(min_xor_count(N, A))  # 出力: 2
