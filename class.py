class 사람:
    수 = 0
    def __init__(본인, 이름, 나이):
        본인.이름 = 이름
        본인.나이 = 나이
        사람.수 += 1

        

print(f"현재 인원 : {사람.수}명")
김싸피 = 사람("김싸피",9)
print(김싸피.이름, 김싸피.나이,f"현재 인원 : {사람.수}명")
부울경 = 사람("부울경",2)
print(부울경.이름, 부울경.나이,f"현재 인원 : {사람.수}명")