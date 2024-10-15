import sqlite3

conn = sqlite3.connect('vibecheck.db')
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS patients (
#     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     name VARCHAR(255) NOT NULL,
#     phoneNumber VARCHAR(255) NOT NULL,
#     diagnosis VARCHAR(1024) NOT NULL,
#     contactDate DATE NOT NULL, # add # of days to the current date for next followup date
#     nurseName VARCHAR(255) NOT NULL,
#     authCode VARCHAR(255) NOT NULL,
#     needsFollowUp BOOLEAN NOT NULL
# )
# ''')

cursor.execute('DELETE FROM patients')

# Insert data into the table
cursor.execute(
    '''INSERT INTO patients (firstName, lastName, phoneNumber, secondaryPhoneNumber, email, admissionDate, dischargeDate, contactDate, admissionReason, proceduresPerformed, diagnosis, medicationsGiven, followupInstructions, authCode, needsFollowUp) VALUES ('Ahmed Kamhawy', '6479086123', 'Myocardial Infarction', 'Adam Katt', '123456', TRUE)'''
)

# conn.commit()

# Query the database
cursor.execute('SELECT * FROM patients')
rows = cursor.fetchall()

for row in rows:
  print(row)

conn.close()
