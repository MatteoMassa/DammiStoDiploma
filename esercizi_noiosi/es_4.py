import sqlite3

# 2. Connessione: crea il file 'scuola.db' se non esiste
conn = sqlite3.connect('scuola.db')
# 3. Creazione Cursore
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Studenti (
    Matricola INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Esami (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Matricola INTEGER NOT NULL,
    Corso TEXT NOT NULL,
    Voto INTEGER,
    FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
)
""")

# Inserimento studenti
cursor.execute("INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)", (101, "Mario", "Rossi"))
cursor.execute("INSERT INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?)", (102, "Lucia", "Bianchi"))

# Inserimento esami per Matricola 101
cursor.execute("INSERT INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?)", (101, "Matematica", 28))
cursor.execute("INSERT INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?)", (101, "Informatica", 30))
cursor.execute("INSERT INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?)", (101, "Fisica", 27))

# Inserimento esami per Matricola 102
cursor.execute("INSERT INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?)", (102, "Matematica", 28))
cursor.execute("INSERT INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?)", (102, "Informatica", 30))
cursor.execute("INSERT INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?)", (102, "Fisica", 27))

# Inserimento esami per Matricola 102
cursor.executemany("INSERT INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?)", [(102, "Matematica", 28), (102, "Informatica", 30), (102, "Fisica", 27)])

# 1. Elenco di tutti gli studenti
cursor.execute("SELECT Matricola, Nome, Cognome FROM Studenti")
studenti = cursor.fetchall()
print("Elenco studenti:")
for studente in studenti:
    print(studente)

# 2. Elenco dei corsi e voti sostenuti da uno studente specifico (matricola 101)
cursor.execute("SELECT Corso, Voto FROM Esami WHERE Matricola = ?", (101,))
esami_101 = cursor.fetchall()
print("\nEsami sostenuti da studente 101:")
for esame in esami_101:
    print(esame)

# 3. Numero di esami sostenuti per ciascuno studente
cursor.execute("SELECT Matricola, COUNT(*) FROM Esami GROUP BY Matricola")
esami_per_studente = cursor.fetchall()
print("\nNumero di esami per ciascuno studente:")
for record in esami_per_studente:
    print(record)








conn.commit()
conn.close()