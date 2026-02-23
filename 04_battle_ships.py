rows_number = int(input())

battle_map = []
for each_row in range(rows_number):
    current_row = list(map(int, input().split()))
    battle_map.append(current_row)

destroyed_ships_count = 0
attacks = input().split()
for assault in attacks:
    (row), column = assault.split("-")
    row = int(row)
    column = int(column)

    if battle_map[row][column] > 0:
        battle_map[row][column] -= 1
        if battle_map[row][column] == 0:
            destroyed_ships_count += 1

print(destroyed_ships_count)