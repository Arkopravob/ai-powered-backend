# def findMax(num1 , num2):
#     if num1 >= num2:
#         return -1
#     valid_numbers = []
#     for num in range( num1 , num2 +1):
#         if num >= 10 & num <=99:
#             if num % 5 == 0:
#                 digitSum = sum(int(d) for d in str(num))
#                 if digitSum % 3 == 0:
#                  valid_numbers.append(num)
#     if valid_numbers:
#         return max(valid_numbers)
#     else:
#         return -1

def find_max(num1, num2):
    max_sum = -1
    # Write your logic here
    if num1 >= num2:
        return -1
    valid_numbers = []
    for num in range(num1, num2 +1):
         if 10<=num <= 99:
             if num % 5 == 0:
                digit_sum = (num // 10) + (num % 10)
                if digit_sum % 3 == 0:
                  valid_numbers.append(num)
    if valid_numbers:
        max_num = max(valid_numbers)
    return max_sum
#Provide different values for num1 and num2 and test your program.
max_num = find_max(20,75)
print(max_num)

