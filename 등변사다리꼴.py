class 등변사다리꼴:

    꼭짓점의_개수 = 4
    변의_개수 = 4
    개수 = 0
    
    def __init__(self, 윗변, 아랫변, 높이):
        self.윗변 = 윗변
        self.아랫변 = 아랫변
        self.__높이 = 높이
        등변사다리꼴.개수 += 1
    
    @classmethod
    def 총_개수_출력(cls):
        print(cls.개수)
    
    @staticmethod
    def 넓이구하기(윗변, 아랫변, 높이):
        return (윗변+아랫변)*높이/2

    ###########################################################

    @property
    def 높이(self):
        print("높이 getter 호출")
        return self.__높이

    @높이.setter
    def 높이(self, value):
        print("높이 setter 호출")
        if value<=0 or type(value)!=int:
            raise ValueError("적절한 값이 아닙니다.")
        self.__높이 = value

    @property
    def 넓이(self):
        print("넓이 getter 호출")
        return 등변사다리꼴.넓이구하기(self.윗변, self.아랫변, self.높이)    





class 직사각형(등변사다리꼴):
    개수 = 0
    def __init__(self, 밑변, 높이):
        super().__init__(밑변, 밑변, 높이)
        직사각형.개수 += 1

    @classmethod
    def 총_개수_출력(cls):
        print(cls.개수)

    @staticmethod
    def 넓이구하기(밑변, 높이):
        return 등변사다리꼴.넓이구하기(밑변, 밑변, 높이)







등변사다리꼴.총_개수_출력() # 초기값 0
직사각형.총_개수_출력() # 초기값 0

등변1= 등변사다리꼴(5,15,5)
print(등변1.넓이) # getter 호출 50

직사1 = 직사각형(8,5)
직사2 = 직사각형(11,3)

등변사다리꼴.총_개수_출력() # 2
직사각형.총_개수_출력() # 3

print(등변사다리꼴.넓이구하기(8,10,7)) # 63
print(직사각형.넓이구하기(10,10)) # 100

print(직사1.넓이) # 넓이 getter 호출 40

print(직사2.넓이) # 넓이 getter 호출 33

print(직사2.높이) # 높이 getter 호출 3

직사2.높이=1 # 높이 setter 호출

print(직사2.높이) # 높이 getter 호출 1

print(직사2.넓이) # 넓이 getter 호출 11

직사2.높이=0 # ValueError: 적절한 값이 아닙니다.