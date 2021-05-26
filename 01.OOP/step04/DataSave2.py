from teacherInfo import Teacher

class DataPublic1:
    
    def tea_public():
        with open('teacher.csv','r',encoding= 'utf-8') as f:
            datas = f.readlines()

            all_tea = []

            for v in datas:
                sv = v.split(',')
                
                all_tea.append(Teacher(sv[0], sv[1], sv[2]))
            return all_tea


    def tea_all_print(all_tea):
        for v in all_tea:
            print(v)


    if __name__ == '__main__':
        all = tea_public()
        tea_all_print(all)