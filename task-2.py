# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, div_=','):
    s1=set(str1.split(div_))
    s2=set(str2.split(div_))
    inter=sorted(list(s1.intersection(s2)))
    return inter
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))