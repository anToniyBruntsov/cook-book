with open('book.txt', encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        ingredients_count = int(file.readline())
        ingredients_list = []
        for i in range(ingredients_count):
            name, quantity, measure = file.readline().strip().split(' | ')
            ingredients_list.append({
                'ingredient_name': name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish.strip()] = ingredients_list
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ticket = {}
    for _dish in dishes:
        _ingredients_list = cook_book.get(_dish)
        for _ingredients in _ingredients_list:
            _name, _quantity, _measure = _ingredients.values()
            if _name in ticket:
                q = str(ticket.get(_name))
                x = int(''.join(filter(str.isdigit, q)))
                ticket[_name] = {int(_quantity) * person_count + x: _measure}
            else:
                ticket[_name] = {int(_quantity) * person_count: _measure}
    print(ticket)


get_shop_list_by_dishes(['Омлет', 'Борщ'], 2)
