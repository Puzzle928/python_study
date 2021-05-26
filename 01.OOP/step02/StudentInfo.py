# 한 학생 정보만 보유 가능한 클래스
# 학생 수 만큼 객체 생성할 경우 데이터 혼란 방지

class Student:

    # 생성자 호출 문법: Student(값1, .., 값4)
    def __init__(self, name, grade , gender, subject):
        self.stu_name = name
        self.stu_grade = grade
        self.stu_gender = gender
        self.stu_subject = subject
    
    # 멤버 변수들값을 다 결합해서 하나의 문자열로 반환
    # 함수의 기능은 참조 변수명만 출력시에 str이 자동 실행되서 return된 구조로 실행됨
    def __str__(self):
        return '학생정보'+ ' ' + self.stu_name + ' ' + self.stu_grade + ' '+ self.stu_gender + ' '+ self.stu_subject

    # 각 멤버 변수별로 set/getXxx 메소드 보유되어 있다 가정

    # ?grade는 1학년, 2학년, 3학년 값에 한해서만 저장
    # 유효성 검증 코드 필수
    def setStuGrade(self,new_grade):
        if new_grade == '1학년' or '2학년' or '3학년':
            self.grade = new_grade

    # ?gender는 남 또는 여
    # 유효성 검증 코드 필수

    def setStuGender(self,new_gender):
        if new_gender == '남' or '여':
            pass
        