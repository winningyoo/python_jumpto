def vartest(a):     # vartest 함수 선언
    a = a + 1

vartest(3)          # vartest 하마수의 입력값으로 a를 대입 
print(a)            #  a 값 출력 



'''
오류발생 : print(a) 문장은 오류가 발생하게 된다.
print(a)에서 사용한 a변수는 어디에도 선언되지 않았기 때문 

그렇다면 함수안에서 함수 밖의 변수를 변경하는 방법은?
'''