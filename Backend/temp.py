series = []

num = 20
first = 0
second = 1
sum = 0

series.append(first)
series.append(second)

for i in range(3, num+1):
    third = first + second
    series.append(third)
    first = second
    second = third

    if third % 2 == 0:
        sum += third
    
print(series)
print(sum)

# arr = [3, 7, 8, 11, 9, 10]

# first = arr[0]
# second = arr[1]

# for num in arr:
#     if num > first:
#         second = first
#         first = num
#     elif num > second:
#         second = num

# print(second)

# arr = [1, 2, 3, 4, 5, 6, 7, 8]

# initial = 1
# last = len(arr)-1

# while initial < len(arr)/2:
#     arr[initial], arr[last] = arr[last], arr[initial]
#     initial += 2
#     last -= 2

# print(arr)

# for 