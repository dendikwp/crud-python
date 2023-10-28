import pymysql as database

conn = database.connect(
  host="localhost",
  user="root",
  password="",
  database="db_pegawai"
)

print(conn,"sukses")