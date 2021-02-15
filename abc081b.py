# atcoder begginer's selection ABC086A

'''
s = input()
token = s.split()

num_list [] # empty list
while token:
    num_list.append(int(token.pop(0))) # take 1st element and converse to int'''
size = int(input())
num_list = list(map(int,input().split()))

num_div = 0
all_even = True
while all_even:
    for i in range(size):
        if num_list[i]%2 == 1: # if element is Odd number ?
           all_even = False
           break
        else:
            num_list[i] //=2
    if all_even:
        num_div +=1
print(num_div)