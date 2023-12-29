"""
Даны N процессов.
Каждый процесс может быть запущен сразу,
    а может быть только после выполнения 
    некоторого количествапредыдущих процессов. 
Список зависимостей дан в списке depend.
depend[i] - список процессов, от которых зависит процесс i. 
Найти порядок, в котором необходимо выполнять процессы, 
    чтобы зависимый процесс начинался после выполнения предыдущих. 
    Если таких порядков несколько, верните любой. 
Гарантируется, что существует хотя бы один процесс, 
    который не имеет зависимостей.
"""