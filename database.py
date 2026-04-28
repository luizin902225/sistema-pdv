import sqlite3
def conectar():
    return sqlite3.connect("database.db")

def criar_tabelas(conn):
    cursor = conn.cursor()
    
    #Tabela clientes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_clientes INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        numero TEXT, 
        cpf TEXT UNIQUE,
        endereco TEXT,
        email TEXT
    )
    """)
    
    #Tabela estoque
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
        id_estoque INTEGER PRIMARY KEY AUTOINCREMENT,
        codigobarras TEXT UNIQUE,
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
        id_vendas INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER,
        quantidade INTEGER, 
        total REAL,
        data_hora INTEGER
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS permissoes (
        id_permissao INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT,
        login TEXT UNIQUE,
        senha TEXT,
        id_permissao INTEGER,
        
        FOREIGN KEY (id_permissao) REFERENCES permissoes(id_permissao)
    )
    """)
    conn.commit()