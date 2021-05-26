# TV 데이터 표현 하는 클래스

class TV:
    def __init__(self, name, company_name):
        self.name = name
        self.company_name = company_name

    # setXxx/ getXxx 들이 다 있다 가정

    def getName(self): # self 는 멤버 변수 호출을 위한 필수 키워드
        return self.name # 생성된 TV 객체가 보유한 멤버변수값 변환


    def __str__(self):
        return "제품명 : " + self.name + '제조사: ' + self.company_name
    
    if __name__ == '__main__':
        tv = TV('난 TV', 'LG')
        print
    


    # TV 객체를 참조하는 변수명 또는 TV 객체 자체를 print() 출력시에 자동 호출되는 __str__재정의

    #  멤버 변수들 값을 하나의 문자열로 결합해서 반환

