# | ====================================================== |
# | Nesse aquivo está as funções que mais serão utilizadas |
# | Coloquei elas aqui para o código ficar mais legível    |
# | ====================================================== | 

# Importações 
import sqlite3
import tkinter as tk
from  tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
from views.utils import *
from funcoes.funcoes_relbanco import *

# Paleta de cores:
FUNDO = "#0F172A"
FUNDO_SECUNDARIO = "#1E293B"
BTN_CONFIRMAR = "#10B981" 
BTN_CANCELAR = "#F43F5E"  
BTN_NAV = "#6366F1"      
BTN_ACAO = "#38BDF8"   
TEXTO_PRINCIPAL = "#F8FAFC" 
TEXTO_SUBTITULO = "#94A3B8"

# | ====================================== |
# | A função que será utilizada no arquivo | 
# | views/tela_estoque para a criação de   | 
# | novos produtos                         | 
# | ====================================== | 
def NovoProduto(parent):
    cadastro = ctk.CTkToplevel(parent)
    cadastro.title("Cadastrar novo produto")
    cadastro.geometry("400x600") # Ajustei o tamanho para algo mais proporcional
    cadastro.attributes("-topmost", True)
    cadastro.grab_set()
    cadastro.configure(fg_color=FUNDO_SECUNDARIO)
    
    fonte_label = ctk.CTkFont("Segoe UI", 16)
    fonte_entry = ctk.CTkFont("Segoe UI", 14)
    
    # --- FUNÇÃO AUXILIAR PARA CRIAR CAMPOS ---
    def criar_campo(texto, x, y, largura=320):
        lbl = ctk.CTkLabel(cadastro, text=texto, font=fonte_label, text_color=TEXTO_PRINCIPAL)
        lbl.place(x=x, y=y, anchor="w")
        
        ent = ctk.CTkEntry(cadastro, fg_color="white", text_color="black", 
                           font=fonte_entry, width=largura, height=30)
        ent.place(x=x, y=y + 25) # Coloca o entry sempre 25px abaixo do label
        return ent

    # Título da Tela
    titulo = ctk.CTkLabel(cadastro, text="Novo Produto", font=("Segoe UI", 24, "bold"), text_color=TEXTO_PRINCIPAL)
    titulo.place(relx=0.5, y=25, anchor="center")

    # --- GERANDO OS CAMPOS ---
    # Agora basta uma linha para cada campo
    entrada_cod     = criar_campo("Código de barras:", 15, 70)
    entrada_nome    = criar_campo("Nome do produto:", 15, 140)
    
    # Campos lado a lado (Estoque e Valor)
    entrada_estoque = criar_campo("Estoque:", 15, 210, largura=150)
    entrada_valor   = criar_campo("Valor R$:", 185, 210, largura=150)
    
    entrada_venc    = criar_campo("Data de vencimento:", 15, 280, largura=180)

    # --- SELEÇÕES (OPÇÕES) ---
    lbl_opcoes = ctk.CTkLabel(cadastro, text="Categoria / Unid. / Mínimo:", font=fonte_label, text_color=TEXTO_PRINCIPAL)
    lbl_opcoes.place(x=15, y=355)

    escolha_categoria = ctk.CTkOptionMenu(cadastro, values=["Medicamentos", "Rações", "Higiene Pet"], width=140)
    escolha_categoria.place(x=15, y=385)

    escolha_unidade = ctk.CTkOptionMenu(cadastro, values=["UN", "KG", "PCT"], width=70)
    escolha_unidade.place(x=165, y=385)

    escolha_quantidade = ctk.CTkOptionMenu(cadastro, values=["3", "5", "10"], width=70)
    escolha_quantidade.place(x=245, y=385)
    
    lista_widgets = {
        "cod": entrada_cod,
        "nome": entrada_nome,
        "estoque": entrada_estoque,
        "valor": entrada_valor,
        "venc": entrada_venc,
        "cat": escolha_categoria,
        "unid": escolha_unidade,
        "min": escolha_quantidade
    }

    btn_cadastrar = ctk.CTkButton(cadastro, text="CONCLUIR CADASTRO", 
                                  font=("Segoe UI", 16, "bold"), 
                                  fg_color=BTN_CONFIRMAR, hover_color="#059669",
                                  width=300, height=45, 
                                  command= lambda: cadastrar_produto(lista_widgets, cadastro))
    btn_cadastrar.place(relx=0.5, y=520, anchor="center")

    print('Tela cadastro de produtos funcionando')

# Imagem
imagem_3x4 = Image.open("imagens/Pessoa.png")#
icone_3x4 = ctk.CTkImage(dark_image=imagem_3x4, light_image=imagem_3x4, size=(250, 300))

def cadastrar_produto(dados, janela): # Cadastro de produtos
    try: 
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    
        cursor.execute("""
            INSERT INTO estoque (codigobarras, nome, preco, quantidade, categoria, qntminima, unidade, vencimento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            dados["cod"].get(),
            dados["nome"].get(),     # Pegando o nome
            dados["valor"].get(),    # Pegando o valor
            dados["estoque"].get(),  # Pegando a quantidade
            dados["cat"].get(),      # Pegando a categoria (OptionMenu)
            dados["min"].get(),      # Pegando a quantidade mínima (OptionMenu)
            dados["unid"].get(),     # Pegando a unidade (OptionMenu)
            dados["venc"].get()
        ))
        conn.commit()
        print("Produto cadastrado com sucesso!")
        janela.destroy()
    except KeyError as e:
        print(f'Erro: A chave {e} não foi encontrada no dicionário de dados.')
    except Exception as e:
        print(f'Erro geral: {e}')
    except sqlite3.Error as e:
        print(f'Erro no banco de dados: {e}')
        raise e
    finally:
        if conn:
            conn.close()
            print('Conexão com banco de produtos fechada com sucesso.')

# | ====================================== | 
# | Função utilizada para tela de cadastro | 
# | No arquivo views/tela_clientes         | 
# | ====================================== |

def TelaCadastro(parent): # Cadastro de clientes
    cadastro = ctk.CTkToplevel(parent)
    cadastro.title("Cadastrar novo cliente")
    cadastro.geometry("700x580")
    cadastro.attributes("-topmost", True)
    cadastro.grab_set()
    cadastro.configure(fg_color=FUNDO_SECUNDARIO)
    fonte = ctk.CTkFont("Segoe UI", 20)
    
    titulo = ctk.CTkLabel(cadastro, text="Menu de Cadastro", font=("Segoe UI", 30, "bold"), text_color=TEXTO_PRINCIPAL)
    titulo.place(relx=0.5, y=20, anchor="center")
    
    imagem = ctk.CTkLabel(cadastro, image=icone_3x4, text="")
    imagem.place(x=530, y=250, anchor="center")
    
    cadastro.entradas = {}
    
    # Lista responsável pela criação dos títulos de cada opção
    campos = ["Nome completo:", "Email:", "Número:", "CPF:", "Endereço:"]
    # Loop responsável pela criação dos campos de entrada 
    for i, texto in enumerate(campos):
        lbl = ctk.CTkLabel(cadastro, text=texto, font=("Segoe UI", 20, "bold"), text_color=TEXTO_SUBTITULO, height=20)
        lbl.place(x=15, y=50 + (i * 90)) 
        
        entry = ctk.CTkEntry(cadastro, font=fonte, width=320, height=28)
        entry.place(x=15, y=85 + (i * 90))
        cadastro.entradas[texto] = entry
    # Botão
    btn_cadastrar = ctk.CTkButton(cadastro, text="Cadastro", font=("Segoe UI", 20, "bold"), fg_color=BTN_CONFIRMAR, width=150, command=lambda: salvar_dados(cadastro.entradas, cadastro))
    btn_cadastrar.place(relx=0.52, y=520, anchor="nw")
    
    btn_sair = ctk.CTkButton(cadastro, text="Cancelar", fg_color=BTN_CANCELAR, font=("Segoe UI", 20, "bold"), width=150, command=cadastro.destroy)
    btn_sair.place(relx=0.48, y=520, anchor="ne")
    print('Tela cadastro de clientes funcionando')

# Função responsável por salvar os dados e fechar a tela de cadastro de clientes
def salvar_dados(entradas, janela_cadastro):
    dados_limpos = {nome: widget.get() for nome, widget in entradas.items()}
    
    cadastrar_pessoas(dados_limpos, janela_cadastro)
    print('Dados salvos')
    janela_cadastro.destroy()

# Função responsável por cadastras os clientes no banco de dados
def cadastrar_pessoas(dados, janela):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO clientes (nome, numero, cpf, endereco, email)
        VALUES (?, ?, ?, ?, ?)
    """, (
        dados["Nome completo:"],
        dados["Número:"],
        dados["CPF:"],
        dados["Endereço:"],
        dados["Email:"]
    ))
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Pessoa cadastrada!", "Pessoa cadastrada com sucesso!", parent=janela)
    print(f"Cadastro realizado! Dados: {dados}")
    janela.destroy()
    
def EditarProduto(parent, dados_atuais, callback_atualizar):
    editar = ctk.CTkToplevel(parent)
    editar.title("Cadastrar novo produto")
    editar.geometry("400x600") # Ajustei o tamanho para algo mais proporcional
    editar.attributes("-topmost", True)
    editar.grab_set()
    editar.configure(fg_color=FUNDO_SECUNDARIO)
    
    fonte_label = ctk.CTkFont("Segoe UI", 16)
    fonte_entry = ctk.CTkFont("Segoe UI", 14)
    
    # --- FUNÇÃO AUXILIAR PARA CRIAR CAMPOS ---
    def criar_campo(texto, x, y, largura=320):
        lbl = ctk.CTkLabel(editar, text=texto, font=fonte_label, text_color=TEXTO_PRINCIPAL)
        lbl.place(x=x, y=y, anchor="w")
        
        ent = ctk.CTkEntry(editar, fg_color="white", text_color="black", 
                           font=fonte_entry, width=largura, height=30)
        ent.place(x=x, y=y + 25) # Coloca o entry sempre 25px abaixo do label
        return ent

    # Título da Tela
    titulo = ctk.CTkLabel(editar, text="Novo Produto", font=("Segoe UI", 24, "bold"), text_color=TEXTO_PRINCIPAL)
    titulo.place(relx=0.5, y=25, anchor="center")

    # --- GERANDO OS CAMPOS ---
    # Agora basta uma linha para cada campo
    entrada_cod     = criar_campo("Código de barras:", 15, 70)
    entrada_nome    = criar_campo("Nome do produto:", 15, 140)
    
    # Campos lado a lado (Estoque e Valor)
    entrada_estoque = criar_campo("Estoque:", 15, 210, largura=150)
    entrada_valor   = criar_campo("Valor R$:", 185, 210, largura=150)
    
    entrada_venc    = criar_campo("Data de vencimento:", 15, 280, largura=180)

    # --- SELEÇÕES (OPÇÕES) ---
    lbl_opcoes = ctk.CTkLabel(editar, text="Categoria / Unid. / Mínimo:", font=fonte_label, text_color=TEXTO_PRINCIPAL)
    lbl_opcoes.place(x=15, y=355)

    escolha_categoria = ctk.CTkOptionMenu(editar, values=["Medicamentos", "Rações", "Higiene Pet"], width=140)
    escolha_categoria.place(x=15, y=385)

    escolha_unidade = ctk.CTkOptionMenu(editar, values=["UN", "KG", "PCT"], width=70)
    escolha_unidade.place(x=165, y=385)

    escolha_quantidade = ctk.CTkOptionMenu(editar, values=["3", "5", "10"], width=70)
    escolha_quantidade.place(x=245, y=385)
    
    ent_cod = ctk.CTkEntry(editar, width=300)
    ent_cod.insert(0, dados_atuais[1]) # Insere o código atual
    ent_cod.place(x=15, y=90)
    
    ent_nome = ctk.CTkEntry(editar, width=300)
    ent_nome.insert(0, dados_atuais[2]) # Insere o nome atual
    ent_nome.place(x=15, y=165)

    def salvar_edicao():
        novos_dados = (
            entrada_cod.get(),
            entrada_nome.get(),
            entrada_valor.get(),
            entrada_estoque.get(),
            escolha_categoria.get(),
            escolha_quantidade.get(),
            escolha_unidade.get(),
            entrada_venc.get(),
            dados_atuais[0] # O ID para o WHERE
        )
        
        atualizar_produto_db(dados_atuais[0], novos_dados)
        messagebox.showinfo("Sucesso", "Produto atualizado!")
        callback_atualizar() # Chama a função para dar refresh na tabela principal
        editar.destroy()

    btn_salvar = ctk.CTkButton(editar, text="SALVAR ALTERAÇÕES", command=salvar_edicao)
    btn_salvar.place(relx=0.5, y=520, anchor="center")
    print('Função de edição funcionado')