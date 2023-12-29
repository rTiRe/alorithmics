"""
В неориентированный взвешенный граф добавляют ребра. 
Напишите программу, которая, после добавления ребер, 
    находит сумму весов ребер в компоненте связности.
На вход подаются два числа n и m - количество вершин в графе и 
    количество производимых добавлений и запросов. 
Далее следует список `add` из m строк. 
Каждая строка состоит из трех чисел x, y, w.
Это означает, что в граф добавляется ребро из 
    вершины x в вершину y веса w. 
Кратные ребра допустимы. 
И число `A` - вершина, для компоненты связности которой 
    необходимо найти суммарный вес ребер.
"""