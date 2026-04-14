import customtkinter as ctk
from tkinter import messagebox
import sqlite3
#Paleta de cores:
FUNDO = "#0F172A"
FUNDO_SECUNDARIO = "#1E293B"
BTN_CONFIRMAR = "#10B981" 
BTN_CANCELAR = "#F43F5E"  
BTN_NAV = "#6366F1"      
BTN_ACAO = "#38BDF8"   
TEXTO_PRINCIPAL = "#F8FAFC" 
TEXTO_SUBTITULO = "#94A3B8" 

def aviso_manutencao():
    messagebox.showwarning("Estamos em manutenção", "Estamos em manutenção para melhor atendermos a você")

def obter_todos_clientes():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, email, numero, cpf, endereco FROM clientes")
    dados = cursor.fetchall() # Retorna uma lista de tuplas
    conn.close()
    return dados