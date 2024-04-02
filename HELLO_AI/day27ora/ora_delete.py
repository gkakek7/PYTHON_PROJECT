import cx_Oracle
    
conn = cx_Oracle.connect("python/python@localhost:1521/xe")
cur = conn.cursor()
e_id=6
sql=f"""
    delete from emp where e_id='{e_id}'
"""

cur.execute(sql)
print(cur.rowcount)
cur.execute("commit")
conn.close()