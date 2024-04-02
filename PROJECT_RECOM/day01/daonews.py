import cx_Oracle 
import numpy as np

class DaoNews:
    def __init__(self):
        self.conn = cx_Oracle.connect('TEAM3_202308F/java@112.220.114.130:1521/xe')
        self.cur = self.conn.cursor()
        
    def deleteRecome(self):
        sql =   """
            delete from news_recom
        """
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount
    # y_train
    def selectLabeList(self):
        sql =   """
            select 
            news_views.news_cg
            from news_views join emp on(news_views.emp_id=emp.emp_id)
            ORDER BY emp.emp_id
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        list = np.array([[float(cell) for cell in row] for row in list])
        return list
    # x_train
    def selectList(self):
        sql =   """
            select 
            CASE 
                    WHEN emp.emp_age < 30 THEN '0'
                    WHEN emp.emp_age < 40 THEN '1'
                    WHEN emp.emp_age < 50 THEN '2'
                    WHEN emp.emp_age < 60 THEN '3'
                    ELSE '4'
            END AS 연령대
            ,
            CASE 
                    WHEN emp.emp_gen  = 'F' THEN '0'
                    WHEN emp.emp_gen  = 'M' THEN '1'
            END AS GEN
            ,
            CASE 
                    WHEN emp.dept_id LIKE 'D0%' THEN '0'
                    WHEN emp.dept_id LIKE 'D1%' THEN '1'
                    WHEN emp.dept_id LIKE 'D2%' THEN '2'
                    WHEN emp.dept_id LIKE 'D2%' THEN '3'
                    ELSE '4'
            END AS 부서번호
            
            from news_views join emp on(news_views.emp_id=emp.emp_id)
            ORDER BY emp.emp_id
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        list = np.array([[float(cell) for cell in row] for row in list])
        return list
    # 추천 정보 저장
    def updateRecom(self, news, age, gen, dept,rank):
        sql = """ 
            UPDATE news_recom
            SET
             
                age_cg_id = :age ,
                gen_cg_id = :gen ,
                dept_cg_id = :dept 
               
            WHERE
                    news_cg_id = :news
                AND age_cg_id = :age
                AND gen_cg_id = :gen
                AND dept_cg_id = :dept
                AND news_rank = :rank
        """
        self.cur.execute(sql, {'news': news, 'age':age,'gen':gen ,'dept':dept,'rank':rank})
        self.conn.commit()
        return self.cur.rowcount
    # 추천 정보 저장
    def insertRecom(self, news, age, gen, dept,rank):
        sql = """ 
              INSERT INTO news_recom (
                news_cg_id
                , age_cg_id
                , gen_cg_id
                , dept_cg_id
                , news_rank
            ) VALUES (
                :news
              , :age
              , :gen
              , :dept
              , :rank
            )
        """
        self.cur.execute(sql, {'news': news, 'age':age,'gen':gen ,'dept':dept,'rank':rank})
        self.conn.commit()
        return self.cur.rowcount
    # 누가 어떤 뉴스를 봤는지에 따른 라벨정보 조회
    def selectXYLabelList(self):
        sql = """
            select 
            news_views.news_cg
            ,
            CASE 
                    WHEN emp.emp_age < 30 THEN '0'
                    WHEN emp.emp_age < 40 THEN '1'
                    WHEN emp.emp_age < 50 THEN '2'
                    WHEN emp.emp_age < 60 THEN '3'
                    ELSE '4'
            END AS 연령대
            ,
            CASE 
                    WHEN emp.emp_gen  = 'F' THEN '0'
                    WHEN emp.emp_gen  = 'M' THEN '1'
            END AS GEN
            ,
            CASE 
                    WHEN emp.dept_id LIKE 'D0%' THEN '0'
                    WHEN emp.dept_id LIKE 'D1%' THEN '1'
                    WHEN emp.dept_id LIKE 'D2%' THEN '2'
                    WHEN emp.dept_id LIKE 'D2%' THEN '3'
                    ELSE '4'
            END AS 부서번호
            
            from news_views join emp on(news_views.emp_id=emp.emp_id)
            ORDER BY emp.emp_id
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
    # y_train 갯수
    def selectCnt(self):
        sql =   """
          SELECT COUNT(*) FROM NEWS_CG
          """
        self.cur.execute(sql)
        cnt = self.cur.fetchone()
        return cnt[0]


# 여기부턴 셀레니움
    def selectUrlList(self,id):
        sql =   f"""
            select news_url from news_cg where news_cg_id = '{id}' or news_cg_id like '%{id}'
          """   
        self.cur.execute(sql)
        url = self.cur.fetchone()
        return url[0];
    
    def selectRecomName(self,id):
        sql =   f"""
        select news_cg_name from news_cg where news_cg_id = '{id}' or news_cg_id like '%{id}'
          """  
        self.cur.execute(sql)
        name = self.cur.fetchone()
        return name[0];
    
    def selectNewsCgList(self):
        sql =   f"""
        select news_cg_id, news_url from news_cg
          """  
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list;
    
    def updateNewsCg(self, id, title, src,reg_dt,repot):
        sql = """
        UPDATE news_cg
        SET 
            news_cg_id = :id,
            news_cg_name = :title,
            news_img_url = :src,
            news_reg_dt = :reg_dt,
            news_repot = :repot
        WHERE news_cg_id = :id
        """
        
        self.cur.execute(sql, {'title': title, 'id': id, 'src': src, "reg_dt": reg_dt, "repot": repot})

        self.conn.commit()
        return self.cur.rowcount
    
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    de = DaoNews()
    # x_train = de.selectList()
    # y_train = de.selectLabeList()
    # cnt = de.selectLabeList()
    # list=de.selectUrlList("03");
    # list=de.selectNewsCgList();
    cnt=de.updateNewsCg('01', 'title',"img")
    
    print(cnt)