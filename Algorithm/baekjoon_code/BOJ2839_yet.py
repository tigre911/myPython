n = int(input())

sugar = [5 , 3]

count = 0

if n%5 == 
for i in sugar:
    print(f'n : {n}')
    print(f'i : {i}')
    count += n // i
    n %= i

    print(f'count : {count}')
print(count)