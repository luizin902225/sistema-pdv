import sqlite3
import tkinter as tk
from  tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
from views.utils import aviso_manutencao
import funcoes.funcoes_cadastros as fc
import funcoes.funcoes_relbanco as fb
import funcoes.funcoes_vendas as fv

#Paleta de cores:
FUNDO = "#0F172A"
FUNDO_SECUNDARIO = "#1F2938"
BTN_CONFIRMAR = "#10B981" 
BTN_CANCELAR = "#F43F5E"  
BTN_NAV = "#6366F1"      
BTN_ACAO = "#38BDF8"   
TEXTO_PRINCIPAL = "#F8FAFC" 
TEXTO_SUBTITULO = "#94A3B8"

#imagem 
imagem_prod = Image.open("imagens/caixa.png")
img = ctk.CTkImage(imagem_prod, size=(200, 200))


class Venda(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.conn = controller.conn
        self.configure(fg_color=FUNDO)
        
        self.grid_columnconfigure(0, weight=1) 
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=2)
        
        fonte_titulo = ctk.CTkFont("Segoe UI", 22, "bold")
        fonte_cod = ctk.CTkFont("Segoe UI", 22, "bold")
        fonte_geral = ctk.CTkFont("Segoe UI", 15, "bold")
        # Frame
        superior = ctk.CTkFrame(self, fg_color="transparent") # Frame superior
        superior.pack(side="top", fill="both", expand=True)
        inferior = ctk.CTkFrame(self, fg_color="transparent", height=100) # Frame inferior
        inferior.pack(side="top", fill="x")
        
        frame1 = ctk.CTkFrame(superior, fg_color="transparent", corner_radius=0, width=800)
        frame1.pack(fill="both", expand=True, side="left")
        frame2 = ctk.CTkFrame(superior, fg_color="transparent", corner_radius=0)
        frame2.pack(fill="both", expand=True, side="left")
        
        frame3 = ctk.CTkFrame(inferior, fg_color="transparent", corner_radius=0, width=800)
        frame3.pack(fill="both", expand=True, side="left")
        frame4 = ctk.CTkFrame(inferior, fg_color="red", corner_radius=0)
        frame4.pack(fill="both", expand=True, side="left")
        
        # Frame 1 - Foto do produto, Lista de compras
        
        foto_produto = ctk.CTkFrame(frame1, fg_color="white", height=455, width=500, corner_radius=0)
        foto_produto.place(x=20, y=20)
        
        ft = ctk.CTkLabel(foto_produto, text=" ", image=img)
        ft.place(relx=0.5, rely=0.5, anchor="center")
        
        titulo_listadecompras = ctk.CTkLabel(frame1, text="Lista de compras", font=("Segoe UI", 18, "bold"), text_color=TEXTO_PRINCIPAL)
        titulo_listadecompras.place(relx=0.75, y=23, anchor="center")
        
        self.listadecompras = ctk.CTkScrollableFrame(frame1, height=425, width=400, corner_radius=0, fg_color="#d8a649")
        self.listadecompras.place(x=560, y=50)
        self.itens_carrinho = []
        
        # Frame 2 - Quantidade, Preço unitário, Preço total
        dados = fv.procura_dados()

        entrada_quantidade = ctk.CTkLabel(frame2, text="Quantidade", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
        entrada_quantidade.place(x=20, y=20)
        self.entrada_quantidade_comprada = ctk.CTkLabel(frame2, text=" ", width=350, height=45, fg_color="white", text_color="black", font=fonte_cod)
        self.entrada_quantidade_comprada.place(x=20, y=50)
        
        entrada_preco_unitario = ctk.CTkLabel(frame2, text="Preço unitário", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
        entrada_preco_unitario.place(x=20, y=100)
        self.entrada_preco = ctk.CTkLabel(frame2, text=" ", width=350, height=45, fg_color="white", text_color="black", font=fonte_cod)
        self.entrada_preco.place(x=20, y=130)
        
        entrada_total_valor = ctk.CTkLabel(frame2, text="Valor total", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
        entrada_total_valor.place(x=20, y=180)
        self.entrada_valor_total = ctk.CTkLabel(frame2,
                                                text=" ",
                                                width=350,
                                                height=45,
                                                fg_color="white",
                                                text_color="black",
                                                font=fonte_cod)
        self.entrada_valor_total.place(x=20, y=210)
        
        entrada_cliente = ctk.CTkLabel(frame2, text="Cliente", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
        entrada_cliente.place(x=20, y=260)
        self.entrada_cliente = ctk.CTkOptionMenu(frame2,
                                                values=dados,
                                                width=350,
                                                height=45,
                                                fg_color="white",
                                                text_color="black",
                                                font=fonte_cod, 
                                                dropdown_font=fonte_cod)
        self.entrada_cliente.place(x=20, y=290)
        
        # Frame 3 - Código de barras, Nome

        self.qnt_prod = 0
        
        codigo_label = ctk.CTkLabel(frame3, text="Código de barras", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
        codigo_label.place(x=20, y=10)
        self.entrada_codigobarras = ctk.CTkEntry(frame3, 
                                            width=600, 
                                            height=45, 
                                            font=fonte_cod, 
                                            fg_color="white", 
                                            border_color="white", 
                                            text_color="black", 
                                            corner_radius=0)
        self.entrada_codigobarras.place(x=20, y=40)
        
        self.entrada_codigobarras.bind('<Return>', lambda event: fv.adicionar_produto(event, self))
        
        nome_produto = ctk.CTkLabel(frame3, text="Nome do produto", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
        nome_produto.place(x=20, y=90)
        self.entrada_nome = ctk.CTkLabel(frame3, width=600, height=45, font=fonte_cod, fg_color="white", text_color="black", text=" ")
        self.entrada_nome.place(x=20, y=120)
        
        qnt_produto = ctk.CTkLabel(frame3, text="Qnt. do produto", text_color=TEXTO_PRINCIPAL, font=fonte_geral)
        qnt_produto.place(x=730, y=10)
        self.entrada_qnt = ctk.CTkLabel(frame3, text=f'{self.qnt_prod}', font=fonte_cod, text_color="black", fg_color="white", width=130, height=45)
        self.entrada_qnt.place(x=730, y=40)
        