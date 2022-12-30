# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:16:31 2018

@author: jhonata
"""

class Usuarios():
    window = Tk()

    window.wm_title('Cadastro de Usuário')
    window.resizable(False, False)
    
    txtidusuario = int()
    txtnome = StringVar()
    txttelefone = StringVar()
    txtemail = StringVar()
    txtusuario = StringVar()
    txtsenha = StringVar()
    
    lblidusuario = Label(window, text='Código')
    lblnome = Label(window, text='Nome')
    lbltelefone = Label(window, text='Telefone')
    lblemail = Label(window, text='Email')
    lblusuario = Label(window, text='Usuário')
    lblsenha = Label(window, text='Senha')
    
    entidusuario = Entry(window, textvariable=txtidusuario)
    entnome = Entry(window, textvariable=txtnome)
    enttelefone = Entry(window, textvariable=txttelefone)
    entemail = Entry(window, textvariable=txtemail)
    entusuario = Entry(window, textvariable=txtusuario)
    entsenha = Entry(window, textvariable=txtsenha)

    list_usuarios = Listbox(window)
    scroll_usuarios = Scrollbar(window)

    btn_listar = Button(window, text='Listar todos')
    btn_buscar = Button(window, text='Buscar')
    btn_inserir = Button(window, text='Inserir')
    btn_atualizar = Button(window, text='Atualizar Selecionados')
    btn_remover = Button(window, text='Remove Selecionados')
    btn_fechar = Button(window, text='Fechar')
    
    lblidusuario.grid(row=0, column=0, padx=5, pady=3, sticky='N')
    lblnome.grid(row=1, column=0, padx=5, pady=3, sticky='N')
    lbltelefone.grid(row=2, column=0, padx=5, pady=3, sticky='N')
    lblemail.grid(row=3, column=0, padx=5, pady=3, sticky='N')
    lblusuario.grid(row=4, column=0, padx=5, pady=3, sticky='N')
    lblsenha.grid(row=5, column=0, padx=5, pady=3, sticky='N')
    entidusuario.grid(row=0, column=1, padx=5, pady=3, sticky='N')
    entnome.grid(row=1, column=1, padx=5, pady=3, sticky='N')
    enttelefone.grid(row=2, column=1, padx=5, pady=3, sticky='N')
    entemail.grid(row=3, column=1, padx=5, pady=3, sticky='N')
    entusuario.grid(row=4, column=1, padx=5, pady=3, sticky='N')
    entsenha.grid(row=5, column=1, padx=5, pady=3, sticky='N')
    list_usuarios.grid(row=0, column=2, rowspan=10, padx=0, pady=0, sticky='NS')
    scroll_usuarios.grid(row=0, column=6, rowspan=10, padx=0, pady=0, sticky='NS')
    btn_listar.grid(row=6, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_buscar.grid(row=7, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_inserir.grid(row=8, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_atualizar.grid(row=9, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_remover.grid(row=10, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
    btn_fechar.grid(row=11, column=0, columnspan=2, padx=5, pady=3, sticky='WE')
        
    list_usuarios.configure(yscrollcommand=scroll_usuarios.set)
    
    scroll_usuarios.configure(command=list_usuarios.yview)

    def run(self):
        Usuarios.window.mainloop()    