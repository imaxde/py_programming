def razmen(money):
    for i in range(money // 4 + 1):
        for j in range((money - i * 4) // 6 + 1):
            remain = money - i * 4 - j * 6
            if remain % 9 == 0:
                k = remain // 9
                return f"{i}x4 {j}x6 {k}x9"
    return "-42'"

print(razmen(int(input())))
