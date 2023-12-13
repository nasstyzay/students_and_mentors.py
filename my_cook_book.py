with open('recipes.txt, "r'):
    data = f.read()
    print(data)
def my_cook_book():
    with open('recipes.txt', encoding="utf-8") as file:
        cook_book = {}
        data = file.read().split('\n\n')
    for recipes in data:
        recipe_info = recipes.split('\n')
        recipe_name = recipe_info[0]
        ingredients = []
        for ingredient_line in recipe_info[2:]:
            ingredient_name, quantity, measure = ingredient_line.split('|')
            ingredients.append({
                "название": ingredient_name,
                "количество": int(quantity),
                "шт": measure
            })

        cook_book[recipe_name] = ingredients

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
        get_shop_list_by_dishes(dishes, person_count)
        print(['Запеченный картофель', 'Омлет'], 2)


