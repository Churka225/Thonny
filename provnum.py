myList = ['346','543','441']

def provnum(numbers):
    for sim in ["0","2","7","8","9"]:
        for elem in str(numbers):
            if sim == elem:
                print("Числа не совпадают")
            if sim != ["1","3","4","5","6"]:
                print("Числа совпадают")
                
numbers = input("Введите число")
provnum(numbers)
