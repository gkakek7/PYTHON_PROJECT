import pymysql

class Daomem:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root',port=3305, password='python', db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = 'select * from mem'
        self.curs.execute(sql)

        list = self.curs.fetchall()
        return list
    
    def select(self,m_id):
        sql = f"select * from mem where m_id= '{m_id}'"
        self.curs.execute(sql)
        vo = self.curs.fetchone()
        return vo
        # list = self.curs.fetchall()
        # return list[0]
        
    def insert(self,m_id,m_name,mobile,email):
        sql = f"insert into mem (m_id, m_name, mobile, email) values ('{m_id}','{m_name}','{mobile}','{email}')"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self,m_id,m_name,mobile,email):
        sql = f"update mem set m_name='{m_name}', mobile='{mobile}', email='{email}' where m_id='{m_id}'"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,m_id):
        sql = f"delete from mem where m_id = '{m_id}'"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
        
    def __del__(self):    
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = Daomem()
    vo = de.selectList()
    # vo = de.select('2')
    # cnt = de.insert('6','6','6','6')
    # cnt = de.update('5', '5', '5','5')
    # cnt = de.delete("1")
    print(vo)