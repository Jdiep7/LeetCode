def largestGoodInteger(num):
    largest = "-1"
    n = len(num)
    for i in range(n - 2):
        cur = num[i]
        if cur == num[i+1] and cur == num[i+2]:
            if cur > largest:
                largest = cur

    return largest*3

print(largestGoodInteger("6777133339"))