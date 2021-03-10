from pprint import pprint

def create_dict_from_file(file_name):
    cook_dict = {}
    with open(file_name, encoding='utf-8') as file_work:
        for line in file_work:
            dish_name = line.lower().strip().capitalize()
            counter = int(file_work.readline())
            list_of_ingredient = []
            for i in range(counter):
                names = ['ingredient_name', 'quantity', 'measure']
                temp_dict = dict(zip(names, (file_work.readline().strip('\n').split(' | '))))
                temp_dict['quantity'] = int(temp_dict['quantity'])
                list_of_ingredient.append(temp_dict)
            cook_dict[dish_name] = list_of_ingredient
            file_work.readline()
    return cook_dict

create_dict_from_file('recipes.txt')

def get_shop_list_by_dishes(dishes, person_count):
    cook_dict = create_dict_from_file('recipes.txt')
    name_lst = []
    ingr_lst = []
    res_dict = {}
    for dish in dishes:
      if dish in cook_dict:
        dict_list = cook_dict[dish]
        for elem_dict in dict_list:
          if elem_dict['ingredient_name'] in res_dict:
            x = elem_dict['ingredient_name']
            y = elem_dict['quantity'] * person_count
            res_dict[x]['quantity'] += y
          else:
            elem_dict['quantity'] *= person_count
            ingr_lst.append(elem_dict)
            name_lst.append(elem_dict.pop('ingredient_name'))
      res_dict.update(dict(zip(name_lst, ingr_lst)))
    return res_dict

pprint(get_shop_list_by_dishes(['Омлет'], 2))
