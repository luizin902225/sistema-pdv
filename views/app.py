import customtkinter as ctk
from views.tela_clientes import MenuClientes
from views.tela_estoque import MenuEstoque
from views.utils import aviso_manutencao
import time

data = time.strftime("%d/%m/%Y")

#Paleta de cores:
FUNDO = "#0F172A"
FUNDO_SECUNDARIO = "#1E293B"
BTN_CONFIRMAR = "#10B981" 
BTN_CANCELAR = "#F43F5E"  
BTN_NAV = "#6366F1"      
BTN_ACAO = "#38BDF8"   
TEXTO_PRINCIPAL = "#F8FAFC" 
TEXTO_SUBTITULO = "#94A3B8" 

class App(ctk.CTk):
    def __init__(self, conn):
        super().__init__()
        self.title("Sistema PDV - v1.0")
        self.geometry("1300x800")
        self.configure(fg_color=FUNDO)
        self.after(0, lambda: self.state("zoomed"))
        self.conn = conn
        
        self.topo = ctk.CTkFrame(self, fg_color=FUNDO_SECUNDARIO, corner_radius=0, height=160)
        self.topo.pack(side="top", fill="x")
        self.configurar_topo() 

        self.container_meio = ctk.CTkFrame(self, fg_color="transparent")
        self.container_meio.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (MenuIniciar, MenuClientes, MenuEstoque):
            frame = F(self.container_meio, self) 
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.mostrar_tela(MenuIniciar)

    def configurar_topo(self):
        topo_titulo = ctk.CTkFrame(self.topo, fg_color=FUNDO_SECUNDARIO, height=50)
        topo_titulo.pack(fill="x")
        
        titulo = ctk.CTkLabel(topo_titulo, text="MENU PRINCIPAL", font=("Segoe UI", 20, "bold"), text_color=TEXTO_SUBTITULO)
        titulo.place(relx=0.5, rely=0.5, anchor="center")
        
        topo_botoes = ctk.CTkFrame(self.topo, fg_color="transparent")
        topo_botoes.pack(pady=10)
        
        botoes = [
            ("💰\nVendas", lambda: aviso_manutencao(), BTN_NAV),
            ("👥\nClientes", lambda: self.mostrar_tela(MenuClientes), BTN_NAV),
            ("📦\nEstoque", lambda: self.mostrar_tela(MenuEstoque), BTN_NAV),
            ("📊\nRelatórios", lambda: aviso_manutencao(), BTN_NAV),
            ("⚙️\nAjustes", lambda: aviso_manutencao(), BTN_NAV),
            ("👥\nUsuários", lambda: aviso_manutencao(), BTN_NAV),
            ("🚪\nSair", lambda: self.destroy(), BTN_CANCELAR),
        ]
        
        for texto, comando, cor in botoes:
            btn = ctk.CTkButton(topo_botoes, font=("Segoe UI", 20, "bold"), text=texto, width=110, height=70, fg_color=cor, hover_color="#2A3A4A", text_color=TEXTO_PRINCIPAL, command=comando)
            btn.pack(side="left", padx=10) 
            
        print('Topo funcionando')


    def mostrar_tela(self, tela):
        frame = self.frames[tela]
        frame.tkraise()


class MenuIniciar(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.conn = controller.conn
        
        self.configure(fg_color=FUNDO)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        
        titulo_central = ctk.CTkLabel(self, text="SISTEMA PDV - v1.0", font=("Segoe UI", 50, "bold"), text_color=TEXTO_SUBTITULO)
        titulo_central.place(relx=0.5, rely=0.5, anchor="center")
        print('Menu inicial funcionando')
        
