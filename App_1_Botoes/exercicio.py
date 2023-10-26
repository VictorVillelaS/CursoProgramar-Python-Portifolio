# Criar uma janela com um botão
# Definir posição e título da janela
# Formatar cor do botão, posição e mensagem

from tkinter import *
from tkinter import messagebox

def MensagemEnviada():
    messagebox.showinfo(title='Notificação', message='Mensagem enviada!')


def MensagemSimNao():
    if messagebox.askyesno(title='Responda', message='Sim ou não???'):
        messagebox.showinfo(title='Sim', message='Sim!')
    else:
        messagebox.showinfo(title='Não', message='Não!')


def MensagemSimNaoCancel():
    estado = messagebox.askyesnocancel(title='Responda', message='Sim, não, ou não escolher?')
    match estado:
        case True:
            estado = 'Sim'
        case False:
            estado = 'Não'
        case None:
            estado = 'Cancel'
    messagebox.showinfo(title=f'{estado}', message=f'Então você escolheu {estado}')


def MensagemYNCacncelElif():
    estado = messagebox.askyesnocancel(title='Responda', message='Sim, não, ou não escolher?')
    if estado == True:
        messagebox.showinfo(title='Sim :]', message='Isso é um sim!')
    elif estado == False:
        messagebox.showinfo(title='Não :[', message='Isso é um não...')
    elif estado == None:
        messagebox.showinfo(title='Sem escolha...', message='Nenhuma escolha foi feita')


Janela = Tk()
Janela.geometry('320x360+100+100')
Janela.title = 'Mensagem'


BotaoDisplay = Button(Janela, text='Mostrar mensagem', width=30, height=1, fg='black', bg='grey',
                      command=MensagemEnviada)
BotaoDisplay.place(x=10,y=10)


BotaoSimNao = Button(Janela, text='Sim ou não?', width=30, height=1, fg='black', bg='grey',
                     command=MensagemSimNao)
BotaoSimNao.place(x=10, y=60)


BotaoSimNaoCancel = Button(Janela, text = 'Sim, não... talvez, cancel', width=30, height=1, fg='black', bg='grey',
                           command=MensagemSimNaoCancel)
BotaoSimNaoCancel.place(x=10, y=110)


BotaoSimNaoCancel = Button(Janela, text = 'Sim, não ou sem escolha?', width=30, height=1, fg='black', bg='grey',
                           command=MensagemYNCacncelElif)
BotaoSimNaoCancel.place(x=10, y=160)


Janela.mainloop()
#tempo limite: 20 minutos
#tempo de código: 18min, 13sec