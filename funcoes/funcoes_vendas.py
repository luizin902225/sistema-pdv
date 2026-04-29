import sqlite3
from views.utils import *
from views.tela_clientes import *
import funcoes.funcoes_cadastros as fc
import funcoes.funcoes_relatorio as fr
import funcoes.funcoes_relbanco as fb
from views.tela_venda import *

FUNDO = "#0F172A"
FUNDO_SECUNDARIO = "#1E293B"
BTN_CONFIRMAR = "#10B981" 
BTN_CANCELAR = "#F43F5E"  
BTN_NAV = "#6366F1"      
BTN_ACAO = "#38BDF8"   
TEXTO_PRINCIPAL = "#F8FAFC" 
TEXTO_SUBTITULO = "#94A3B8"

# Função responsável por fazer pesquisa do código e adição nas label ( código, nome, preço )
def adicionar_produto(event, venda):
    codigo = venda.entrada_codigobarras.get()

    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM estoque WHERE codigobarras LIKE ?", (f'%{codigo}%',))
        dados = cursor.fetchone()

        if dados:
            venda.entrada_nome.configure(text=str(dados[0]))
            venda.entrada_codigobarras.delete(0, 'end')
            
            venda.qnt_prod += 1
            venda.entrada_qnt.configure(text=f'{venda.qnt_prod}')
        else:
            venda.entrada_nome.configure(text="Produto não encontrado")
            
        cursor.execute("SELECT nome, preco FROM estoque WHERE codigobarras = ?", (codigo,))
        produto = cursor.fetchone()
        
        if produto:
            
            nome, preco = produto[0], produto[1]

            
            # 1. Criar um frame para a linha (horizontal)
            linha = ctk.CTkFrame(venda.listadecompras, fg_color="transparent", height=40)
            linha.pack(fill="x", pady=2)
            
            # 2. Adicionar as informações na linha
            lbl_nome = ctk.CTkLabel(linha, text=nome, text_color="black", font=("Segoe UI", 14, "bold"))
            lbl_nome.pack(side="left", padx=10)
            
            lbl_preco = ctk.CTkLabel(linha, text_color="black", text=f"R$ {preco:.2f}", font=("Segoe UI", 14, "bold"))
            lbl_preco.pack(side="right", padx=10)
            

            
            # Limpar para o próximo
            venda.entrada_codigobarras.delete(0, 'end')
            
        else:
            venda.entrada_nome.configure(text="Não encontrado")
        
        conn.close()
            
    except Exception as e:
        print(f"Erro: {e}")
        
    except sqlite3.Error as e:
        print(f'Erro no banco adicionar_produto: {e}')
