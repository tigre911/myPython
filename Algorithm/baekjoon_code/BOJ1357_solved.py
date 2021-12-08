x, y = map(str, input().split())
# 문자열을 거꾸로 해줄때는 n[::-1]로 해준다 (문자열만 가능한듯?)

def rev(n):
    n = (n[::-1])
    return n
#return 을 넣어줘야 함수를 사용했을때 값이 나온다.

result = rev(str(int(rev(x))+int(rev(y))))
#rev함수로 되면 str이므로 덧셈을 할때는 int로 캐스팅후 덧셈한다
#덧셈을 한뒤에는 str로 변경해야 다시 rev 함수가 사용가능하므로 다시 str 로 캐스팅한다

print(int(result)) #마지막엔 int 로 캐스팅