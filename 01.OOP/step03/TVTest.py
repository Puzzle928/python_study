# self는 생성된 해당 객체 참조 변수로 간주 하셔도 됩니다.
# 객체 생성 없는 클래스 내부에서는 self 를 사용할 필요가 없음
# self의 주용도 - 멤버 변수 호출


from TVInfo import TV

class Test:

    # list에 TV 객체들 저장

    # 이미 list내에 저장된 TV 객체들의 TV 이름만 출력
    def tv_info_public():
        tv_all = [TV('난 TV', 'LG'), TV('난 TV2', 'samsung')]
        return tv_all

    def tv_info_print(datas):   # [<TVInfo.TV object at 0x000002A99B7D7B50>, <TVInfo.TV object at 0x000002A99B772130>] 을 나타내기위하여
        for v in datas:
            print(v.getName())


    if __name__ == '__main__':

        # step02 - 데이터 받아서 활용하는 메소드 호출
        all = tv_info_public() # [TV('난 TV', 'LG'), TV('난 TV2', 'samsung')]


        tv_info_print(all) # [TV('난 TV', 'LG'), TV('난 TV2', 'samsung')] 하지만   [<TVInfo.TV object at 0x000002A99B7D7B50>, <TVInfo.TV object at 0x000002A99B772130>] 뜸


        # step01 - 객체 생성 문법과 __str__자동 호출되는 내용 재확인
        # 객체 생성해서 tv 변수에 객체의 주소값 대입
        #tv = TV('난 TV', 'LG')
        #print(tv) # __str__ 자동 호출 왜? 객체를 참조하는 변수(객체명 또는 객체라고 표현하기도 함)


        # 객체 생성해서 해당 객체를 바로 출력
        #print(TV('난 TV', 'LG')) # __str__ 자동 호출 왜? 객체를 참조하는 변수(객체명 또는 객체라고 표현하기도 함)