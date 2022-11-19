def provpas(parol):
    for sim in ["п","о","л","к",";",".",",","$"]:
        for elem in str(parol):
            if sim == elem:
                print("Неверный пароль")

parol = input("Введите парольь:")
provpas(parol)
    
