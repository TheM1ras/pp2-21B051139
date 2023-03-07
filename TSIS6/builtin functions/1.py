def sum(nums):
    a = int(1)
    for i in nums:
        a = a * i
    return a
mynums = [1, 2, 3, 4, 5, 6, ]

print(sum(mynums))