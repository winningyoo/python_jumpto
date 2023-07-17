def say_myself(name, age, man=True):   # man=True <- 디폴트값. 매개변수에 미리 값을 넣어 초기값을 설정한것. 
                                       #                    초기화 하고 싶은 매개변수는 항상 뒤쪽에 놓아야한다
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살 입니다." % age)
    if man: 
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("박운용", 27)