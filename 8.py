class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
        print("생성자 호출 : " + self.name + " age : "+ str(age))
    def whoAreYou(self) :
        return "나는 {}입니다.".format(self.name)
    def updatePerson(self, name, age) :
        self.nmae =name
        self.age = age    