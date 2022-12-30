# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:15:16 2018

@author: jhonata
"""

from tkinter import *


class Clientes:
    window = Tk()

    window.wm_title('Cadastro de Clientes')
    window.resizable(False, False)
    
    txtcod_cli = int()
    txtnome = StringVar()
    txttelefone = StringVar()
    txtemail = StringVar()
    txtcpf = StringVar()
    txtcnpj = StringVar()
    
    lblcod_cli = Label(window, text='Código')
    lblnome = Label(window, text='Nome')
    lbltelefone = Label(window, text='Telefone')
    lblemail = Label(window, text='Email')
    lblcpf = Label(window, text='CPF')
    lblcnpj = Label(window, text='CNPJ')
    
    entcod_cli = Entry(window, textvariable=txtcod_cli)
    entnome = Entry(window, textvariable=txtnome)
    enttelefone = Entry(window, textvariable=txttelefone)
    entemail = Entry(window, textvariable=txtemail)
    entcpf = Entry(window, textvariable=txtcpf)
    entcnpj = Entry(window, textvariable=txtcnpj)

    list_clientes = Listbox(window)
    scroll_clientes = Scrollbar(window)

    btn_listar = Button(window, text='Listar todos')
    btn_buscar = Button(window, text='Buscar')
    btn_inserir = Button(window, text='Inserir')
    btn_atualizar = Button(window, text='Atualizar Selecionados')
    btn_remover = Button(window, text='Remove Selecionados')
    btn_fechar = Button(window, text='Fechar')
    
    lblcod_cli.grid(row=0, column=0, padx=5, pady=3, sticky='N')
    lblnome.grid(row=1, column=0, padx=5, pady=3, sticky='N')
    lbltelefone.grid(row=2, column=0, padx=5, pady=3, sticky='N')
    lblemail.grid(row=3, column=0, padx=5, pady=3, sticky='N')
    lblcpf.grid(row=4, column=0, padx=5, pady=3, sticky='N')
    lblcnpj.grid(row=5, column=0, padx=5, pady=3, sticky='N')
    entcod_cli.grid(row=0, column=1, padx=5, pady=3, sticky='N')
    entnome.grid(row=1, column=1, padx=5, pady=3, sticky='N')
    enttelefone.grid(row=2, column=1, padx=5, pady=3, sticky='N')
    entemail.grid(row=3, column=1, padx=5, pady=3, sticky='N')
    entcpf.grid(row=4, column=1, padx=5, pady=3, sticky='N')
    entcnpj.grid(row=5, column=1, padx=5, pady=3, sticky='N')
    list_clientes.grid(row=0, column=2, rowspan=10, padx=0, pady=0, sticky='NS')
    scroll_clientes.grid(row=0, column=6, rowspan=10, padx=0, pady=0, sticky='NS')
    btn_listar.grid(row=6, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_buscar.grid(row=7, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_inserir.grid(row=8, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_atualizar.grid(row=9, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_remover.grid(row=10, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_fechar.grid(row=11, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
        
    list_clientes.configure(yscrollcommand=scroll_clientes.set)
    
    scroll_clientes.configure(command=list_clientes.yview)

    def run(self):
        Clientes.window.mainloop()