task = 'Домашняя работа по уроку "Функции в Python.Функция с параметром"'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
def get_matrix(n, m, volue):
    matrix = []
    for i in range(n):
        matrix1 = []
        for j in range(m):
            matrix1.append(volue)
        matrix.append(matrix1)
    #print('Кол-во в ячейке:', matrix1)
    print('Результат: ', matrix)
# Исходный код
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
#print(result1)
#print(result2)
#print(result3)
print()
print(thanks)