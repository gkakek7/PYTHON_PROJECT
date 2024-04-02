import pymysql

class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',port=3305, password='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def insert(self,s_name,price,s_code,ymd):
        sql = f"insert into stock (s_name, price, s_code, ymd) values ('{s_name}',{price},'{s_code}','{ymd}')"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt