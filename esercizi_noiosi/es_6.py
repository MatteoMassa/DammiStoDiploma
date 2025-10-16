import sqlite3

# 2. Connessione: crea il file 'libreria.db' se non esiste
conn = sqlite3.connect('libreria.db')
# 3. Creazione Cursore
cursor = conn.cursor()

def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS autori (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS libri (
        id INTEGER PRIMARY KEY,
        titolo TEXT NOT NULL,
        anno_pubblicazione INTEGER,
        autore_id INTEGER,
        FOREIGN KEY (autore_id) REFERENCES autori(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prestiti (
        id INTEGER PRIMARY KEY,
        libro_id INTEGER FOREIGN KEY,
        utente TEXT NOT NULL,
        data_prestito TEXT NOT NULL,
        data_restituzione TEXT NOT NULL
    )
    ''')

def insert_data():
    #Autori
    cursor.execute("INSERT OR IGNORE INTO autori (id, nome, cognome) VALUES (?, ?, ?)", (1, "Mario", "Rossi") )    

    cursor.execute("INSERT OR IGNORE INTO autori (id, nome, cognome) VALUES (?,?,?)", (2, "Lucia", "Bianchi"))

    cursor.execute("INSERT OR IGNORE INTO autori (id, nome, cognome) VALUES (?,?,?)", (3, "Alessandro", "Verdi"))

    #Libri
    cursor.execute("INSERT OR IGNORE INTO autori (id, titolo, autore_id, anno, genere) VALUES (?,?,?,?,?)", (1, 'Il mistero del castello', 1, 2020, 'Giallo'))

    cursor.execute("INSERT OR IGNORE INTO autori (id, titolo, autore_id, anno, genere) VALUES (?,?,?,?,?)", (2, 'Viaggio nel tempo', 1, 2018, 'Fantascienza'))    

    cursor.execute("INSERT OR IGNORE INTO autori (id, titolo, autore_id, anno, genere) VALUES (?,?,?,?,?)", (3, 'La cucina italiana', 2, 2019, 'Cucina')) 

    cursor.execute("INSERT OR IGNORE INTO autori (id, titolo, autore_id, anno, genere) VALUES (?,?,?,?,?)", (4, 'Storia antica', 3, 2021, 'Storia'))

    cursor.execute("INSERT OR IGNORE INTO autori (id, titolo, autore_id, anno, genere) VALUES (?,?,?,?,?)", (5, 'Romanzo moderno', 3, 2022, 'Narrativa'))

    cursor.execute("INSERT OR IGNORE INTO autori (id, titolo, autore_id, anno, genere) VALUES (?,?,?,?,?)", (6, 'Il ritorno del castello', 1, 2023, 'Giallo'))

    #Prestiti
    cursor.execute("INSERT OR IGNORE INTO prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?,?,?,?,?)", (1, 1, 'Mario Rossi', '2023-01-01', '2023-01-15'))

    cursor.execute("INSERT OR IGNORE INTO prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?,?,?,?,?)", (2, 2, 'Lucia Bianchi', '2023-02-01', None))

    cursor.execute("INSERT OR IGNORE INTO prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?,?,?,?,?)", (3, 3, 'Alessandro Verdi', '2023-03-01', '2023-03-10'))

    cursor.execute("INSERT OR IGNORE INTO prestiti (id, libro_id, utente, data_prestito, data_restituzione) VALUES (?,?,?,?,?)", (4, 4, 'Mario Rossi', '2023-04-01', None))


create_tables()
insert_data()

def query_libri_per_autore(autore_id):
    cursor.execute('''
        SELECT libri.id, libri.titolo, libri.anno_pubblicazione
        FROM libri
        JOIN autori ON libri.autore_id = autori.id
        WHERE autori.id = ?
    ''', (autore_id,))
    return cursor.fetchall()

def query_prestiti_per_utente(utente):
    cursor.execute('''
        SELECT prestiti.id, libri.titolo, prestiti.data_prestito, prestiti.data_restituzione
        FROM prestiti
        JOIN libri ON prestiti.libro_id = libri.id
        WHERE prestiti.utente = ?
    ''', (utente,))
    return cursor.fetchall()

def query_libri_per_genere():
    cursor.execute('''
        SELECT libri.genere, COUNT(*) as numero_libri
        FROM libri
        GROUP BY libri.genere
    ''')
    return cursor.fetchall()

def query_autori_con_piu_libri():
    cursor.execute('''
        SELECT autori.nome, autori.cognome, COUNT(libri.id) as numero_libri
        FROM autori
        LEFT JOIN libri ON autori.id = libri.autore_id
        GROUP BY autori.id
        ORDER BY numero_libri DESC
    ''')
    return cursor.fetchall()

def query_prestiti_non_restituiti():
    cursor.execute('''
        SELECT prestiti.id, libri.titolo, prestiti.utente, prestiti.data_prestito
        FROM prestiti
        JOIN libri ON prestiti.libro_id = libri.id
        WHERE prestiti.data_restituzione IS NULL
    ''')
    return cursor.fetchall()

#Esercizio 6 che pal

