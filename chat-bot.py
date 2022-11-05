empty = []
myList = ['помыться','позавтракать','сделать уроки','пойти на тренировку']

del myList[2]

myList.insert(1,input("Введите новый элемент списка, он встанет на индекс 1"))

myList.remove("пойти на тренировку")

print(myList[1])

print(myList)
