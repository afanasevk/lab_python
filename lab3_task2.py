# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, separator=","):
    set_1 = set(str_1.split(separator))
    set_2 = set(str_2.split(separator))
    intersection = sorted(set_1.intersection(set_2))  # сортировка

    return intersection


participants_first_group = "Иванов|Петров|Сидоров|Антонов|Афанасьев"
participants_second_group = "Афанасьев|Петров|Сидоров|Смирнов|Антонов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print("Общие участники:", find_common_participants(participants_first_group, participants_second_group, "|"))
