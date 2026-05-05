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
            
        cursor.execute("SELECT nome, preco, quantidade FROM estoque WHERE codigobarras = ?", (codigo,))
        produto = cursor.fetchone()
        
        if produto:
            
            nome, preco, quantidade = produto[0], produto[1], produto[2]

            # 1. Criar um frame para a linha (horizontal)
            linha = ctk.CTkFrame(venda.listadecompras, fg_color="transparent", height=40)
            linha.pack(fill="x", pady=2)
            
            # 2. Adicionar as informações na linha
            lbl_nome = ctk.CTkLabel(linha, text=nome, text_color="black", font=("Segoe UI", 14, "bold"))
            lbl_nome.pack(side="left", padx=10)
            
            lbl_preco = ctk.CTkLabel(linha, text_color="black", text=f"R$ {preco:.2f}".replace('.', ','), font=("Segoe UI", 14, "bold"))
            lbl_preco.pack(side="right", padx=10)
            
            produto_lista = {
                "nome": nome,
                "preco": preco,
                "quantidade": 1
            }
            venda.itens_carrinho.append(produto_lista)
            print(venda.itens_carrinho)
            venda.qnt_prod += 1
            venda.entrada_nome.configure(text=nome)
            venda.entrada_preco.configure(text=f'R$ {preco:.2f}'.replace('.', ','))
            venda.entrada_qnt.configure(text=f'{venda.qnt_prod}')

            venda.total = sum(item["preco"] for item in venda.itens_carrinho)
            venda.entrada_valor_total.configure(text=f"R$ {venda.total:.2f}".replace(".", ","))
            venda.entrada_quantidade_comprada.configure(text="1")
            
            # Limpar para o próximo
            venda.entrada_codigobarras.delete(0, 'end')
            
            
        else:
            venda.entrada_nome.configure(text="Não encontrado")
        
        conn.close()
            
    except sqlite3.Error as e:
        print(f'Erro no banco adicionar_produto: {e}')

def procura_dados():
    
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    
        cursor.execute("SELECT nome FROM clientes ORDER BY nome ASC")
        dados = cursor.fetchall()
        
        conn.close()
        return [linha[0] for linha in dados]
    
    except sqlite3.Error as e:
        print(f'Erro no banco da função procura_dados: {e}')
        
def tela_finalizar(self):
    finalizar = ctk.CTkToplevel(self)
    finalizar.geometry("650x400")
    finalizar.attributes("-topmost", True)
    finalizar.grab_set()
    finalizar.configure(fg_color=FUNDO_SECUNDARIO)
    
    fonte_titulo = ctk.CTkFont("Segoe UI", 22, "bold")
    fonte_cod = ctk.CTkFont("Segoe UI", 22, "bold")
    fonte_geral = ctk.CTkFont("Segoe UI", 15, "bold")
    
    dados = procura_dados()
    
    # Nome do cliente
    cliente = ctk.CTkLabel(finalizar, text="Cliente", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
    cliente.place(x=20, y=10)
    self.opcao_cliente = ctk.StringVar(value="CONSUMIDOR PADRÃO")
    self.entrada_cliente = ctk.CTkOptionMenu(finalizar,
                                            values=dados,
                                            width=430,
                                            height=35,
                                            fg_color="white",
                                            text_color="black",
                                            font=fonte_cod, 
                                            dropdown_font=fonte_cod,
                                            variable=self.opcao_cliente)
    self.entrada_cliente.place(x=20, y=40)
    
    #Forma de pagamento
    pagamento_label = ctk.CTkLabel(finalizar, text="Forma de Pagamento", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
    pagamento_label.place(x=480, y=10)
    
    self.opcao_pagamento = ctk.StringVar(value="DINHEIRO")
    self.forma_pagamento = ctk.CTkOptionMenu(finalizar,
                                             values=["DINHEIRO", "DÉBITO", "CRÉDITO", "PIX", "FIADO"],
                                             width=55,
                                             height=35,
                                             fg_color="white",
                                             text_color="black",
                                             dropdown_font=("Segoi UI", 18, "bold"),
                                             variable=self.opcao_pagamento)
    self.forma_pagamento.place(x=480, y=40)
    
    # Valor Recebido
    recebido_label = ctk.CTkLabel(finalizar, text="Valor recebido:", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
    recebido_label.place(x=20, y=150)

    self.recebido_valor = ctk.CTkEntry(finalizar,
                                       width=100, 
                                       height=35,
                                       fg_color="white",
                                       text_color="black",
                                       font=fonte_cod,
                                       placeholder_text="R$ 0,00",
                                       placeholder_text_color="black")
    self.recebido_valor.place(x=20, y=180)
    
    valor_texto = self.recebido_valor.get()
    
    if valor_texto.strip() == "":
        messagebox.showinfo("Adicione algum produto!", "Adicione algum produto antes de finalizar a venda")
        return
    
    valor_recebido = float(self.recebido_valor.get().replace(",", "."))
    valor_troco = self.total - valor_recebido
    
    print(f'RELATÓRIO DE VENDA: Valor total: R$ {self.total}, Recebido: R$ {valor_recebido}, Troco: R$ {valor_troco}')
    
    # Valor total
    
    
    
    # Troco
    
    # Botão finalizar
    
    finalizar.mainloop()
