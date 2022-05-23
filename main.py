import re

def duplicate(a, list):
    for i in list:
        if i == a:
            return True
        else:
            return False
class Table:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.data = []
    def load_data(self):
        try:
            file = open(self.path, 'r', encoding='utf-8')
            temp = file.readlines()
            for line in temp:
                l = line.split(";")
                self.data.append(l)
        except:
            print("O arquivo não existe")
    def show(self):
        print("Tabela" + self.name)
        for line in self.data:
            print(line)
    def intersec(self, table):
        t3 = Table('t3', 'intersec.csv')
        ret = []
        for lt1 in self.data:
            for lt2 in table.data:
                if lt1[0] == lt2[0] and not(duplicate(lt2, ret)):
                    ret.append(lt2)

        print(len(ret))
        return ret
    def save(self, table):
        try:
            file = open('savefile.csv', 'w', encoding='utf-8')
            for line in table:
                ls = len(line)
                for i in range(ls):
                    if i < ls-1:
                        file.write(line[i]+';')
                    else:
                        file.write(line[i])
                
            file.close()
        except:
            print("erro")
def main(**kwargs):
    t1 = Table('t1', 'prod.csv')
    t1.load_data()
    #t1.show()
    t2 = Table('t2', 'servicos - 23614.csv')
    t2.load_data()
    #t2.show()
    t1.save(t1.intersec(t2))

main()