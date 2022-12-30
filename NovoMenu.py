# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:08:43 2018

@author: jhonata
"""

from tkinter import *
from Backend import *
from CadastroCliente import CadastroCli
from CadastroProduto import CadastroProd
#from CadastrarFornecedor import Application
from CadastroUsuario import CadastroUser
from Venda import Venda
#from Atividades import Application
import tkinter as tk
class NovoMenu(object):
    
    def __init__(self,master=None):
        
        
        self.fonte=("Baskerville Old Face","20")
        self.fonte2=("Baskerville Old Face","13")
        
        self.titulo = Label(window, text='MENU', font=self.fonte)
        self.btn_cadastroCli = Button(window, text='Cadastrar/Alterar Cliente', font=self.fonte2, width=40, height=1)
        self.btn_cadastroUser = Button(window, text='Cadastrar/Alterar Usuário', font=self.fonte2, width=40, height=1)
        self.btn_cadastroProd = Button(window, text='Cadastrar/Alterar Produto', font=self.fonte2, width=40, height=1)
        self.btn_cadastroForn = Button(window, text='Cadastrar/Alterar Fornecedor', font=self.fonte2, width=40, height=1)
        self.btn_atividades = Button(window, text='Relatorio de Atividades', font=self.fonte2, width=40, height=1)
        self.btn_venda = Button(window, text='Realizar Venda', font=self.fonte2, width=40, height=1)
        
        self.titulo.grid(row=0, column=0, padx=5, pady=5)
        self.btn_cadastroCli.grid(row=1, column=0, padx=100, pady=5)
        self.btn_cadastroUser.grid(row=2, column=0, padx=100, pady=5)
        self.btn_cadastroForn.grid(row=3, column=0, padx=100, pady=5)
        self.btn_cadastroProd.grid(row=4, column=0, padx=100, pady=5)
        self.btn_venda.grid(row=5, column=0, padx=100, pady=5)
        self.btn_atividades.grid(row=6, column=0, padx=100, pady=5)
        
        
        self.btn_cadastroCli["command"]= self.cadastrar_alterar_clientes
        self.btn_cadastroUser["command"]= self.cadastrar_alterar_usuarios
        self.btn_cadastroForn["command"]= self.cadastrar_alterar_fornecedores
        self.btn_cadastroProd["command"]= self.cadastrar_alterar_produtos
        self.btn_atividades["command"]= self.atividades
        self.btn_venda["command"]= self.vender
        
        
        
        
        
        
        
    def cadastrar_alterar_clientes(self):
        
        root = Tk()
        root.title('Perfect Sale')
        root.geometry("1366x768")
        CadastroCli(root)
        root.mainloop()
        
        

        

    def cadastrar_alterar_produtos(self):
        root = Tk()
        root.title('Perfect Sale')
        root.geometry("1366x768")
        CadastroProd(root)
        root.mainloop()
        
            

    def cadastrar_alterar_fornecedores(self):
        pass
        
    
    def cadastrar_alterar_usuarios(self):
        root = Tk()
        root.title('Perfect Sale')
        root.geometry("1366x768")
        CadastroUser(root)
        root.mainloop()
        
        
    
    def vender(self):
        window.title('Perfect Sale')
        window.geometry("1366x768")
        Venda(window)
        window.mainloop()
        
        
    
    def atividades(self):
        pass
        
        
window = Tk()
window.title('Perfect Sale')
window.geometry("1366x768")
NovoMenu(window)

imagem = tk.PhotoImage(file="C:/Users/Rodolfo/Pictures/perfectsale.png")
w = tk.Label(window, image=imagem)
w.place(relwidth=1, relheight=1)
w.imagem = imagem
w.grid()


#window.configure(background='OrangeRed2')


window.mainloop()