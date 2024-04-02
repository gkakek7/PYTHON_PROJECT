import cx_Oracle 

class DaoEmp:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@192.168.41.221:1521/xe')
        self.cur = self.conn.cursor()
    
    def selectList(self):
        sql =   """
            select 
                e_id,
                e_name,
                DECODE(gen, 'm', '남자', 'f', '여자', '기타') gen,  
                addr
            from emp
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        myjson = []
        for e in list:
            myjson.append({'e_id':e[0],'e_name':e[1],'gen':e[2],'addr':e[3]})
        return myjson

    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    de = DaoEmp()
    list = de.selectList()
    print(list)