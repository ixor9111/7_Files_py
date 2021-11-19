import os


def get_cook_book(path):
    cook_book = {}

    with open(path, encoding='utf-8') as file:
        for recipe in file:
            recipe_name = recipe.strip()
            cook_book[recipe_name] = []

            amount_ingredients = int(file.readline().strip())
            for ingredient in range(amount_ingredients):
                line = file.readline().strip().split(' | ')
                cook_book[recipe_name].append({'ingredient_name': line[0], 'quantity': line[1], 'measure': line[2]})

            file.readline()

        return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    ingredients = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            quantity_by_persons = int(ingredient['quantity']) * person_count

            if ingredient['ingredient_name'] in ingredients:
                ingredients[ingredient['ingredient_name']]['quantity'] += quantity_by_persons
            else:
                ingredients[ingredient['ingredient_name']] = {}
                ingredients[ingredient['ingredient_name']].setdefault('measure', ingredient['measure'])
                ingredients[ingredient['ingredient_name']].setdefault('quantity', quantity_by_persons)

    return ingredients


cook_book = get_cook_book('recipes.txt')
print(cook_book)
print(get_shop_list_by_dishes(cook_book, ['Омлет', 'Фахитос'], 2))

# --------------3е задание--------------
file1 = open('1.txt', encoding='utf-8')
file2 = open('2.txt', encoding='utf-8')
file3 = open('3.txt', encoding='utf-8')
files = [file1, file2, file3]

temp_data = {}
for file in files:
    file_list = list(file.readlines())
    file_name = os.path.basename(file.name)
    file_lines_count = len(file_list)

    temp_data[file_name] = {}
    temp_data[file_name]['lines_count'] = file_lines_count
    temp_data[file_name]['text'] = file_list

file1.close()
file2.close()
file3.close()

data = sorted(temp_data.items(), key=lambda item: item[1]['lines_count'])

main_file = open('main_file.txt', 'w', encoding='utf-8')

for elem in data:
    main_file.write(elem[0] + '\n')
    main_file.write(str(elem[1]['lines_count']) + '\n')

    for line in elem[1]['text']:
        main_file.write(line)

    main_file.write('\n')
