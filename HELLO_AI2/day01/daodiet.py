import cx_Oracle 
import numpy as np

class DaoDiet:
    def __init__(self):
        self.conn = cx_Oracle.connect('python/python@127.0.0.1:1521/xe')
        self.cur = self.conn.cursor()
    
    def selectList(self):
        sql =   """
            select 
                e.e_name,
                m.m_name,
                d.ymd 
            from diet d, emp e, menu m
            where
                d.E_ID = e.E_ID and
                d.m_id = m.m_id
            order by d.ymd desc ,e.e_name
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        myjson = []
        for e in list:
            myjson.append({'e_name':e[0],'m_name':e[1],'ymd':e[2]})
        return myjson
    
    def getXtYt(self,e_id,cnt):
        sql =   f"""
            select 
                m_id 
            from
                diet
            where
                e_id = '{e_id}'
            order by ymd desc
        """
        print("getXtYt",sql)
        self.cur.execute(sql)
        list = self.cur.fetchall()
        arr = []
        for i in list:
            arr.append(i[0])
        xtr = []    
        xt = []
        yt = []
        
        for i in range(len(arr)-2):
            yt.append(arr[i])
            xt.append(arr[i+2])
            xt.append(arr[i+1])
            
            
        for i in range(len(xt)):
            line_n = np.zeros(cnt).astype(int)
            line_n[xt[i]] = 1
            for l in line_n:
                xtr.append(l)
    
        
        x_train = np.array(xtr)
        y_train = np.array(yt)
        
        x_train = np.reshape(x_train,(-1,2*cnt))
        
        return x_train,y_train
    
    def getPred(self,e_id,cnt):
        sql =   f"""
            select 
                m_id 
            from
                diet
            where
                e_id = '{e_id}'
            order by ymd desc
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        arr = []
        for i in list:
            arr.append(i[0])
        
        line_n1 = np.zeros(cnt).astype(int)
        line_n1[arr[1]] = 1

        line_n2 = np.zeros(cnt).astype(int)
        line_n2[arr[0]] = 1
        
        
        ret = np.concatenate((line_n1, line_n2))
        return ret
        
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    de = DaoDiet()
    ret = de.getPred('S001',5)
    
    print(ret)

    
    
    
    
    
    