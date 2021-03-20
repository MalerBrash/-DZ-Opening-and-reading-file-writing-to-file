import os

file_name = 'recipes.txt'


def nest_dict():  
  dish_name = f.readline().strip()  
  count = int(f.readline())
  ingred_dish = list()

  for i in range(count):           
    ingred = f.readline().strip().split('|')    
    part_ingred = {'ingredient_name': ingred[0],'quantity': ingred[1], 'measure': ingred[2]}
    ingred_dish.append(part_ingred)
    cook_book[dish_name] = ingred_dish
  f.readline()  


with open('recipes.txt') as f: 
  cook_book = {
  # 'Омлет': [
  #   {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
  #   {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
  #   {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
  #   ], ...
  }
  count = 0 
  for string in f.readlines():    
    if string.strip('\n').isdigit():      
      count += 1 
  
with open('recipes.txt') as f:
  for line in range(count):
    nest_dict()
  

print('ДЗ №1: ', cook_book, sep='\n') ############################DZ 1


def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for d in dishes:
    try:
      for ingredients in cook_book[d]:            
        if list(ingredients.items())[0][1] in shop_list.keys():
          repeat_quant = shop_list.pop(list(ingredients.items())[0][1])['quantity']
            
          ingredient = (int(list(ingredients.items())[1][1]) * person_count) + repeat_quant, list(ingredients.items())[2][1]
        else:
          ingredient = int(list(ingredients.items())[1][1]) * person_count, list(ingredients.items())[2][1]

        shop_list[list(ingredients.items())[0][1]] = dict(list(zip(('quantity', 'measure'), ingredient)))

    except KeyError:
      print(f'Блюда {dish} нет в книге рецептов')

  print('ДЗ №2: ', shop_list, sep='\n')
 
 
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2) ###################DZ 2


def get_path(names):
  name_files = []
  for name in range(len(names)):    
    file_path = os.path.join(os.getcwd(), 'ad_files', names[name])
    name_files.append(file_path)
  return name_files


def get_min():
  names_files = ['1.txt', '2.txt', '3.txt']
  name_files = get_path(names_files)
  grand = []
  iter_list = []
  for n, i in enumerate(name_files):    
    with open(i, 'r') as r:      
      grand.append([len(r.readlines()), n])

  for i in range(len(grand)):    
    min_res = min(grand)
    grand.remove(min_res)
    iter_list.append(min_res)
  
  for i in iter_list:    
    with open(name_files[i[1]], 'r') as r:
      data = r.read()      
      with open('result.txt', 'a') as f:
        f.write(name_files[i[1]][-5:] + '\n')
        f.write(str(i[0]) + '\n')
        f.write(data + '\n')
    

get_min()############################################################DZ 3
