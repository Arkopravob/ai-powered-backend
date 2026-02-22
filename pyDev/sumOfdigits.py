def findSumOfDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
        return sum
    sum = findSumOfDigits(123)
    print('sum of digits is', sum)
