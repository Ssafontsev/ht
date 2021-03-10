from pprint import pprint
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_name_by_number(number):
  for doc_number in documents:
    if doc_number["number"] == number:
      print(doc_number["name"])
      break
  else:
    print('Такого номера документа нет в базе./')
  return
def get_shelf_by_number(value):
  for k, v in directories.items():
    if value in v:
      print(k)
      break
  print('Такого номера документа нет в базе.')
  return
def get_list():
    for lines in documents:
        print('{} "{}" "{}"'.format(lines['type'], lines['number'], lines['name']))
    return
def add_document(number, type, name, shelf_number):
    dict = {"type": type, "number": number, "name": name}
    documents.append(dict)
    if shelf_number in directories.keys():
        directories[shelf_number].append(number)
    pprint(documents)
    print(directories)
    return

add_document("222", "passport", "Иван Иванов", "1")

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.