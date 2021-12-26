n = int(input())

num_list = []

for i in range(n):
    num_list.append(i+1)

print(num_list)

while len(num_list) > 1:
    for i in reversed(range(0, len(num_list), 2)):

        print(f'numlist = {num_list}')
        print(i)
        num_list.remove(num_list[i])
        print(f'result = {num_list}')
        print('-'*50)
result = num_list[0]

print(result)

for i in range(0,7,2):      #range(처음, 끝, 간격(얼마나띄울건지))
    print(f'원래 : {i}')

for i in reversed(range(0,7,2)):
    print(f'뒤집어서 : {i}')