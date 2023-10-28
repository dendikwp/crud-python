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