import pymysql as database

conn = database.connect(
  host="localhost",
  user="root",
  password="",
  database="db_pegawai"
)
print(conn,"sukses")

mycursor = conn.cursor()

# edit data
update = "UPDATE pegawai SET nama = 'zen',nik='', jabatan='' WHERE id = '1'"
mycursor.execute(update)
conn.commit()
print(mycursor.rowcount, "berhasil edit")