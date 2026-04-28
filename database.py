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
        cpf TEXT,
        endereco TEXT,
        email TEXT
    )
    """)
    
    #Tabela estoque
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estoque (
        id_estoque INTEGER PRIMARY KEY AUTOINCREMENT,
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
        id_vendas INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER,
        quantidade INTEGER, 
        total REAL,
        data_hora INTEGER
    )
    """)
    cursor.executescript("""
    INSERT INTO estoque (codigobarras, nome, preco, quantidade, categoria, qntminima, unidade, vencimento) VALUES
        ('7891000000011', 'Arroz 5kg', 25.90, 50, 'Alimentos', '10', 'UN', '2026-12-10'),
        ('7891000000012', 'Feijão 1kg', 7.50, 80, 'Alimentos', '20', 'UN', '2026-10-15'),
        ('7891000000013', 'Macarrão 500g', 4.20, 100, 'Alimentos', '30', 'UN', '2026-09-01'),
        ('7891000000014', 'Óleo de Soja 900ml', 8.99, 60, 'Alimentos', '15', 'UN', '2026-11-20'),
        ('7891000000015', 'Açúcar 1kg', 4.50, 70, 'Alimentos', '20', 'UN', '2027-01-05'),
        ('7891000000016', 'Sal 1kg', 2.00, 90, 'Alimentos', '25', 'UN', '2027-05-10'),
        ('7891000000017', 'Café 500g', 12.99, 40, 'Alimentos', '10', 'UN', '2026-08-18'),
        ('7891000000018', 'Leite 1L', 5.30, 120, 'Bebidas', '30', 'UN', '2026-07-01'),
        ('7891000000019', 'Refrigerante 2L', 9.00, 55, 'Bebidas', '15', 'UN', '2026-09-25'),
        ('7891000000020', 'Suco 1L', 6.50, 65, 'Bebidas', '20', 'UN', '2026-08-30'),

        ('7891000000021', 'Detergente 500ml', 2.80, 75, 'Limpeza', '20', 'UN', '2027-02-10'),
        ('7891000000022', 'Sabão em pó 1kg', 10.90, 45, 'Limpeza', '10', 'UN', '2027-03-15'),
        ('7891000000023', 'Amaciante 2L', 14.50, 35, 'Limpeza', '10', 'UN', '2027-04-01'),
        ('7891000000024', 'Água sanitária 1L', 3.50, 80, 'Limpeza', '20', 'UN', '2027-06-20'),
        ('7891000000025', 'Esponja', 1.50, 150, 'Limpeza', '50', 'UN', '2030-01-01'),

        ('7891000000026', 'Shampoo 350ml', 12.00, 40, 'Higiene', '10', 'UN', '2027-08-10'),
        ('7891000000027', 'Condicionador 350ml', 13.00, 38, 'Higiene', '10', 'UN', '2027-08-10'),
        ('7891000000028', 'Sabonete', 2.50, 120, 'Higiene', '30', 'UN', '2027-09-15'),
        ('7891000000029', 'Pasta de dente', 4.00, 90, 'Higiene', '25', 'UN', '2027-10-05'),
        ('7891000000030', 'Papel higiênico 12un', 18.00, 60, 'Higiene', '15', 'UN', '2030-01-01');
    """)
    
    cursor.executescript("""
    INSERT INTO clientes (nome, numero, cpf, endereco, email) VALUES
        ('João Silva', '31991234567', '123.456.789-00', 'Rua A, 123 - BH', 'joao@gmail.com'),
        ('Maria Oliveira', '31992345678', '234.567.890-11', 'Rua B, 456 - BH', 'maria@gmail.com'),
        ('Carlos Souza', '31993456789', '345.678.901-22', 'Rua C, 789 - BH', 'carlos@gmail.com'),
        ('Ana Santos', '31994567890', '456.789.012-33', 'Rua D, 321 - BH', 'ana@gmail.com'),
        ('Pedro Costa', '31995678901', '567.890.123-44', 'Rua E, 654 - BH', 'pedro@gmail.com'),

        ('Juliana Lima', '31996789012', '678.901.234-55', 'Rua F, 987 - BH', 'juliana@gmail.com'),
        ('Lucas Pereira', '31997890123', '789.012.345-66', 'Rua G, 147 - BH', 'lucas@gmail.com'),
        ('Fernanda Alves', '31998901234', '890.123.456-77', 'Rua H, 258 - BH', 'fernanda@gmail.com'),
        ('Rafael Gomes', '31999012345', '901.234.567-88', 'Rua I, 369 - BH', 'rafael@gmail.com'),
        ('Beatriz Rocha', '31990123456', '012.345.678-99', 'Rua J, 159 - BH', 'beatriz@gmail.com'),

        ('Gabriel Martins', '31991239876', '111.222.333-00', 'Rua K, 753 - BH', 'gabriel@gmail.com'),
        ('Camila Barros', '31992348765', '222.333.444-11', 'Rua L, 852 - BH', 'camila@gmail.com'),
        ('Thiago Ribeiro', '31993457654', '333.444.555-22', 'Rua M, 951 - BH', 'thiago@gmail.com'),
        ('Larissa Freitas', '31994566543', '444.555.666-33', 'Rua N, 357 - BH', 'larissa@gmail.com'),
        ('Bruno Carvalho', '31995675432', '555.666.777-44', 'Rua O, 258 - BH', 'bruno@gmail.com'),

        ('Patrícia Melo', '31996784321', '666.777.888-55', 'Rua P, 159 - BH', 'patricia@gmail.com'),
        ('Eduardo Teixeira', '31997893210', '777.888.999-66', 'Rua Q, 753 - BH', 'eduardo@gmail.com'),
        ('Aline Batista', '31998902109', '888.999.000-77', 'Rua R, 852 - BH', 'aline@gmail.com'),
        ('Diego Nunes', '31999011098', '999.000.111-88', 'Rua S, 951 - BH', 'diego@gmail.com'),
        ('Renata Duarte', '31990120987', '000.111.222-99', 'Rua T, 357 - BH', 'renata@gmail.com');
    """)
    
        
    conn.commit()