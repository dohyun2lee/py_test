a = input()

def triple(put) :
    if put.isdecimal() == True :
        print(int(put) * 3)
    else :
        print(put * 3)

triple(a)