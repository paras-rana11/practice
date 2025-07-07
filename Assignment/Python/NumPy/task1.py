def find_pairs_with_sum(target_sum, max_num):
    pairs = []
    for a in range(1, max_num + 1):
        b = target_sum - a
        if b >= 1 and b <= max_num and a <= b:
            pairs.append((a, b))
    return pairs

target_sum = 24
max_num = 25

result = find_pairs_with_sum(target_sum, max_num)

print(f"Pairs from 1 to {max_num} with sum {target_sum}:")
for pair in result:
    print(pair)

