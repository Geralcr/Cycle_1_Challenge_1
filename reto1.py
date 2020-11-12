# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:11:43 2020

@author: Geraldine Claros
"""

def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
 
 sumaTotalNotas = nota1 + nota2 + nota3 + nota4 + nota5
 valorMinimoNotas = min(nota1, nota2, nota3, nota4, nota5)   
 promedioNotasRango_0_100 = (sumaTotalNotas - valorMinimoNotas) / 4
 promedioNotasRango_0_5 = (promedioNotasRango_0_100 * 5) / 100
 promedioRedondiado = round(promedioNotasRango_0_5, 2)
 return"El promedio ajustado del estudiante {} es: {}".format(codigo,promedioRedondiado)


print(nota_quices("xxx", 19, 90, 38, 55, 68))
print(nota_quices("xxx", 37, 10, 50, 19, 79))
print(nota_quices("xxx", 45, 46, 33, 74, 22))
print(nota_quices("xxx", 57, 100, 87, 93, 21))
print(nota_quices("xxx", 5, 14, 76, 91, 5))
print(nota_quices("xxx", 40, 50, 39, 76, 96))