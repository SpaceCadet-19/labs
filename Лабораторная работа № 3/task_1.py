# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def find_the_index(items_list, find_item):
    if find_item in items_list:
        index = items_list.index(find_item)
        return index

    else:
        return None


for find_item in ['банан', 'груша', 'персик']:
    index_item = find_the_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
