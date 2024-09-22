# sys.stdin.readline() 은 EOFError 를 발생시키지 않고 빈 문자열을 리턴한다
# 입력이 없는데 input() 을 호출하면 에러가 발생

while 1:
    try:
        print(input())
    except:
        break
