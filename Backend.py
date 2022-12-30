# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 08:27:16 2018

@author: jhonata
"""
import sqlite3

class Banco(object):
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableUser()
        self.createTableProd()
        self.createTableClient()
        self.createTableFornec()
        self.createTablePedido()
        
    def fetchall(self):
        return self.cursor.fetchall()
        
    def createTableUser(self):
        c = self.conexao.cursor()
        
        c.execute("""create table if not exists usuarios(
                idusuario integer primary key autoincrement,
                nome text,
                telefone text,
                email text,
                usuario text,
                senha text)""")
        
    def createTableProd(self):
        c = self.conexao.cursor()
        
        c.execute("""create table if not exists produtos(
                cod_prod integer primary key autoincrement,
                descricao text,
                embalagem text,
                qt_ent integer,
                preco float,
                cod_forn integer)""")
        
        
    def createTableClient(self):
        c = self.conexao.cursor()
        
        c.execute("""create table if not exists clientes(
                cpf integer unique,
                cnpj integer unique,
                cod_cli integer primary key autoincrement,
                nome text,
                telefone text,
                email text,
                endereco text)""")
        
        
    def createTableFornec(self):
        c = self.conexao.cursor()
        
        c.execute("""create table if not exists fornecedores(
                cnpj integer unique,
                inscricao_estadual integer unique,
                razao_social text,
                telefone text,
                primary key (cnpj,inscricao_estadual))""")
     
    def createTablePedido(self):
        c = self.conexao.cursor()
        
        c.execute("""create table if not exists pedidos(
                numPedido integer primary key autoincrement,
                cod_prod integer,
                descrecicao text,
                preco float,
                qt_prod integer,
                idusuario integer,
                cod_cli integer,
                nome_cli text,
                data date,
                foreign key (cod_prod) references produtos (cod_prod),
                foreign key (cod_cli) references clientes (cod_cli),
                foreign key (idusuario) references usuarios (idusuario))""")
        
        self.conexao.commit()
        c.close()

class Clientes(object):
    
    def __init__(self, cpf = 0, cnpj = 0, cod_cli =0 , nome = "", telefone = "", email = "", endereco = ""):
        self.info = {}
        self.cpf = cpf
        self.cnpj = cnpj
        self.cod_cli = cod_cli
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        
    def insertCli(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("insert into clientes(cpf, cnpj, nome, telefone, email, endereco) values ('"+ self.cpf + "' , '"+ self.cnpj + "' , '" + self.nome + "' , '" + self.telefone + "' , '" + self.email + "' , '" + self.endereco + "')")
            
            banco.conexao.commit()
            c.close()
            
            return "Cliente Cadastrado com Sucesso!"
        except:
            return "Ocorreu um Erro na inserção do Cliente"
    
    def UpdateCli(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("update cliente set nome = '"+ self.cpf + "' , '"+ self.cnpj + "' , '" + self.nome + "',  telefone = '" + self.telefone + "', email = '" + self.email + "', endereco = '" + self.endereco + "' where cod_cli = " + self.cod_cli + " ")
            
            banco.conexao.commit()
            c.close()
            
            return "Cliente atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do Cliente"
        
    def deleCli(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("delete from clientes where cod_cli = " + self.cod_cli + " ")
            
            banco.conexao.commit()
            c.close()
            
            return "Usuário excluido com sucesso!"
        except:
            return "Ocorreu um erro ao excluir o usuário"
        
    def selectCli(self, cod_cli):
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute ("select * from clientes where cod_cli =" + cod_cli + " ")
            
            for linha in c.fetchall():
                self.cpf = linha[0]
                self.cnpj = linha[1]
                self.cod_cli = linha[3]
                self.nome = linha[4]
                self.telefone = linha[5]
                self.email = linha[6]
                self.endereco = linha[7]
            
            c.close()
            
            return "Busca Realizada com Sucesso!"
        except:
            return "Ocorreu um erro na busca do cliente, por favor escolher um cliente valido!"

class Produtos(object):
    
    def __init__(self, codigoProduto = 0, descricao = "", embalagem = "", qtEntrada = "", preco = "", codigoFornecedor = ""):
        self.info = {}
        self.codigoProduto = codigoProduto
        self.descricao = descricao
        self.embalagem = embalagem
        self.qtEntrada = qtEntrada
        self.preco = preco
        self.codigoFornecedor = codigoFornecedor
        
    def insertProd(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("insert into produtos(descricao, embalagem, qt_ent, preco, cod_forn) values ('" + self.descricao+ "' , '" + self.embalagem + "' , '" + self.qtEntrada + "' , '" + self.preco + "' , '" + self.codigoFornecedor + "')")
            
            banco.conexao.commit()
            c.close()
            
            return "Produto Cadastrado com Sucesso!"
        except:
            return "Ocorreu um Erro na inserção do Produto"
    
    def UpdateProd(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("update produtos set descricao = '" + self.descricao + "',  embalagem = '" + self.embalagem + "', qt_ent = '" + self.qtEntrada + "', preco = '" + self.preco + "', cod_forn = '" + self.codigoFornecedor + "' where cod_prod = " + self.codigoProduto + " ")
            
            banco.conexao.commit()
            c.close()
            
            return "Produto atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do Produto"
        
    def deleProd(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("delete from produtos where cod_prod = " + self.codigoProduto + " ")
            
            banco.conexao.commit()
            c.close()
            
            return "Produto excluido com sucesso!"
        except:
            return "Ocorreu um erro ao excluir o Produto"
        
    def selectProd(self, codigoProduto):
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute ("select * from produtos where cod_prod =" + codigoProduto + " ")
            
            for linha in c.fetchall():
                self.codigoProduto = linha[0]
                self.descricao = linha[1]
                self.embalagem = linha[2]
                self.qtEntrada = linha[3]
                self.preco = linha[4]
                self.codigoFornecedor = linha[5]
            
            c.close()
            
            return "Busca Realizada com Sucesso!"
        except:
            return "Ocorreu um erro na busca do Produto, por favor escolher um Produto valido!"    

class Usuarios(object):
    
    def __init__(self, idusuario = 0, nome = "", telefone = "", email = "", usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha
        
    def insertUser(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("insert into usuarios(nome, telefone, email, usuario, senha) values ('" + self.nome+ "' , '" + self.telefone + "' , '" + self.email + "' , '" + self.usuario + "' , '" + self.senha + "')")
            
            banco.conexao.commit()
            c.close()
            
            return "Usuário Cadastrado com Sucesso!"
        except:
            return "Ocorreu um Erro na inserção do Usuário"
    
    def UpdateUser(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("update usuarios set nome = '" + self.nome + "',  telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where idusuario = " + self.idusuario + " ")
            
            banco.conexao.commit()
            c.close()
            
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
        
    def deleUser(self):
        
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")
            
            banco.conexao.commit()
            c.close()
            
            return "Usuário excluido com sucesso!"
        except:
            return "Ocorreu um erro ao excluir o usuário"
        
    def selectUser(self, idusuario):
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute ("select * from usuarios where idusuario =" + idusuario + " ")
            
            for linha in c.fetchall():
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
            
            c.close()
            
            return "Busca Realizada com Sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário, por favor escolher um usuário valido!"
    
    def loginUser(self):
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute ("select usuario, senha from usuarios where usuario="+ self.usuario +" and senha = " + self.senha + "")
            
            c.close()
            
            return "Login Realizado com Sucesso!"
        except:
            return "Login incorreto, Usuário  ou senha incorreta!"
        
class FuncoesdeVendas(object):
    def __init__(self, cod_prod=0, descricao="", preco=0.00, qt_prod=0, idusuario=0, cod_cli=0, nome_cli="", data='00-00-0000'):
        self.cod_prod = cod_prod
        self.descricao = descricao
        self.preco = preco
        self.qt_prod = qt_prod
        self.idusuario = idusuario
        self.cod_cli = cod_cli
        self.nome_cli = nome_cli
        self.data = data
        
    def selectProd(self, cod_prod):
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("select cod_prod, descricao, preco from produtos where cod_prod ="+cod_prod+"")
            
            for linha in c.fetchall():
                self.cod_prod = linha[0]
                self.descricao = linha[1]
                self.preco = linha[3]
            
            c.close()
            
            return "Busca realizada com sucesso!"
        except:
            return "Produto Não localizado"

    def inserirProd(self):
        banco = Banco()
        try:
            
            c = banco.conexao.cursor()
            
            c.execute("insert into pedidos(cod_prod, descricao, qt_prod, preco, idusuario, cod_cli, nome_cli, data) values ('"+self.cod_prod+"','"+self.descricao+"','"+self.qt_prod+"','"+self.preco+"','"+self.idusuario+"','"+self.cod_cli+"','"+self.nome_cli+"','"+self.data+"')")
            
            banco.conexao.commit()
            
            banco.close()
            
            return "Pedido"
        except:
            return "erro ao inserir produto!"