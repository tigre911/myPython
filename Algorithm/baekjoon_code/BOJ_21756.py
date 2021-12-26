n = int(input())

num_list = []

for i in range(n):
    num_list.append(i+1)

print(num_list)

while len(num_list) > 1:
    for i in reversed(range(0, len(num_list), 2)):
        print(f'i : {i}')
        print(f'numlist = {num_list}')
        num_list.pop(i)
        print(f'result = {num_list}')
result = num_list[0]

print(result)

#
# for i in reversed(range(0,7,2)):
#     print(i)