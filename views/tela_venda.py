import sqlite3
import tkinter as tk
from  tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
from views.utils import aviso_manutencao
import funcoes.funcoes_cadastros as fc
import funcoes.funcoes_relbanco as fb

#Paleta de cores:
FUNDO = "#0F172A"
FUNDO_SECUNDARIO = "#1F2938"
BTN_CONFIRMAR = "#10B981" 
BTN_CANCELAR = "#F43F5E"  
BTN_NAV = "#6366F1"      
BTN_ACAO = "#38BDF8"   
TEXTO_PRINCIPAL = "#F8FAFC" 
TEXTO_SUBTITULO = "#94A3B8"

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
        fonte_geral = ctk.CTkFont("Segoe UI", 14, "bold")
        # Frame
        superior = ctk.CTkFrame(self, fg_color="transparent") # Frame superior
        superior.pack(side="top", fill="both", expand=True)
        inferior = ctk.CTkFrame(self, fg_color="transparent", height=100) # Frame inferior
        inferior.pack(side="top", fill="x")
        
        frame1 = ctk.CTkFrame(superior, fg_color="green", corner_radius=0, width=800)
        frame1.pack(fill="both", expand=True, side="left")
        frame2 = ctk.CTkFrame(superior, fg_color="gray", corner_radius=0)
        frame2.pack(fill="both", expand=True, side="left")
        
        frame3 = ctk.CTkFrame(inferior, fg_color="blue", corner_radius=0, width=800)
        frame3.pack(fill="both", expand=True, side="left")
        frame4 = ctk.CTkFrame(inferior, fg_color="red", corner_radius=0)
        frame4.pack(fill="both", expand=True, side="left")
        
        # Entradas ( Código de barras, Nome )
        
        entrada_codigobarras = ctk.CTkEntry(frame3, width=500, height=45, font=fonte_cod, fg_color="white", border_color="white", font_color="black")
        entrada_codigobarras.place(x=20, y=50)