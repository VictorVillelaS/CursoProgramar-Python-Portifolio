from front import *

app = tk.Tk()
frmPreferencias = FrmPreferencias(app)
frmPreferencias.pack()

app.mainloop()

"""
TODO:
-Construir BLL da tabela Parentes
- OK: Fazer Stringbuilder na DAL
-Nomear os parâmetros do edit
-Adicionar mensagens de confirmação para adicionar, editar e deletar
"""