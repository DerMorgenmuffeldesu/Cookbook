def create_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            cook_book[dish_name] = []
            number_of_ingredients = int(file.readline().strip())
            for i in range(number_of_ingredients):
                ingredients_info = file.readline().strip().split(' | ')
                name_of_ingredient = ingredients_info[0]
                quantity_of_ingredient = int(ingredients_info[1])
                measure_of_ingredient = ingredients_info[2]
                ingredient = {
                    'ingredient_name': name_of_ingredient,
                    'quantity': quantity_of_ingredient,
                    'measure': measure_of_ingredient
                }
                cook_book[dish_name].append(ingredient)
            file.readline()
    return cook_book


cook_book_result = create_cook_book('recipes.txt')


def print_cook_book(dictionary):
    print("cook_book = {")
    for dish, ingredients in dictionary.items():
        print("  '{}' : [".format(dish))
        for ingredient in ingredients:
            print("    {}, ".format(ingredient))
        print("  ],")
    print("}")


print_cook_book(cook_book_result)

#Задание 2
print()
def get_shop_list_by_dishes(person_count: int, dishes: list, cook_book):
		result = {}
		for dish in dishes:
				if dish in cook_book:
						for consist in cook_book[dish]:
								if consist['ingredient_name'] in result:
										result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
								else:
										result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
				else:
						print('Такого блюда нет в книге')
		print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'], cook_book_result)