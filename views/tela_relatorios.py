import sqlite3
import tkinter as tk
from  tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
import funcoes.funcoes_cadastros as fc
import funcoes.funcoes_relbanco as fb
import funcoes.funcoes_relatorio as fr

#Paleta de cores:
FUNDO = "#0F172A"
FUNDO_SECUNDARIO = "#1E293B"
BTN_CONFIRMAR = "#10B981" 
BTN_CANCELAR = "#F43F5E"  
BTN_NAV = "#6366F1"      
BTN_ACAO = "#38BDF8"   
TEXTO_PRINCIPAL = "#F8FAFC" 
TEXTO_SUBTITULO = "#94A3B8"

class MenuRelatorios(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.conn = controller.conn
        self.configure(fg_color=FUNDO)
        fonte_titulo = ctk.CTkFont("Segoe UI", 22, "bold")
        fonte_geral = ctk.CTkFont("Segoe UI", 14, "bold")
        # Frame

        resto = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        resto.pack(fill="both", expand=True)
        
        frame_clientes = ctk.CTkFrame(resto, fg_color="transparent", corner_radius=0)
        frame_clientes.pack(fill="both", expand=True, side="left")
        frame_estoque = ctk.CTkFrame(resto, fg_color="transparent", corner_radius=0)
        frame_estoque.pack(fill="both", expand=True, side="left")
        frame_vendas = ctk.CTkFrame(resto, fg_color="transparent", corner_radius=0)
        frame_vendas.pack(fill="both", expand=True, side="left")
        
        # Títulos 
        titulo_clientes = ctk.CTkLabel(frame_clientes, text_color=TEXTO_PRINCIPAL, text="CLIENTES", font=fonte_titulo)
        titulo_clientes.place(y=25, relx=0.5, anchor="center")
        titulo_estoque = ctk.CTkLabel(frame_estoque, text_color=TEXTO_PRINCIPAL, text="ESTOQUE", font=fonte_titulo)
        titulo_estoque.place(y=25, relx=0.5, anchor="center")
        titulo_vendas = ctk.CTkLabel(frame_vendas, text_color=TEXTO_PRINCIPAL, text="VENDAS", font=fonte_titulo)
        titulo_vendas.place(y=25, relx=0.5, anchor="center")
        
        # Variáveis da contagem
        
        clientes = fr.total_clientes()
        estoque = fr.total_estoque()
        
        # Cliente
        
        clientes_total = ctk.CTkLabel(frame_clientes, font=fonte_geral, text_color=TEXTO_PRINCIPAL, text=f"Total de clientes: {clientes}")
        clientes_total.place(y=100, relx=0.05)
        
        # Estoque
        
        estoque_total = ctk.CTkLabel(frame_estoque, font=fonte_geral, text_color=TEXTO_PRINCIPAL, text=f'Total de produtos em estoque: {estoque}')
        estoque_total.place(y=100, relx=0.05)
        
        # Vendas
        
        vendas_total = ctk.CTkLabel(frame_vendas, font=fonte_geral, text_color=TEXTO_PRINCIPAL, text=f'Total de vendas feitas: (Em manutenção)')
        vendas_total.place(y=100, relx=0.05)