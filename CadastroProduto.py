# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 08:12:44 2018

@author: sistemas
"""

from Backend import Produtos
from tkinter import * 

class CadastroProd(object):
    def __init__(self, master=None):
        self.fonte = ("Baskerville Old Face","13")
        
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
        
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
        
        self.titulo = Label(self.container1, text="""CADASTRO DO PRODUTO""")
        self.titulo["font"] = ("Baskerville Old Face","20")
        self.titulo.pack()
        
        self.lblcodigoProduto = Label(self.container2, text="Cód.Produto:", font=self.fonte, width=10)
        self.lblcodigoProduto.pack(side=LEFT)
        
        self.txtcodigoProduto = Entry(self.container2)
        self.txtcodigoProduto["width"] = 10
        self.txtcodigoProduto["font"] = self.fonte
        self.txtcodigoProduto.pack(side=LEFT)
        
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarProduto
        self.btnBuscar.pack(side=RIGHT)
        
        self.lbldescricao = Label(self.container3, text="Descrição:", font=self.fonte, width=10)
        self.lbldescricao.pack(side=LEFT)
        
        self.txtdescricao = Entry(self.container3)
        self.txtdescricao["width"] = 25
        self.txtdescricao["font"] = self.fonte
        self.txtdescricao.pack(side=LEFT)
        
        self.lblembalagem = Label(self.container4, text="Embalagem:", font=self.fonte, width=10)
        self.lblembalagem.pack(side=LEFT)
        
        self.txtembalagem = Entry(self.container4)
        self.txtembalagem["width"] = 25
        self.txtembalagem["font"] = self.fonte
        self.txtembalagem.pack(side=LEFT)
        
        self.lblqtEntrada = Label(self.container5, text="QT. Entrada:", font=self.fonte, width=10)
        self.lblqtEntrada.pack(side=LEFT)
        
        self.txtqtEntrada = Entry(self.container5)
        self.txtqtEntrada["width"] = 25
        self.txtqtEntrada["font"] = self.fonte
        self.txtqtEntrada.pack(side=LEFT)
        
        self.lblpreco = Label(self.container6, text="Preço:", font=self.fonte, width=10)
        self.lblpreco.pack(side=LEFT)
        
        self.txtpreco = Entry(self.container6)
        self.txtpreco["width"] = 25
        self.txtpreco["font"] = self.fonte
        self.txtpreco.pack(side=LEFT)
        
        self.lblcodigoFornecedor = Label(self.container7, text="Cód. Forn.:", font=self.fonte, width=10)
        self.lblcodigoFornecedor.pack(side=LEFT)
        
        self.txtcodigoFornecedor = Entry(self.container7)
        self.txtcodigoFornecedor["width"] = 25
        self.txtcodigoFornecedor["font"] = self.fonte
        self.txtcodigoFornecedor.pack(side=LEFT)
        
        self.btnInserir = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.btnInserir["command"] = self.inserirProduto
        self.btnInserir.pack(side=LEFT)
        
        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"] = self.alterarProduto
        self.btnAlterar.pack(side=LEFT)
        
        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excluirProduto
        self.btnExcluir.pack(side=LEFT)
        
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana","9","italic")
        self.lblmsg.pack()
        
    def inserirProduto(self):
        prod = Produtos()
  
        prod.descricao = self.txtdescricao.get()
        prod.embalagem = self.txtembalagem.get()
        prod.qt_ent = self.txtqtEntrada.get()
        prod.preco = self.txtpreco.get()
        prod.cod_forn = self.txtcodigoFornecedor.get()
  
        self.lblmsg["text"] = prod.insertProd()
  
        self.txtcodigoProduto.delete(0, END)
        self.txtdescricao.delete(0, END)
        self.txtembalagem.delete(0, END)
        self.txtqtEntrada.delete(0, END)
        self.txtpreco.delete(0, END)
        self.txtcodigoFornecedor.delete(0, END)
  
  
  
    def alterarProduto(self):
        prod = Produtos()
  
        prod.cod_prod = self.txtcodigoProduto.get()
        prod.descricao = self.txtdescricao.get()
        prod.embalagem = self.txtembalagem.get()
        prod.qt_ent = self.txtqtEntrada.get()
        prod.preco = self.txtpreco.get()
        prod.cod_forn = self.txtcodigoFornecedor.get()
  
        self.lblmsg["text"] = prod.UpdateProd()
  
        self.txtcodigoProduto.delete(0, END)
        self.txtdescricao.delete(0, END)
        self.txtembalagem.delete(0, END)
        self.txtqtEntrada.delete(0, END)
        self.txtpreco.delete(0, END)
        self.txtcodigoFornecedor.delete(0, END)
  
  
  
    def excluirProduto(self):
        prod = Produtos()
  
        prod.cod_prod = self.txtcodigoProduto.get()
  
        self.lblmsg["text"] = prod.deleProd()
  
        self.txtcodigoProduto.delete(0, END)
        self.txtdescricao.delete(0, END)
        self.txtembalagem.delete(0, END)
        self.txtqtEntrada.delete(0, END)
        self.txtpreco.delete(0, END)
        self.txtcodigoFornecedor.delete(0, END)
  
  
    def buscarProduto(self):
        prod = Produtos()
  
        cod_prod = self.txtcodigoProduto.get()
  
        self.lblmsg["text"] = prod.selectProd(cod_prod)
  
        self.txtcodigoProduto.delete(0, END)
        self.txtcodigoProduto.insert(INSERT, prod.codigoProduto)
  
        self.txtdescricao.delete(0, END)
        self.txtdescricao.insert(INSERT, prod.descricao)
  
        self.txtembalagem.delete(0, END)
        self.txtembalagem.insert(INSERT, prod.embalagem)
  
        self.txtqtEntrada.delete(0, END)
        self.txtqtEntrada.insert(INSERT, prod.qtEntrada)
  
        self.txtpreco.delete(0, END)
        self.txtpreco.insert(INSERT, prod.preco)
  
        self.txtcodigoFornecedor.delete(0, END)
        self.txtcodigoFornecedor.insert(INSERT,prod.codigoFornecedor)
    
        
        
  
  
  
