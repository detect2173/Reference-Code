# nums = [11, 44, 23,17]
#
# for num in nums:
#     square = num ** 2
#     print(square)
#
# nums_sq = [x**2 for x in nums]

#Get the avg of a given list of numbers rounded to the nearest whole number
#Without using sum() or len()
list_01 = [23, 51, 83, 12, 77, 103, 67]
x = 0
i = 0
for num in list_01:
    x = x + num
    i += 1

avg = x / i
print(round(avg))