# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:48:02 2018

@author: sistemas
"""

from Backend import Usuarios
from tkinter import *



class CadastroUser(object):
    def __init__(self, master=None):
        self.fonte = ("Baskerville Old Face","13")
        
        self.container1 = Frame(master) #definção do tamanho do container para receber o button
        self.container1["pady"] = 10
        self.container1.pack()
        
        self.container2 = Frame(master) #definção do tamanho do container para receber o button
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        
        self.container3 = Frame(master) #definção do tamanho do container para receber o button
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        
        self.container4= Frame(master) #definção do tamanho do container para receber o button
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        
        self.container5 = Frame(master) #definção do tamanho do container para receber o button
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        
        self.container6 = Frame(master) #definção do tamanho do container para receber o button
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        
        self.container7 = Frame(master) #definção do tamanho do container para receber o button
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        
        self.container8 = Frame(master) #definção do tamanho do container para receber o button
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        
        self.container9 = Frame(master) #definção do tamanho do container para receber o button
        self.container9["pady"] = 15
        self.container9.pack()
        
        self.titulo = Label(self.container1, text="INFORME OS DADOS") #Definição do titulo e sua fonte
        self.titulo["font"] = ("Baskerville Old Face","20")
        self.titulo.pack()
        
        self.lblidusuario = Label(self.container2, text="idUsuario:", font=self.fonte, width=10) #Legenda da informação que indica o valor a ser inserido ao lado
        self.lblidusuario.pack(side=LEFT)
        
        self.txtidusuario = Entry(self.container2) #função que define o campo onde será inserido os valores
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)
        
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
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
        
        self.lblemail = Label(self.container5, text="E-mail", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        
        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)
        
        self.lblusuario = Label(self.container6, text="Usuário", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
        
        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)
        
        self.lblsenha = Label(self.container7, text="Senha", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        
        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)
        
        self.btnInserir = Button(self.container8, text="Inserir", font=self.fonte, width=12) #definição do button e a função a qual vai chamar
        self.btnInserir["command"] = self.inserirUsuario
        self.btnInserir.pack(side=LEFT)
        
        self.btnAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12) #definição do button e a função a qual vai chamar
        self.btnAlterar["command"] = self.alterarUsuario
        self.btnAlterar.pack(side=LEFT)
        
        self.btnExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12) #definição do button e a função a qual vai chamar
        self.btnExcluir["command"] = self.excluirUsuario
        self.btnExcluir.pack(side=LEFT)
        
        self.lblmsg = Label(self.container9, text="") #Definião do espaço e a fonte da mensagem que aparecera com cada função realizada
        self.lblmsg["font"] = ("Verdana","9","italic")
        self.lblmsg.pack()
        
    def inserirUsuario(self): #Função para inserir o Usuário no Banco de dados
        user = Usuarios() #chamando a class Usuarios do arquivo de conexão com o banco importado acima
  
        user.nome = self.txtnome.get() #Coleta do nome inserido no campo definido
        user.telefone = self.txttelefone.get() #Coleta do Telefone 
        user.email = self.txtemail.get() #Coleta de E-mail
        user.usuario = self.txtusuario.get() #Coleta do Usuário
        user.senha = self.txtsenha.get() #Coleta da Senha
  
        self.lblmsg["text"] = user.insertUser() #Mensagem cadastrada no Arquivo de conexão com o Banco de dados
  
        self.txtidusuario.delete(0, END) #Deleta os dados 
        self.txtnome.delete(0, END) #Deleta os dados
        self.txttelefone.delete(0, END) #Deleta os dados 
        self.txtemail.delete(0, END) #Deleta os dados 
        self.txtusuario.delete(0, END) #Deleta os dados 
        self.txtsenha.delete(0, END) #Deleta os dados 
  
  
  
    def alterarUsuario(self): #Função para Alterar um Usuário já cadastrado dentro do Banco de dados
        user = Usuarios()
  
        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
  
        self.lblmsg["text"] = user.UpdateUser()
  
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
  
  
  
    def excluirUsuario(self): #Função para excluir um Usuário do Banco de dades
        user = Usuarios()
  
        user.idusuario = self.txtidusuario.get()
  
        self.lblmsg["text"] = user.deleUser()
  
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
  
  
    def buscarUsuario(self): #Função para realizar a busca de usuarios do Banco de dados
        user = Usuarios()
  
        idusuario = self.txtidusuario.get()
        
        self.lblmsg["text"] = user.selectUser(idusuario)
  
        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)
  
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
  
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT,user.telefone)
  
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)
  
        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)
  
        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT,user.senha)
 
    
