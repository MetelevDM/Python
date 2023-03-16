# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных


def vvodDannih():
    with open("spravochnik.txt","a", encoding="utf-8") as data:
        data.write("\n")
        inf=input("Введите ФИО: ")
        data.write(inf)
        data.write("-")
        inf=input("Введите телефон: ")
        data.write(inf+"\n")
        data.close()
        menu()


def poisk():
    with open("spravochnik.txt", encoding="utf-8") as of:
        obiekt=input("Введите что ищем: ")
        for line in of.readlines():
            if obiekt in line:
                print(line,end="")
    menu()
                
    

def poiski():
    with open("spravochnik.txt", encoding="utf-8") as of:
        obiekt=input("Введите что ищем: ")
        for (num,line) in enumerate(of,1):
            if obiekt in line:
                print(num)
                line=000
    menu()

def readAllSpisok():
    with open("spravochnik.txt","r", encoding="utf-8") as of:               
        for line in of.readlines():
            print(line,end="")
    of.close()
    menu()


def killed():
    with open("spravochnik.txt","r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
        f = open("spravochnik.txt","w",encoding="utf-8")
        delet=(input("Введите строку для удаления: "))
        for line in lines:
            if line!=delet+"\n":
                f.write(line)
    f.close()
    menu()


def menu():
    delstr()
    print("Список команд:0-выход из справочника, 1-ввод данных, 2-Поиск по введенному значнию, 3-Вывести весь справочник,4-изменить данные,5-удаление записи")
    number=int(input("Введите команду: "))
    if number==1:
        vvodDannih()
    elif number==2:
        poisk()
    elif number==3:
        readAllSpisok()
    elif number==0:
        exit
    elif number==4:
        changeName()
    elif number==5:
        killed()
    
def changeName():
    with open("spravochnik.txt","r", encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
        f = open("spravochnik.txt","w",encoding="utf-8")
        delet=(input("Введите строку для изменения: "))
        newName=(input("Введите ФИО для занесения в справочник: "))
        newPhone=(input("Введите телефон для занесения в справочник: "))
        for line in lines:
            if line==delet+"\n":
                f.write("\n")
                
                f.write(newName)
                
                f.write(newPhone+"\n")
            else:
                f.write(line)
            
        f.close()
        menu()

    
def exit():
    print("До встречи")

# menu()
def delstr():
    with open("spravochnik.txt","r", encoding="utf-8") as f:
        lines=f.readlines()
        f.close()
        with open("spravochnik.txt","w", encoding="utf-8") as o:
            for line in lines:
                if line.strip():
                    o.write(line)
        o.close()

menu()