hour, minute = map(int, input('hours, minutes').split()) #'hours, minutes'지우니까 성공
if 23>=hour >0 :
    if (minute - 45)<0:
        print(hour -1 , 60+(minute-45))
    else:
        print(hour, minute-45)
elif hour ==0:
    if (minute - 45)<0:
        print(23 , 60+(minute-45))
    else:
        print(hour, minute - 45)