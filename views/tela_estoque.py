import sqlite3
import tkinter as tk
from  tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
from views.utils import aviso_manutencao
import funcoes.funcoes_cadastros as fc
import funcoes.funcoes_relbanco as fp

#Paleta de cores:
FUNDO = "#0F172A"
FUNDO_SECUNDARIO = "#1F2938"
BTN_CONFIRMAR = "#10B981" 
BTN_CANCELAR = "#F43F5E"  
BTN_NAV = "#6366F1"      
BTN_ACAO = "#38BDF8"   
TEXTO_PRINCIPAL = "#F8FAFC" 
TEXTO_SUBTITULO = "#94A3B8"

class MenuEstoque(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.conn = controller.conn
        self.configure(fg_color=FUNDO)
        # Frame
        topo = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0, height=80)
        topo.pack(fill="x")
        resto = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        resto.pack(fill="both", expand=True)
        
        # Barra de pesquisa
        self.entrada_pesquisa = ctk.CTkEntry(topo, placeholder_text="Digite aqui o nome...", font=("Segoe UI", 14), width=480, height=35)
        self.entrada_pesquisa.pack(side="left", padx=20, pady=20)
        
        self.entrada_pesquisa.bind("<Return>", lambda e: fp.buscar_estoque(e, self))
        self.entrada_pesquisa.bind("<KeyRelease>", lambda e: fp.buscar_estoque(e, self))
        
        botoes = [
            ("🔍​Buscar", lambda: fp.buscar_estoque(None, self), BTN_NAV),
            ("➕​Novo", lambda: fc.NovoProduto(self), BTN_NAV),
            ("🖊️​Editar", self.abrir_edicao, BTN_NAV),
            ("🗑️ Deletar", self.deletar_item, BTN_CANCELAR)
        ]
        
        for nome, comando, cor in botoes:
            btn = ctk.CTkButton(topo, text=nome, command=comando, fg_color=cor, text_color=TEXTO_PRINCIPAL, font=("Segoe UI", 16))
            btn.pack(side="left", padx=10, pady=10)
        
        tabela = ttk.Style()
        tabela.theme_use("clam")
        tabela.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", rowheight=30)
        tabela.configure("Treeview.Heading", background="#1f538d", foreground="white")
        
        colunas = ("id", "codigobarras", "nome", "preco", "quantidade", "categoria", "vencimento")
        self.tabela = ttk.Treeview(resto, columns=colunas, show="headings")
        
        self.tabela.heading("id", text="ID")
        self.tabela.heading("codigobarras", text="Código de barras")
        self.tabela.heading("nome", text="Nome do produto")
        self.tabela.heading("preco", text="Valor")
        self.tabela.heading("quantidade", text="Estoque")
        self.tabela.heading("categoria", text="Categoria")
        self.tabela.heading("vencimento", text="Data de vencimento")
        
        self.tabela.column("id", width=40, anchor="center", stretch=False)
        self.tabela.column("codigobarras", width=200, minwidth=150)
        self.tabela.column("nome", width=200, minwidth=150)
        self.tabela.column("preco", width=80, anchor="center")
        self.tabela.column("quantidade", width=40, anchor="center")
        self.tabela.column("categoria", width=100, anchor="center")
        self.tabela.column("vencimento", width=100, anchor="center")
        
        self.tabela.pack(fill="both", expand=True, padx=20, pady=20)
        
        fp.atualizar_tabela_estoque(self, "")
        
    def deletar_item(self):
        # 1. Verifica se há algo selecionado
        item_selecionado = self.tabela.selection()
        
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Por favor, selecione um produto na tabela para deletar.")
            return

        # 2. Pega os dados da linha (o ID é o primeiro valor: index 0)
        valores = self.tabela.item(item_selecionado)['values']
        id_produto = valores[0]
        nome_produto = valores[2]

        # 3. Confirmação do usuário
        confirmar = messagebox.askyesno("Confirmar Exclusão", f"Deseja realmente deletar o produto:\n{nome_produto}?")
        
        if confirmar:
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM estoque WHERE id = ?", (id_produto,))
                self.conn.commit()
                
                # 4. Remove da interface e avisa o usuário
                self.tabela.delete(item_selecionado)
                messagebox.showinfo("Sucesso", "Produto removido com sucesso!")
                
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível deletar do banco de dados: {e}")
                
    def abrir_edicao(self):
        selecao = self.tabela.selection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um item para editar!")
            return
    
    # Pega os dados da linha clicada
        item_id = selecao[0]
        dados_da_linha = self.tabela.item(item_id)['values']
    
    # Abre a janela passando os dados e a função de atualizar a tabela
        fc.EditarProduto(self, dados_da_linha, lambda: fp.atualizar_tabela_estoque(self, ""), fp.atualizar_produto_db)
