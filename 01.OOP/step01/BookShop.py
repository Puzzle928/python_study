# *.py 독립적으로 개발된 파일 샐행 명령어?
#>python Bookshop.py
#? py파일을 독립적으로 실행시에 실행 시작점음 개발자가 코드로 선정


# Customer / Book  클래스를 사용해서 정보 저장(메모리에 저장)
# Custimer 객체 생성 -> getCustName() 호출해서 고객 이름 출력

# 모듈 적용
from CustomerInfo import Customer
from BookInfo import Book

class BookShopAdmin:

    
    #self라는 키워드는 클래스 내에 멤버 변수 선언 및 호출시에 사용
    #멤버 변수를 사용하는 메소드들도 parameter or argument or 인수 or 인자 에 self 적용 필수

    # BookShopAdmin에는 멤버 변수가 없음 따라서 self 불필요
    # 객체 생성 후에만 self 키워드가 유효한 기능 따라서 객체 생성없이 메소드만 호출시에는 self parameter 미선언
    def cust_create():
        # c1 로컬 변수, 메소드 실행시에 메모리에 생성되었다가 메소드 종료되며 메모리에서 자동 삭제
        # 시스템 자원의 한꼐로 메모리 관리를 자체적을 함
        c1 = Customer('재석','vvip')
        return c1

    def book_create():
        b1 = Book('python basic', '종원')
        return b1
      
    
    
    # >python BookShopAdmin.py 명령어로 실행시 최초로 자동 실행되는 로직의 코드
    # 암기 하세요
    # intro 설정 코드
    print(6)
    if __name__ == '__main__':
        print(5)
        print(cust_create()) # 현 클래스가 보유한 메소드 호출
        
        
        # 생성된 객체가 저장된 시스템 메모리의 이름을 c1이라는 새로운 변수에 대입
        c = (cust_create())
        # c1 보유한 주소번지에 저장된 객체의 getCustName() 이라는 고객 이름 반환하는 메소드의 결과값 받고 출력
        print(c.getCustName())