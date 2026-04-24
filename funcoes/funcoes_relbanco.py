import sqlite3
from views.utils import *
from views.tela_clientes import *
import funcoes.funcoes_cadastros as fc

def buscar_clientes(event, instancia_tela):
    termo = instancia_tela.entrada_pesquisa.get()
    atualizar_tabela_clientes(instancia_tela, termo)

def atualizar_tabela_clientes(instancia_tela, termo=""):
    for item in instancia_tela.tabela.get_children():
        instancia_tela.tabela.delete(item)
        
    dados = buscar_clientes_db(termo)
    
    for linha in dados:
        instancia_tela.tabela.insert("", "end", values=linha)
        
def buscar_clientes_db(nome):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id_clientes, nome, email, numero, cpf, endereco FROM clientes WHERE nome LIKE ?", (f'%{nome}%',))
        dados = cursor.fetchall()
        conn.close()
        return dados
    
def buscar_estoque(event, instancia_tela):
    termo = instancia_tela.entrada_pesquisa.get()
    atualizar_tabela_estoque(instancia_tela, termo)
    
def atualizar_tabela_estoque(instancia_tela, termo=""):
    for item in instancia_tela.tabela.get_children():
        instancia_tela.tabela.delete(item)
    
    dados = buscar_estoque_db(termo)
    
    for linha in dados:
        instancia_tela.tabela.insert("", "end", values=linha)
    
def buscar_estoque_db(nome):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id_estoque, codigobarras, nome, preco, quantidade, categoria, vencimento FROM estoque WHERE nome LIKE ?", (f'%{nome}%',))
        dados = cursor.fetchall()
        conn.close()
        return dados
    except sqlite3.Error as e:
        print(f'Erro no banco de dados: {e}')
        raise e
        

# --- FUNÇÃO PARA DELETAR ---
def deletar_registro_no_banco(id_usuario):
    # Esta função recebe um ID e apaga do banco de dados.
    try:
        conexao = sqlite3.connect('database.db')
        cursor = conexao.cursor()
    
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
    
        conexao.commit()
        conexao.close()
    except sqlite3.Error as e:
        print(f'Erro no banco de dados: {e}')
        raise e
    
def atualizar_produto_db(id_produto, dados_novos):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = """
            UPDATE estoque 
            SET codigobarras = ?, nome = ?, preco = ?, quantidade = ?, categoria = ?, qntminima = ?, unidade = ?, vencimento = ?
            WHERE id_estoque = ?
        """
        cursor.execute(query, dados_novos)
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f'Erro no banco de dados: {e}')
        raise e