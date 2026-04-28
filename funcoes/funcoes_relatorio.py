import sqlite3
from views.utils import *
from views.tela_clientes import *
import funcoes.funcoes_cadastros as fc
import funcoes.funcoes_relbanco as fb

def total_clientes():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(id_clientes) FROM clientes")
    resultado_clientes = cursor.fetchone()
            
    conn.close()
            
    resultado_clientes = resultado_clientes[0]
    return resultado_clientes

def total_estoque():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(id_estoque) FROM estoque")
    
    resultado_estoque = cursor.fetchone()
    
    conn.close()
    
    resultado_estoque = resultado_estoque[0]
    return resultado_estoque
