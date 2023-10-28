import pymysql as database

conn = database.connect(
  host="localhost",
  user="root",
  password="",
  database="db_pegawai"
)
print(conn,"sukses")

mycursor = conn.cursor()

# insert data
insert = "INSERT INTO pegawai (nama, nik,jabatan) VALUES (%s, %s, %s)"
val = [
  ('Peter', '2222','UPT'),
  ('Amy', '3333','UPT')
]
mycursor.executemany(insert, val)
conn.commit()
print(mycursor.rowcount, "berhasil disimpan.")

# menampilkan data
mycursor.execute("SELECT * FROM pegawai")
data = mycursor.fetchall()
print(data)

# edit data
update = "UPDATE pegawai SET nama = 'zen',nik='', jabatan='' WHERE id = '1'"
mycursor.execute(update)
conn.commit()
print(mycursor.rowcount, "berhasil edit")

# hapus data
delete = "DELETE FROM pegawai WHERE id = '10'"
mycursor.execute(delete)
conn.commit()
print(mycursor.rowcount, "data berhasil dihapus")