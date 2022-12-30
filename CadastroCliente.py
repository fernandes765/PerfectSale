# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 08:12:25 2018

@author: sistemas
"""
from Backend import Clientes
from tkinter import *
import tkinter as tk
class CadastroCli(object):
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
        
        self.titulo = Label(self.container1, text="INFORME OS DADOS")
        self.titulo["font"] = ("Baskerville Old Face", "20")
        self.titulo.pack()
        
        self.lblcod_cli = Label(self.container2, text="Código:", font=self.fonte, width=10)
        self.lblcod_cli.pack(side=LEFT)
        
        self.txtcod_cli = Entry(self.container2)
        self.txtcod_cli["width"] = 10
        self.txtcod_cli["font"] = self.fonte
        self.txtcod_cli.pack(side=LEFT)
        
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarCliente
        self.btnBuscar.pack(side=RIGHT)
        
        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)
        
        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        
        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)
        
        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        
        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)
        
        self.lblcpf = Label(self.container6, text="CPF:", font=self.fonte, width=10)
        self.lblcpf.pack(side=LEFT)
        
        self.txtcpf = Entry(self.container6)
        self.txtcpf["width"] = 25
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side=LEFT)
        
        self.lblcnpj = Label(self.container7, text="CNPJ:", font=self.fonte, width=10)
        self.lblcnpj.pack(side=LEFT)
        
        self.txtcnpj = Entry(self.container7)
        self.txtcnpj["width"] = 25
        self.txtcnpj["font"] = self.fonte
        self.txtcnpj.pack(side=LEFT)
        
        self.btnInserir = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.btnInserir["command"] = self.inserirCliente
        self.btnInserir.pack(side=LEFT)
        
        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        #self.btnAlterar["command"] = self.alterarCliente
        self.btnAlterar.pack(side=LEFT)
        
        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        #self.btnExcluir["command"] = self.excluirCliente
        self.btnExcluir.pack(side=LEFT)
        
        self.lblmsg = Label(self.container9, text="")
        #self.lblmsg["font"] = ("Verdana","9","italic")
        self.lblmsg.pack()
        
    def buscarCliente(self):
        cli = Clientes()
  
        cod_cli = self.txtcod_cli.get()
        
        self.lblmsg["text"] = cli.selectCli(cod_cli)
  
        self.txtcod_cli.delete(0, END)
        self.txtcod_cli.insert(INSERT, cli.cod_cli)
  
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, cli.nome)
  
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT,cli.telefone)
  
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, cli.email)
  
        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT, cli.cpf)
  
        self.txtcnpj.delete(0, END)
        self.txtcnpj.insert(INSERT,cli.cnpj)
        
    def inserirCliente(self):
        cli = Clientes()
        
        cod_cli = self.txtcod_cli.get()
        nome = self.txtnome.get()
        telefone = self.txttelefone.get()
        email = self.txtemail.get()
        cpf = self.txtcpf.get()
        cnpj = self.txtcnpj.get()
    

