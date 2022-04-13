# def validate_pin(pin):
#     return len(str(pin)) in (4, 6) and str(pin).isdigit()
# print(validate_pin('2345'))
# import math
# x = pow(2,38)
# print(x)

# import string
#
# d = dict.fromkeys(string.ascii_lowercase)
# alphabet = {key: index for (key, index) in d.items()}
# print(alphabet)

# mylist = range(1,10001)
# new_count = 0
# for num in mylist:
#     if num % 17 == 0:
#         new_count += 1
# print(new_count)
#
#
# ###TUPLE Unpacking
# mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
# sum = 0
# for (a, b) in mylist:
#     sum = sum + (a*b)
#     #print(b)
# print(sum)

x = 0
while x <= 10:
    print(f"The value of x is:  {x}")
    x += 1