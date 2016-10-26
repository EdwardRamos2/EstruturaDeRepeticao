#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/12/2016 U.S.A


"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; 
"""

nome = ''
idade = 0
salario = 0
sexo = ''
civil = ''

while len(nome) <= 3:
    nome = str(input("Nome: maior que 3 caracteres: "))
print("(+) Nome correto! %s" % nome)

while idade < 1 or idade > 150:
    idade = int(input("Idade: entre 1 e 150: "))
print("(+) Idade Correta! %s" % idade)


while salario < 1:
    salario = float(input("Salario: maior que zero: "))
print("(+) Salario ok: %r" % salario)

while sexo != 'f'  and sexo != 'm':
  sexo = input('Sexo: m - Masculino f - Feminino:')
if 'm' in sexo: 
    print("(+) Sexo Masculino: %s" % sexo)
if 'f' in sexo:
    print("(+) Sexo Feminino: %s" % sexo)


while civil != 's'  and civil != 'c' and civil != 'v' and civil != 'd':
   civil = input("Estado Civil: 's - Solteiro', 'c - Casado', 'v - Viuvo', 'd - Divorsiado'")
   
if 's' in civil:
    print("(+) Estado civil: SOLTEIRO: %s" % civil)
if 'c' in civil:
    print("(+) Estado civil: CASADO: %s" % civil)
if 'v' in civil:
    print("(+) Estado civil: VIUVO: %s" % civil)
if 'd' in civil:
    print("(+) Estado civil: DIVORSIADO: %s" % civil)

