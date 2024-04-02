import pymysql
import numpy as np
class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',port=3305, password='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def insert(self,s_name,price,s_code,ymd):
        sql = f"insert into stock (s_name, price, s_code, ymd) values ('{s_name}',{price},'{s_code}','{ymd}')"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    def selectArr(self,s_name):
        sql = f"select * from stock where s_name= '{s_name}'"
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        arr=[]
        for s in list:
            arr.append(s['price'])
            
        return arr
    
    def selectArrN(self,s_name):
        sql = f"select * from stock where s_name= '{s_name}'"
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        arr=[]
        for s in list:
            arr.append(s['price'])
            
        return np.array(arr)
    def selectSNames(self):
        sql = "SELECT s_name FROM stock GROUP BY s_name "
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        arr=[]
        for s in list:
            arr.append(s['s_name'])
        return arr
if __name__ == '__main__':
    de=DaoStock()
    list = de.selectArrN("삼성전자")
    print(list)
    

