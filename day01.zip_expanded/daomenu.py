import cx_Oracle 

class DaoMenu:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@192.168.41.221:1521/xe')
        self.cur = self.conn.cursor()
        
        
    def getLabels(self):
        sql =   """
            select 
                m_id,
                m_name
            from menu
            order by m_id
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        myjson = []
        for e in list:
            myjson.append({'m_id':e[0],'m_name':e[1]})
        return myjson
    
    
    
    def selectList(self):
        sql =   """
            select 
                m_id,
                m_name,
                DECODE(use_yn, 'y', 'O', 'n', 'X', '-') use_yn
            from menu
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        myjson = []
        for e in list:
            myjson.append({'m_id':e[0],'m_name':e[1],'use_yn':e[2]})
        return myjson
    
    def getCnt(self):
        sql =   """
            select 
                count(*) as cnt
            from menu
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list[0][0]

    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    de = DaoMenu()
    cnt = de.getCnt()
    print(cnt)