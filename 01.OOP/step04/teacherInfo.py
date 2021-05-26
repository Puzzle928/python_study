class Teacher:
    
    def __init__(self, name, teaching, subject):
        self.name = name
        self.teaching = teaching
        self.subject = subject
    
    def __str__(self):
        return "선생님 정보: " + self.name + ' ' + self.teaching + ' ' + self.subject

    #def setName(self, new_name):
     #   if new_name == '1학년' or '2학년' or '3학년':
      #      self.name = new_name
    
    
    #def  setSubJect(self, new_subject):
     #   if new_subject == '미술' or '체육' or '음악':
      #      self.subject = new_subject