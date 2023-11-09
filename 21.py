num = int(input())

for n in range(1, num) :
    match (n % 3, n % 5) :
        case (0, 0) :
            print("FizzBuzz")
        case (0, _) :
            print("Fizz")
        case (_, 0) :
            print("Bizz")
        case _ :
            print(n)