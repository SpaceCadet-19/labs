# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(participants_first_group, participants_second_group, pr = ','):
    split_first_participants = participants_first_group.split(pr)
    split_second_participants = participants_second_group.split(pr)
    in_every_group = set(split_second_participants).intersection(set(split_first_participants))
    in_every_group = list(in_every_group)
    in_every_group.sort()
    return in_every_group
print(find_common_participants(participants_first_group,participants_second_group))
