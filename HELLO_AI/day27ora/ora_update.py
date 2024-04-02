import cx_Oracle
    
conn = cx_Oracle.connect("python/python@localhost:1521/xe")
cur = conn.cursor()
i=5
e_id=6
e_name=i
gen=i
addr=i
sql=f"""
    update emp set e_name= '{e_name}', gen='{gen}',addr='{addr}' where e_id='{e_id}'
"""

cur.execute(sql)
print(cur.rowcount)
cur.execute("commit")
conn.close()