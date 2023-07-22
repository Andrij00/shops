import sqlite3

conn = sqlite3.connect("Artistc.db") # з'єднання з базою даних (БД)
cursor = conn.cursor() #курсор (посилання) на БД

cursor.execute("SELECT * FROM artists")
data = cursor.fetchall()
print(data[0][1])
# Запитання 1. Інформація про скількох художників представлена у базі даних?
print(len(data))

# Запитання 2. Скільки жінок (Female) у базі?
cursor.execute('''SELECT * FROM artists WHERE gender=="Female" AND nationality=="American"''')
data = cursor.fetchall()
print(len(data))

# Запитання 3. Скільки людей у базі даних народилися до 1900 року?
cursor.execute('''SELECT * FROM artists WHERE "Birth Year"<1900''')
data = cursor.fetchall()
print(len(data))

# Запитання 4*. Як звати найстаршого художника?
cursor.execute('''SELECT name FROM artists ORDER BY "Birth Year"''')
data = cursor.fetchone()
print(data[0])


# cursor.execute('''INSERT INTO artists
#         (Name, Nationality, Gender, "Birth Year")
#         VALUES ("Пікассо", "espanian", "male", 1881)
#     ''')
cursor.execute('''UPDATE artists SET "Artist ID" = 579
               WHERE Name == "Пікассо"
    ''')

conn.commit() # підтвердження змін в БД
conn.close() # закриваємо з'єднання з БД