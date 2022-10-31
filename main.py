def get_recipes (recipes_file ='./recipies.txt'):
    cook_book = {}
    with open(recipes_file, "r", encoding="utf-8") as receipt_file:
        while True:
            dish = receipt_file.readline().rstrip('\n').lower() or receipt_file.readline().rstrip('\n, \n').lower()
            if not dish:
                break
            cook_book[dish] = []
            ingridient_amount = int(receipt_file.readline().rstrip('\n'))
            items = [receipt_file.readline().rstrip('\n').rsplit('|') for _ in range(ingridient_amount)]
            for item in items:
                cook_book[dish].append({'ingridient_name': item[0].rstrip(),
                                        'quantity': int(item[1].replace(' ', '')),
                                        'measure': item[2].replace(' ', '')})
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете '
                   'на одного человека (через запятую: Омлет, Утка По-Пекински, '
                   'Запеченный Картофель или Фахитос) ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)

cook_book = get_recipes()
create_shop_list(cook_book)

# Задача №3
def files_len(file1='./1.txt', file2='./2.txt', file3='./3.txt'):
    merge_file = "merge_file.txt"
    with open(file1, "r", encoding="utf-8") as file1len:
        file1 = file1len.readlines()

    with open(file2, "r", encoding="utf-8") as file2len:
        file2 = file2len.readlines()

    with open(file3, "r", encoding="utf-8") as file3len:
        file3 = file3len.readlines()

    with open(merge_file, "w", encoding="utf-8") as mergefile:
        if len(file1) < len(file2) and len(file1) < len(file3):
            mergefile.write("Имя файла: 1.txt" + '\n')
            mergefile.write("Длина файла в строках: " + str(len(file1)) + '\n')
            mergefile.writelines(file1)
            mergefile.write('\n' + '\n')
        elif len(file2) < len(file1) and len(file2) < len(file3):
            mergefile.write("Имя файла: 2.txt" + '\n')
            mergefile.write("Длина файла в строках: " + str(len(file2)) + '\n')
            mergefile.writelines(file2)
            mergefile.write('\n' + '\n')
        elif len(file3) < len(file1) and len(file3) < len(file2):
            mergefile.write("Имя файла: 3.txt" + '\n')
            mergefile.write("Длина файла в строках: " + str(len(file3)) + '\n')
            mergefile.writelines(file3)
            mergefile.write('\n' + '\n')
        if len(file1) < len(file2) and len(file2) < len(file3) or len(file1) > len(file2) and len(file2) > len(file3):
            mergefile.write("Имя файла: 2.txt" + '\n')
            mergefile.write("Длина файла в строках: " + str(len(file2)) + '\n')
            mergefile.writelines(file2)
            mergefile.write('\n' + '\n')
        elif len(file3) < len(file1) and len(file1) < len(file2) or len(file3) > len(file1) and len(file1) > len(file2):
            mergefile.write("Имя файла: 1.txt" + '\n')
            mergefile.write("Длина файла в строках: " + str(len(file1)) + '\n')
            mergefile.writelines(file1)
            mergefile.write('\n' + '\n')
        elif len(file2) < len(file3) and len(file3) < len(file1) or len(file2) > len(file3) and len(file3) > len(file1):
            mergefile.write("Имя файла: 3.txt" + '\n')
            mergefile.write("Длина файла в строках: " + str(len(file3)) + '\n')
            mergefile.writelines(file3)
            mergefile.write('\n' + '\n')
        if len(file1) > len(file2) and len(file1) > len(file3):
            mergefile.write("Имя файла: 1.txt" + '\n')
            mergefile.write("Длина файла в строках: " + str(len(file1)) + '\n')
            mergefile.writelines(file1)
            mergefile.write('\n' + '\n')
        elif len(file2) > len(file1) and len(file2) > len(file3):
            mergefile.write("Имя файла: 2.txt" + '\n')
            mergefile.write("Длина файла в строках: " + str(len(file2)) + '\n')
            mergefile.writelines(file2)
            mergefile.write('\n' + '\n')
        elif len(file3) > len(file1) and len(file3) > len(file2):
            mergefile.write("Имя файла: 3.txt" + '\n')
            mergefile.write("Длина файла в строках: " + str(len(file3)) + '\n')
            mergefile.writelines(file3)
            mergefile.write('\n' + '\n')

files_len ()

