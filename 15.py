num = int(input())

if num % 4 == 0 :
    if num % 100 == 0 :
        if num % 400 == 0 :
            print(num, "년은 윤년입니다.")
        else :
            print(num, "년은 평년입니다.")
    else :
        print(num, "년은 윤년입니다.")
else :
    print(num, "년은 평년입니다.")          