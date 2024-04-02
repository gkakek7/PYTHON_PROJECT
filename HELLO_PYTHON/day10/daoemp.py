import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',port=3305, password='python', db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = 'select * from emp'
        self.curs.execute(sql)

        list = self.curs.fetchall()
        return list
    
    def select(self,e_id):
        sql = f"select * from emp where e_id= '{e_id}'"
        self.curs.execute(sql)
        vo = self.curs.fetchone()
        return vo
        # list = self.curs.fetchall()
        # return list[0]
        
    def insert(self,e_id,e_name,gen,addr):
        sql = f"insert into emp (e_id, e_name, gen, addr) values ('{e_id}','{e_name}','{gen}','{addr}')"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,e_id,e_name,gen,addr):
        sql = f"update emp set e_name='{e_name}', gen='{gen}', addr='{addr}' where e_id='{e_id}'"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"delete from emp where e_id = {e_id}"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
        
    def __del__(self):    
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    vo = de.selectList()
    # vo = de.select('2')
    # cnt = de.insert('6','6','6','6')
    # cnt = de.update('5', '5', '5','5')
    # cnt = de.delete("1")
    print(vo)