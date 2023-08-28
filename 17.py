num = int(input("What year were you born? "))

if num <= 1924 :
        print("가장 위대한 세대")
elif (1925 <= num & num <= 1945) :
    print("침묵 세대")
elif (1946 <= num & num <= 1954) :
    nationality = str(input("Are you Korean?(y/n) "))
    if nationality == 'y' :
        print("침묵 세대")
    else :
        print("베이비붐 세대")
    print("침묵 세대")
elif (1955 <= num & num <= 1963) :
    print("베이비붐 세대") 
elif num == 1964 :
    nationality = str(input("Are you Korean?(y/n) "))
    if nationality == 'y' :
        print("X 세대")
    else :
        print("베이비붐 세대")
elif (1965 <= num & num <= 1980) :
    print("X 세대")
elif (1981 <= num & num <= 1996) :
    print("밀레니얼 세대")
else :
    print("Z세대") 