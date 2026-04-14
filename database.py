import sqlite3
def conectar():
    return sqlite3.connect("database.db")

def criar_tabelas(conn):
    cursor = conn.cursor()
    
    #Tabela clientes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        numero TEXT, 
        cpf TEXT,
        endereco TEXT,
        email TEXT
    )
    """)
    
    #Tabela estoque
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigobarras TEXT,
        nome TEXT,
        preco REAL,
        quantidade INTEGER,
        categoria TEXT,
        qntminima TEXT,
        unidade TEXT,
        vencimento TEXT
    )
    """)
    
    #Tabela vendas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER,
        quantidade INTEGER, 
        total REAL,
        data_hora INTEGER
    )
    """)
    
    conn.commit()