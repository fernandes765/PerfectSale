# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 09:37:34 2018

@author: sistemas
"""
from tkinter import *
from Backend import *
from CadastroCliente import CadastroCli
from CadastroProduto import CadastroProd
#from CadastrarFornecedor import Application
from CadastroUsuario import CadastroUser
from Venda import Venda
#from Atividades import Application

class Menu(object):
    
    def __init__(self, master=None):
        self.fonte = ("Verdana","8")
        
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        
        self.container4= Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        
        self.titulo = Label(self.container1, text="""Cadastro de Produto""")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()
        
        self.btnCadastCli = Button(self.container1, text="Cadastrar/Alterar Clientes", font=self.fonte, width=80, height=5)
        self.btnCadastCli["command"] = self.cadastrar_alterar_clientes
        self.btnCadastCli.pack(side=LEFT)
        
        self.btnCadastProd = Button(self.container2, text="Cadastrar/Alterar Produtos", font=self.fonte, width=80, height=5)
        self.btnCadastProd["command"] = self.cadastrar_alterar_produtos
        self.btnCadastProd.pack(side=LEFT)
        
        self.btnCadasForn = Button(self.container3, text="Cadastrar/Alterar Fornecedores", font=self.fonte, width=80, height=5)
        self.btnCadasForn["command"] = self.cadastrar_alterar_fornecedores
        self.btnCadasForn.pack(side=LEFT)
        
        self.btnCadastUser = Button(self.container4, text="Cadastrar/Alterar Usuários", font=self.fonte, width=80, height=5)
        self.btnCadastUser["command"] = self.cadastrar_alterar_usuarios
        self.btnCadastUser.pack(side=LEFT)
        
        self.btnVender = Button(self.container5, text="Realizar Venda", font=self.fonte, width=80, height=5)
        self.btnVender["command"] = self.vender
        self.btnVender.pack(side=LEFT)
        
        #self.btnAtividades = Button(self.container6, text="Atividades", font=self.fonte, width=80, height=5)
        #self.btnAtividades["command"] = self.atividades
        #self.btnAtividades.pack(side=LEFT)
        
    def cadastrar_alterar_clientes(self):
        root = Tk()
        root.title('Perfect Sale')
        CadastroCli(root)
        root.mainloop()
        

    def cadastrar_alterar_produtos(self):
        root = Tk()
        root.title('Perfect Sale')
        CadastroProd(root)
        root.mainloop()
        
            

    def cadastrar_alterar_fornecedores(self):
        pass
        
    
    def cadastrar_alterar_usuarios(self):
        root = Tk()
        root.title('Perfect Sale')
        CadastroUser(root)
        root.mainloop()
        
        
    
    def vender(self):
        Venda(window)
        window.mainloop()
        
        
    
    def atividades(self):
        pass
        
    def closeRoot(self):              
        self.destroy()

root = Tk()
root.title('Perfect Sale')
root.geometry('800x600')
Menu(root)
root.mainloop()