
import sqlite3

conn = sqlite3.connect('test2.db')

# Create a table with an auto-incrementing primary key and a string field for file names
with conn:
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tbl_files( \
        id INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )''')
    conn.commit()

filelist = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhotot.jpg')

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    # Filter the list to get only .txt files
    txt_files = [file for file in filelist if file.endswith('.txt')]
    # Insert each .txt file into the database
    for txt_file in txt_files:
        cur.execute("INSERT INTO tbl_files(col_filename) VALUES (?)", (txt_file,))
    conn.commit()
conn.close()

# Connect to the database and query the .txt files
conn = sqlite3.connect('test2.db')

with conn:
     cur = conn.cursor()
     cur.execute("SELECT col_filename FROM tbl_files")
     varFiles = cur.fetchall()
     # Print the .txt files
     print("Text files in the database:")
     for item in varFiles:
         print(item[0])
conn.close()
