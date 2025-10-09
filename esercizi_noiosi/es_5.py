import sqlite3

# 2. Connessione: crea il file 'libreria.db' se non esiste
conn = sqlite3.connect('libreria.db')
# 3. Creazione Cursore
cursor = conn.cursor()