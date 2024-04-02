import pymysql

conn = pymysql.connect(host='localhost', user='root',port=3305, password='python', db='python', charset='utf8')
 
curs = conn.cursor(pymysql.cursors.DictCursor)

sql = 'select * from emp'
# sql1 = 'insert into emp(e_id, e_name, gen, addr) values(%s,%s,%s,%s)'
sql2 = "insert into emp(e_id, e_name, gen, addr) values(5,'5','5','5')"
# val = (4,"4","4","4")

curs.execute(sql)
# curs.execute(sql,(4,4,4,4))

table = curs.fetchall()

# print(table)

conn.commit()

for a in table:
    print(a)

curs.close()
conn.close()