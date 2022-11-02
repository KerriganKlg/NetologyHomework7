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

import os

BASE_DIR = os.getcwd()
FILES_DIR_NAME = "Files"

file_path = os.path.join(BASE_DIR, FILES_DIR_NAME)
files = os.listdir(file_path)

file_dict = {}
for string in files:
    name = os.path.join(file_path, string)
    with open(name, encoding='utf-8') as file:
        lines = file.readlines()
        text = []
        len_text = len(lines)
        for line in lines:
            text.append(line.strip())
        file_dict[string] = (len_text, text)

sorted_values = sorted(file_dict.values())
sorted_dict = {}

for position in sorted_values:
    for lenght in file_dict.keys():
        if file_dict[lenght] == position:
            sorted_dict[lenght] = file_dict[lenght]
            break

with open('merge_file.txt', "w", encoding='utf-8') as file:
    for key, value in sorted_dict.items():
        file.write(f"{key}\n")
        file.write(f"{value[0]}\n")
        for val in value[1]:
            file.write(f"{val}\n")