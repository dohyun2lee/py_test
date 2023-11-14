a = int(input())

def korean_number(a) :
    match(a) :
        case (1) :
            print("일")
        case (2) :
            print("이")
        case (3) :
            print("삼")
        case (4) :
            print("사")
        case (5) :
            print("오")
        case (6) :
            print("육")
        case (7) :
            print("칠")
        case (8) :
            print("팔")
        case (9) :
            print("구")
        case (10) :
            print("십")
            
print(korean_number(a))
