import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password test)"
cursor.execute(create_table)

user = (1, 'ahmet', 'asdf')
insert_query = "INSERT INTO users values (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'mehmet', 'asdf'),
    (3, 'fehmi', '1234')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()