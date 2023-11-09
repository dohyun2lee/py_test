num = input()

start, end = num.split()

while True : 
    degree = int(input())
    if int(start) <= degree & degree <= int(end) :
        print("Nothing to report")
    elif degree == -999 :
        break
    else :
        print("Alert!")
    
