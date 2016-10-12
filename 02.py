#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/12/2016 U.S.A



#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações. 


usuario = input("Nome usuario: ")
senha = input("Senha usuario: ")
usuario_db = ['edward','pedro','iale']
senha_db = ['123','1234','12345']
while usuario not in usuario_db or senha not in senha_db:
    print("Nome ou senhas invalidos: ")
    usuario = input("Nome usuario: ")
    senha = input("Senha usuario: ")
if usuario in usuario_db and senha in senha_db:
    user1 = usuario_db.index(usuario)
    senha1 = senha_db.index(senha)
    if user1 == senha1:
        print("(+) Usuarios e senhas corretos!")
    if user1 != senha:
        print("(-) Usuario e senha invalidos!")
