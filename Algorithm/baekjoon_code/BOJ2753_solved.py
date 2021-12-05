n=1

n = int(input())
if 4000>n>1:
    if (n%4) == 0 and ((n%100) != 0 or (n%400) == 0):
        print(1)
    else:
        print(0)