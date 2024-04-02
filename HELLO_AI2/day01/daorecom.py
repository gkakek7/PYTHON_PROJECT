import cx_Oracle 
import numpy as np

class DaoRecom:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@127.0.0.1:1521/xe')
        self.cur = self.conn.cursor()
    
    def insert(self,e_id,ymd,m_id):
        sql = f"""
            insert into recom
            (e_id,ymd,m_id)
            values 
            ('{e_id}', '{ymd}', '{m_id}')
        """
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount

    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    dr = DaoRecom()
    cnt = dr.insert('1','1','1')
    
    print(cnt)

    
    
    
    
    
    