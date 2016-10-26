#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/04/2016 U.S.A


#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
#e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
#A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 


populacaoA,populacaoB,anos  = 80000, 200000, 0
print(populacaoA,populacaoB,anos)
crescimentoA,crescimentoB = 0.03, 0.015
print(crescimentoA,crescimentoB)

while populacaoA < populacaoB:
    anos += 1
    populacaoA = populacaoA + (populacaoA * crescimentoA)
    populacaoB = populacaoB + (populacaoB * crescimentoB)
    print('Em %d  a populacao A ira ultrapassar a populacaoB' % anos) 
    print('Quantidade da populacao A e %r' % populacaoA)
    print('Quantidade da populacao B e %r' % populacaoB) 

