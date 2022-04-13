import random as rd

nums = ['None',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
mylist = []
x = rd.choice(nums)
def create_list():
    mylist.append(rd.randint(1,10000))

if x != 'None':
    i = 0
    while i <= x:
        create_list()
        i += 1

print(mylist)
if x == 'None':
    print("My GODDAMNED list is empty you Knob Gobbler!!!")
elif len(mylist) == 1:
    print(f"My list has {len(mylist)} random integer in it!")
else:
    print(f"My list has {len(mylist)} random integers in it!")



