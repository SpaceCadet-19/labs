list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2
#общее кол-во игроков
count_of_players = len(list_players)
first_team = list_players[:middle_index] #первая половина
second_team = list_players[middle_index:] #вторая половина

print(first_team)
print(second_team)
