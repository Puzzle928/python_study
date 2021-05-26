# 책(제목(cust_name), 등급(author))
# 멤버 변수 : cust_name/author
# 메소드 : 이름 제공(리턴)- getCust_name or getCustName / 등급 제공 - getXxx

class Book:
    
    # 생성자 - 객체생성(실 데이터로 생성=멤버 변수에 값 할당, 멤버 변수 초기화)
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print('Book __init__')
    
    def getBookName(self):
        print('Book getBookName')
        return self.title