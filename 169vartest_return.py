a = 1 
def vartest(a):
    a = a + 1
    return a

a = vartest(a)  # vartest(a)의 리턴값을 함수 밖의 변수 a에 대입 
print(a)