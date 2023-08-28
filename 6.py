def exceptionchk(a, b) :
    try :
        if a/b == 0 : 
            print("결과:",a/b)
        else :
            print("결과(!=0):", a/b)
    except: 
        print("0으로는 나눌 수 없음")
        
exceptionchk(6,2)
exceptionchk(5,3)
exceptionchk(3,0)
exceptionchk(0,2)