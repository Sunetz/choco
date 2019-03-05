def make_choco(small, big, goal):
    weight_small = 1
    weight_big = 5
    whole_part = goal // 5
    m = goal - (goal // 5) * 5
    if whole_part <= big and m <= small:
        return m
    if whole_part > big and (goal - big*5) <= small:
        return goal - big*5
    else:
        return -1
    if whole_part > big and goal <= small:
        return goal
    else:
        return -1

print(make_choco(6,1,10))
print(make_choco(60,100,550))
