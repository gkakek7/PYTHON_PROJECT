from sqlalchemy.dialects.mssql.base import MONEY
class Xi:
    def __init__(self):
        self.money = 1000;
    def spend(self,cost):
        self.money -= cost
    def __del__(self):
        print("")



class Putin:
    def __init__(self):
        self.nuclear = 10000;
    
    def war(self):
        self.nuclear -= 1;
    def __del__(self):
        print("")
        


class Minkyu(Xi, Putin):
    def __init__(self):
        Xi.__init__(self)
        Putin.__init__(self)
    # def spend(self, cost):
    #     self.money -= cost


if __name__ == '__main__':
    mk = Minkyu()
    print(mk.money)
    print(mk.nuclear)
    mk.spend(5)
    mk.war()
    print(mk.money)
    print(mk.nuclear)
