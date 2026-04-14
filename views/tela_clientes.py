import sqlite3
import tkinter as tk
from  tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
from views.utils import aviso_manutencao, obter_todos_clientes
import funcoes.funcoes_cadastros as fc
import funcoes.funcoes_relbanco as fp

#Paleta de cores:
FUNDO = "#0F172A"
FUNDO_SECUNDARIO = "#1E293B"
BTN_CONFIRMAR = "#10B981" 
BTN_CANCELAR = "#F43F5E"  
BTN_NAV = "#6366F1"      
BTN_ACAO = "#38BDF8"   
TEXTO_PRINCIPAL = "#F8FAFC" 
TEXTO_SUBTITULO = "#94A3B8"

class MenuClientes(ctk.CTkFrame):
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
        
        # Bind do Enter 
        self.entrada_pesquisa.bind("<Return>", lambda e: fp.buscar(e, self))
        self.entrada_pesquisa.bind("<KeyRelease>", lambda e: fp.buscar(e, self))

        # Botões
        botoes = [
            ("🔍​Buscar", lambda: fp.buscar_clientes(None, self), BTN_NAV), # Chamada corrigida
            ("➕​Cadastrar", lambda: fc.TelaCadastro(self), BTN_NAV),
            ("🖊️​Editar", lambda: aviso_manutencao(), BTN_NAV),
            ("Fiados", lambda: aviso_manutencao(), BTN_NAV),
            ("Notas em aberto", lambda: aviso_manutencao(), BTN_NAV)
        ]  
        for texto, comando, cor in botoes:
            btn = ctk.CTkButton(topo, font=("Segoe UI", 16), text=texto, command=comando, fg_color=cor, text_color=TEXTO_PRINCIPAL)
            btn.pack(side="left", pady=10, padx=10)
            
        # Estilo
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", rowheight=30)
        estilo.configure("Treeview.Heading", background="#1f538d", foreground="white")

        colunas = ("id", "nome", "email", "numero", "cpf", "endereco")
        self.tabela = ttk.Treeview(resto, columns=colunas, show="headings")

        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("endereco", text="Endereço")
        self.tabela.heading("email", text="Email")
        self.tabela.heading("numero", text="Número de celular")
        self.tabela.heading("cpf", text="CPF")

        self.tabela.column("id", width=40, anchor="center", stretch=False)
        self.tabela.column("nome", width=200, minwidth=150)
        self.tabela.column("email", width=180, minwidth=150)
        self.tabela.column("numero", width=100, anchor="center")
        self.tabela.column("cpf", width=100, anchor="center")
        self.tabela.column("endereco", width=250)

        self.tabela.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Carga inicial
        fp.atualizar_tabela_clientes(self, "")
