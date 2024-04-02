class animal:
    def __init__(self):
        self.name = ""
        print("생성자")
        
    def named(self,name):
        self.name = name
        
    def __str__(self):
        return "[animal][name]:"+self.name
        
    def __del__(self):    
        print("소멸자")
        
class human(animal):
    
    def __init__(self):
        super().__init__() # 부모를 잡아주어야 함
        self.asset = 0
        
    def goldenSpoon(self):
        self.asset = 1000000000
        
if __name__ == '__main__':
      
    hu = human()
    print("ani.name1",hu.name)
    print("ani.asset",hu.asset)
    hu.named("영웅")
    hu.goldenSpoon()
    print("ani.name1",hu.name) 
    print("ani.asset",hu.asset)
