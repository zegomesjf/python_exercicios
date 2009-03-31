#encoding: latin1
"""Faça um programa para imprimir:
            1
            2    2
            3    3   3
            .....
            n    n   n   n    n    n   ... n
     para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""

def imprimir(valor):
    if isinstance(valor, int):
        x = 1
        while x <= valor:
            y = 1
            texto = ''
            while y <= x:                
                texto += str(x) + "\t"
                y += 1
            print texto
            x += 1
