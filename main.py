# | ============================ |
# | Arquivo main responsável por |
# | iniciar o programa           | 
# | ============================ | 

import customtkinter as ctk
from views.app import App
from database import conectar, criar_tabelas
from views.utils import aviso_manutencao

def main():
    conn = conectar()
    criar_tabelas(conn)
    
    app = App(conn)
    app.mainloop()
    
    conn.close()
    
if __name__ == "__main__":
    main()
