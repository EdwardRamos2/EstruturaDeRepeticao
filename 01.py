#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/12/2016 U.S.A

"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
"""

nota = float(input("Nota: "))
while nota >= 10:
    print("(+) Invalido")
    nota = float(input("Nota: "))
print("(+) Valor valido: %r" % nota)
