import cx_Oracle
    
conn = cx_Oracle.connect("python/python@localhost:1521/xe")
cur = conn.cursor()
i=5
e_id=i
e_name=i
gen=i
addr=i
sql=f"""
    insert into emp(e_id,e_name,gen,addr)
    values('{e_id}','{e_name}','{gen}','{addr}')
"""

cur.execute(sql)
print(cur.rowcount)
cur.execute("commit")

conn.close()
