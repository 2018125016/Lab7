import re

def sort_by_count(item):
    return -item[1] 

with open('input_7_2.txt', 'r') as input_file:
    text = input_file.read().upper()
    
    counting_dict = {chr(i): 0 for i in range(65, 91)}

    matches = re.findall(r'\w', text)
    for match in matches:
        if match in counting_dict:
            counting_dict[match] += 1

counting_list = list(counting_dict.items())

counting_list.sort(key=sort_by_count)

sorted_characters = [char for char, count in counting_list if count > 0]

print(sorted_characters)
