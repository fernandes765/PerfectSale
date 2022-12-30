# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 09:37:34 2018

@author: jhonata
"""
from tkinter import *
from Backend import *

class Venda(object):
    def __init__(self, idUsuario=0, nome="", cpf="", cnpj="", codigoProduto=0, descricao = "", embalagem = "", qtEntrada = 0, preco =0.00, codigoFornecedor = 0):
        
        window = Tk()
        window.colormapwindows()
        
        self.fonte = ("Baskerville Old Face","10")
        self.fonte2 = ("Baskerville Old Face","13")
        
        self.lblcodigoProduto = Label(window, text="Código do Produto", font=self.fonte)
        self.lbldescricao = Label(window, text="Descrição", font=self.fonte)
        self.lblpreco = Label(window, text="Preço", font=self.fonte)
        self.txtcodProd = Entry(window)
        self.txtdescricao = Entry(window)
        self.txtpreco = Entry(window)
        
        self.ent_codigoProduto = Entry(window)
        self.ent_qtProd = Entry(window)
        self.btn_buscar = Button(window, text="Buscar", font=self.fonte2)
        self.btn_inserir = Button(window, text="inserir", font=self.fonte2)
        self.btn_salvar = Button(window, text="Salvar", font=self.fonte2)
        self.btn_limpar = Button(window, text="Limpar", font=self.fonte2)
        
        self.lblcodigoProduto.grid(row=1, column=0, padx=5, pady=3, sticky='N')
        self.lbldescricao.grid(row=1, column=1, padx=5, pady=3, sticky='N')
        self.lblpreco.grid(row=1, column=3, padx=5, pady=3, sticky='N')
        self.ent_codigoProduto.grid(row=0, column=0, padx=5, pady=3, sticky='N')
        self.ent_qtProd.grid(row=0, column=1, padx=5, pady=3, sticky='N')
        self.btn_buscar.grid(row=0, column=4, padx=5, pady=3, sticky='WE')
        self.btn_inserir.grid(row=0, column=5, padx=5, pady=3, sticky='WE')
        self.btn_salvar.grid(row=5, column=5, padx=5, pady=3, sticky='WE')
        self.btn_limpar.grid(row=5, colum=4, padx=5, pady=3, sticky='WE')
        self.txtcodProd.grid(row=2, column=0, padx=5, pady=3, sticky='N')
        self.txtdescricao.grid(row=2, column=1, padx=5, pady=3, sticky='N')
        self.txtpreco.grid(row=2, column=3, padx=2, pady=2, sticky='N')
        
        self.btn_buscar["command"]= self.buscarProduto
        self.btn_inserir["command"]= self.inserirProduto
        
        self.lblmsg = Label(window, text="")
        self.lblmsg.grid(row=30, column=0, padx=30, pady=30, sticky='WE')
        
    def buscarProduto(self):
        func = FuncoesdeVendas()
        
        cod_prod = self.ent_codigoProduto.get()#coleta a informação do código do produto segundo o que o usuário digitar
  
        self.lblmsg["text"] = func.selectProd(cod_prod)# mensagens  retornadas no banco
        
        self.txtcodProd.insert(INSERT, func.cod_prod)
        self.txtdescricao.insert(INSERT, func.descricao)
        self.txtpreco.insert(INSERT, func.preco)
        
    def inserirProduto(self):
        func = FuncoesdeVendas
        
        cod_prod = self.ent_codigoProduto.get()
        
        self.lblmsg["text"] = func.inserirProd(cod_prod)
        
#window = Tk()
#window.title('Perfect Sale')
#Venda(window)
#window.mainloop()