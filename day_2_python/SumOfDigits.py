def findSumOfDigits(number):
    sum = 0
    while number > 0 :
        rem = number % 10
        number = number // 10
        sum = sum + rem
        return sum
    sum = findSumOfDigits(123)
    print('sum of digits is', sum)