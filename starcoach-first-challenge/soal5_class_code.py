k = int(input())

numbers_range = range(1, 5001)

numbers_string = ''.join(str(num) for num in numbers_range)

print(numbers_string[k-1])

