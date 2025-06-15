
#из методички 

"""- 5 11 9
10 - 8 7
7 14 - 8
12 6 15 -"""



#Функция нахождения минимального элемента, исключая текущий элемент
def Min(lst,myindex):
    return min(x for index, x in enumerate(lst) if index != myindex)

#функция удаления нужной строки и столбцах
def Delete(matrix,index1,index2):
    del matrix[index1]
    for i in matrix:
        del i[index2]
    return matrix

#Функция вывода матрицы
def PrintMatrix(matrix):
    print("---------------")
    for i in range(len(matrix)):
        print(matrix[i])
    print("---------------")

n=int(input("Последовательно введите количество элементов матрицы, саму матрицу\n"))
matrix=[]
H=0 #сумма констант привидения
Lenght_of_path=0
Stroka=[]
Stolbec=[]
res=[]
result=[]
StartMatrix=[]

#Инициализируем массивы для сохранения индексов
for i in range(n):
    Stroka.append(i)
    Stolbec.append(i)

#Вводим матрицу
# Вводим матрицу
for i in range(n):
    row = input().split()
    matrix.append([float('inf') if x == '-' else int(x) for x in row])
	
#Сохраняем изначальную матрицу
for i in range(n):StartMatrix.append(matrix[i].copy())

#Присваеваем главной диагонали float(inf)
for i in range(n): matrix[i][i]=float('inf')

while True:
    #Редуцируем
    #--------------------------------------
    #Вычитаем минимальный элемент в строках
    for i in range(len(matrix)):
        temp=min(matrix[i])
        H+=temp
        for j in range(len(matrix)):
            matrix[i][j]-=temp

    #Вычитаем минимальный элемент в столбцах    
    for i in range(len(matrix)):
        temp = min(row[i] for row in matrix)
        H+=temp
        for j in range(len(matrix)):
            matrix[j][i]-=temp
    #--------------------------------------
	
    #Оцениваем нулевые клетки и ищем нулевую клетку с максимальной оценкой, самый тяжелый нуль
    #--------------------------------------
    NullMax=0
    index1=0
    index2=0
    tmp=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==0:
                tmp=Min(matrix[i],j)+Min((row[j] for row in matrix),i)
                if tmp>=NullMax:
                    NullMax=tmp
                    index1=i
                    index2=j
    #--------------------------------------

	#Находим нужный нам путь, записываем его в res и удаляем все ненужное
    res.append(Stroka[index1]+1)
    res.append(Stolbec[index2]+1)
	
    oldIndex1=Stroka[index1]
    oldIndex2=Stolbec[index2]
    if oldIndex2 in Stroka and oldIndex1 in Stolbec:
        NewIndex1=Stroka.index(oldIndex2)
        NewIndex2=Stolbec.index(oldIndex1)
        matrix[NewIndex1][NewIndex2]=float('inf')
    del Stroka[index1]
    del Stolbec[index2]
    # Если длина матрицы 2x2, выводим её и завершаем
    if len(matrix) == 2:
        print("Последняя матрица 2x2:")
        PrintMatrix(matrix)

    matrix = Delete(matrix, index1, index2)

    if len(matrix) == 1:
        break
	
#Формируем порядок пути
for i in range(0,len(res)-1,2):
	if res.count(res[i])<2:
		result.append(res[i])
		result.append(res[i+1])
for i in range(0,len(res)-1,2):
	for j in range(0,len(res)-1,2):
		if result[len(result)-1]==res[j]:
			result.append(res[j])
			result.append(res[j+1])
print("----------------------------------")
print([[result[i], result[i + 1]] for i in range(0, len(result), 2)])

#Считаем длину пути
for i in range(0,len(result)-1,2):
    if i==len(result)-2:
        Lenght_of_path+=StartMatrix[result[i]-1][result[i+1]-1]
        Lenght_of_path+=StartMatrix[result[i+1]-1][result[0]-1]
    else: Lenght_of_path+=StartMatrix[result[i]-1][result[i+1]-1]
print(Lenght_of_path)
print("----------------------------------")
input()
