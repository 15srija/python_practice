import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",passwd="123456789")
c=conn.cursor()
c.execute("use database_1")
# c.execute("create table tab_python(name varchar(10),roll_number integer)")
# c.execute("drop table table_py")
# create_table = "create table Table_s(s_id integer not null, s_name varchar(30) not null, s_class varchar(10) not null,primary key(s_id))"
# c.execute(create_table)
insert_values="insert into table_s values(%s,%s,%s)"
v=(101,"reetha","cse")
c.execute(insert_values,v)
conn.commit()