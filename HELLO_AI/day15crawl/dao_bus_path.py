import pymysql

class DaoBusPath:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                               db='python', charset='utf8')
         
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "select * from bus_path"
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    

    
    def insert(self,bp_name,bp_seq,sta_id,sta_name,lat,lng):
        sql = f"""
            insert into bus_path
            (bp_name,bp_seq,sta_id,sta_name,lat,lng)
            values 
            ('{bp_name}','{bp_seq}','{sta_id}','{sta_name}','{lat}','{lng}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    

    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoBusPath()
    list = de.selectList()
    print(list)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        