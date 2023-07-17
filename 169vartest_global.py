a = 1
def vartest():
    global a 
    a = a + 1

vartest()
print(a)

'''
vartest 함수 안의 global a 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다.
하지만 프로그래밍을 핳ㄹ때 glodbal 명령어는 사용하지 않는 것이 좋음 
함수는 독립적으로 존재하는 것이 좋기 때문 '''